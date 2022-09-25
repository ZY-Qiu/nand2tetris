# -*- coding: utf-8 -*-
"""
Crself.eated on Sat Oct 31 19:26:58 2020

@author: QiuGeGe
"""

from Tokenizer import JackTokenizer
from SymbolTable import SymbolTable
from utils import prepare_data

class CompliationEngine():
    def __init__(self, new_data, data):
        self.new_data = new_data
        self.data = data
        self.tknzr = JackTokenizer()
        self.ClassTable = SymbolTable()
        self.SubroutineTable = SymbolTable()
        self.NameTable = SymbolTable()
        self.token_list = 0
        self.output = []
        self.count = 0
        self.inden = 2
    
    def run(self):
        self.token_list = prepare_data(self.data)
        print("Data prepare complete!")
        self.tknzr.advance(self.token_list[self.tknzr.count:])
        print("Advance! Go compile class!")
        self.CompileClass()
        # 可以两次编译，目的是在第一次更新所有的subroutine定义
        self.write()
        print("Complete!")
        print("."*80)
        return
    
    def CompileClass(self):
        self.output.append(self.count*self.inden*" "+"<class>")
        self.count += 1
        
        self.eat("class")  # class
        self.NameTable.put(self.tknzr.token, None, "class")
        self.eat(self.tknzr.token)  # main...
        
        self.eat("{")
        while (self.tknzr.token == "field" or self.tknzr.token == "static"):
            print("Advance! Go compile ClassVarDec!")
            self.CompileClassVarDec()
        while (self.tknzr.token == "constructor" or 
               self.tknzr.token == "function" or 
               self.tknzr.token == "method"):
            print("Advance! Go compile SubroutineDec!")
            self.CompileSubroutineDec()
        self.eat("}")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</class>")
    
    def CompileClassVarDec(self):
        self.output.append(self.count*self.inden*" "+"<classVarDec>")
        self.count += 1
        self.ClassTable = SymbolTable()
        
        kind = self.tknzr.token
        self.eat(self.tknzr.token)  #field or static
        typ = self.tknzr.token
        self.eat(self.tknzr.token)  #int, bolean, char or class type var
        name = self.tknzr.token
        self.ClassTable.put(name, typ, kind)
        self.eat(self.tknzr.token)  #x...
        
        while (self.tknzr.token == ","):
            self.eat(",")
            self.ClassTable.put(self.tknzr.token, typ, kind)
            self.eat(self.tknzr.token)  #y...
        self.eat(";")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</classVarDec>")
    
    def CompileSubroutineDec(self):
        self.output.append(self.count*self.inden*" "+"<subroutineDec>")
        self.count += 1
        
        self.SubroutineTable = SymbolTable()
        
        kind = "subroutine"
        self.eat(self.tknzr.token)  # constructor, function, method
        typ = self.tknzr.token
        self.eat(self.tknzr.token)  # void, int...
        name = self.tknzr.token
        self.NameTable.put(name, typ, kind)
        self.eat(self.tknzr.token)  # main...
        
        self.eat("(")
        print("Advance! Go compile ParameterList!")
        self.CompileParameterList()
        self.eat(")")
        print("Advance! Go compile SubroutineBody!")
        self.CompileSubroutineBody()
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</subroutineDec>")
    
    def CompileParameterList(self):
        self.output.append(self.count*self.inden*" "+"<parameterList>")
        self.count += 1
        if(self.tknzr.token != ")"):
            
            kind = "argument"
            typ = self.tknzr.token
            self.eat(self.tknzr.token)  # int, bolean, char or class type var
            name = self.tknzr.token
            self.SubroutineTable.put(name, typ, kind)
            self.eat(self.tknzr.token)  # x...
            
            while(self.tknzr.token == ","):
                self.eat(",")
                typ = self.tknzr.token
                self.eat(self.tknzr.token)
                name = self.tknzr.token
                self.SubroutineTable.put(name, typ, kind)
                self.eat(self.tknzr.token)
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</parameterList>")
    
    def CompileSubroutineBody(self):
        self.output.append(self.count*self.inden*" "+"<subroutineBody>")
        self.count += 1
        self.eat("{")
        while(self.tknzr.token == "var"):
            print("Advance! Go compile VarDec!")
            self.CompileVarDec()
        print("Advance! Go compile Statements!")
        self.CompileStatements()
        self.eat("}")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</subroutineBody>")
    
    def CompileVarDec(self):
        self.output.append(self.count*self.inden*" "+"<varDec>")
        self.count += 1
        
        kind = "local"
        self.eat("var")  # var
        typ = self.tknzr.token
        self.eat(self.tknzr.token)  # int, bolean, char or class type var
        name = self.tknzr.token
        self.SubroutineTable.put(name, typ, kind)
        self.eat(self.tknzr.token)  # x...
        
        while(self.tknzr.token == ","):
            self.eat(",")
            self.SubroutineTable.put(self.tknzr.token, typ, kind)
            self.eat(self.tknzr.token) #varName
        self.eat(";")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</varDec>")
    
    def CompileStatements(self):
        self.output.append(self.count*self.inden*" "+"<statements>")
        self.count += 1
        while (self.tknzr.token != "}"):
            if (self.tknzr.token == "let"):
                print("Advance! Go compile Let!")
                self.CompileLet()
            elif (self.tknzr.token == "if"):
                print("Advance! Go compile if!")
                self.CompileIf()
            elif (self.tknzr.token == "while"):
                print("Advance! Go compile while!")
                self.CompileWhile()
            elif (self.tknzr.token == "do"):
                print("Advance! Go compile do!")
                self.CompileDo()
            elif (self.tknzr.token == "return"):
                print("Advance! Go compile return!")
                self.CompileReturn()
            else:
                print(self.tknzr.token)
                raise Exception("No string matches the requirments!")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</statements>")
    
    def CompileLet(self):
        self.output.append(self.count*self.inden*" "+"<letStatement>")
        self.count += 1
        self.eat("let")
        self.eat(self.tknzr.token)
        if (self.tknzr.token == "["):
            self.eat("[")
            print("Advance! Go compile Expression!")
            self.CompileExpression()
            self.eat("]")
        self.eat("=")
        print("Advance! Go compile Expression!")
        self.CompileExpression()
        self.eat(";")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</letStatement>")
    
    def CompileIf(self):
        self.output.append(self.count*self.inden*" "+"<ifStatement>")
        self.count += 1
        self.eat("if")
        self.eat("(")
        print("Advance! Go compile Expression!")
        self.CompileExpression()
        self.eat(")")
        self.eat("{")
        print("Advance! Go compile Statements!")
        self.CompileStatements()
        self.eat("}")
        if (self.tknzr.token == "else"):
            self.eat("else")
            self.eat("{")
            print("Advance! Go compile Statements!")
            self.CompileStatements()
            self.eat("}")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</ifStatement>")
    
    def CompileWhile(self):
        self.output.append(self.count*self.inden*" "+"<whileStatement>")
        self.count += 1
        self.eat("while")
        self.eat("(")
        print("Advance! Go compile Expression!")
        self.CompileExpression()
        self.eat(")")
        self.eat("{")
        print("Advance! Go compile Statements!")
        self.CompileStatements()
        self.eat("}")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</whileStatement>")
    
    def CompileDo(self):
        self.output.append(self.count*self.inden*" "+"<doStatement>")
        self.count += 1
        self.eat("do")
        self.eat(self.tknzr.token)
        if(self.tknzr.token == "("): #subroutinName(expressionList)
            self.eat("(")
            print("Advance! Go compile ExpressionList!")
            self.CompileExpressionList()
            self.eat(")")
        elif(self.tknzr.token == "."): #varName|className.subroutinName(expressionList)
            self.eat(".")
            
            kind = "subroutine"
            name = self.tknzr.token
            self.NameTable.put(name, None, kind)
            self.eat(self.tknzr.token)  # subroutine name

            self.eat("(")
            print("Advance! Go compile ExpressionList!")
            self.CompileExpressionList()
            self.eat(")")
        self.eat(";")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</doStatement>")
    
    def CompileReturn(self):
        self.output.append(self.count*self.inden*" "+"<returnStatement>")
        self.count += 1
        self.eat("return")
        if (self.tknzr.token != ";"):
            print("Advance! Go compile Expression!")
            self.CompileExpression()
        self.eat(";")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</returnStatement>")
    
    def CompileExpression(self):
        self.output.append(self.count*self.inden*" "+"<expression>")
        self.count += 1
        print("Advance! Go compile Term!")
        self.CompileTerm()
        if (self.tknzr.classification == "SYMBOL"):
            while (self.tknzr.token != "]" and self.tknzr.token != ")" and 
                   self.tknzr.token != ";" and self.tknzr.token != ","):
                self.eat(self.tknzr.token)
                print("Advance! Go compile Term!")
                self.CompileTerm()
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</expression>")
    
    def CompileExpressionList(self):
        self.output.append(self.count*self.inden*" "+"<expressionList>")
        self.count += 1
        if (self.tknzr.token != ")"):
            print("Advance! Go compile Expression!")
            self.CompileExpression()
            while (self.tknzr.token == ","):
                self.eat(",")
                print("Advance! Go compile Expression!")
                self.CompileExpression()
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</expressionList>")
    
    def CompileTerm(self):
        self.output.append(self.count*self.inden*" "+"<term>")
        self.count += 1
        if (self.tknzr.classification == "KEYWORD" or
            self.tknzr.classification == "INT_CONST" or
            self.tknzr.classification == "STRING_CONST"):
            self.eat(self.tknzr.token)
        elif (self.tknzr.classification == "SYMBOL"): #(expression)
            if (self.tknzr.token == "("):
                self.eat("(")
                self.CompileExpression()
                self.eat(")")
            elif(self.tknzr.token == "-" or self.tknzr.token == "~"):                                     #
                self.eat(self.tknzr.token)
                self.CompileTerm()
        elif(self.tknzr.classification == "IDENTIFIER"):
            self.eat(self.tknzr.token)
            if(self.tknzr.token == "["): #varName[expression]
                self.eat("[")
                self.CompileExpression()
                self.eat("]")
            elif(self.tknzr.token == "("): #subroutinName(expressionList)
                self.eat("(")
                self.CompileExpressionList()
                self.eat(")")
            elif(self.tknzr.token == "."): #varName|className.subroutinName(expressionList)
                self.eat(".")
                
                kind = "subroutine"
                name = self.tknzr.token
                self.NameTable.put(name, None, kind)
                self.eat(self.tknzr.token)  # subroutine name
                
                self.eat("(")
                print("Advance! Go compile ExpressionList!")
                self.CompileExpressionList()
                self.eat(")")
            #varName
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</term>")
    
    def eat(self, string):
        if (self.tknzr.token != string):
            print(self.output)
            print(string)
            print(self.tknzr.token)
            raise Exception("Strings do not match!")
        elif(self.tknzr.classification == "KEYWORD"):
            self.output.append(self.count*self.inden*" "+"<keyword> "+
                               string+" </keyword>")
            self.tknzr.advance(self.token_list[self.tknzr.count:])
        elif(self.tknzr.classification == "SYMBOL"):
            self.output.append(self.count*self.inden*" "+"<symbol> "+
                               string+" </symbol>")
            if(self.tknzr.hasMoreTokens(self.token_list)):
                self.tknzr.advance(self.token_list[self.tknzr.count:])
            else:
                return
            
        elif(self.tknzr.classification == "IDENTIFIER"):
            
            data = self.ClassTable.get(self.tknzr.token)
            data2 = self.SubroutineTable.get(self.tknzr.token)
            data3 = self.NameTable.get(self.tknzr.token)
            
            for i in reversed(self.output):
                if(i.count(" ", 0, self.count*self.inden) != self.count*self.inden):
                    Dec = i
                    break
            if("<class>" in Dec or "<classVarDec>" in Dec or "<subroutineDec>" in Dec or 
               "<parameterList>" in Dec or "<varDec>" in Dec):
                pass

            
            if(data2):
                if("<parameterList>" in Dec or "<varDec>" in Dec):
                    self.output.append(self.count*self.inden*" "+"<identifier_{}_{}_defined> ".format(data2[1], data2[2])+
                                   string+" </identifier>")
                else:
                    self.output.append(self.count*self.inden*" "+"<identifier_{}_{}_used> ".format(data2[1], data2[2])+
                                   string+" </identifier>")
            elif(data):
                if("<classVarDec>" in Dec):
                    self.output.append(self.count*self.inden*" "+"<identifier_{}_{}_defined> ".format(data[1], data[2])+
                                   string+" </identifier>")
                else:
                    self.output.append(self.count*self.inden*" "+"<identifier_{}_{}_used> ".format(data[1], data[2])+
                                   string+" </identifier>")
            elif(data3):
                if("<class>" in Dec or "<subroutineDec>" in Dec):
                    self.output.append(self.count*self.inden*" "+"<identifier_{}_defined> ".format(data3[1])+
                                   string+" </identifier>")
                else:
                    self.output.append(self.count*self.inden*" "+"<identifier_{}_used> ".format(data3[1])+
                                   string+" </identifier>")
            else:
                self.output.append(self.count*self.inden*" "+"<identifier_class_used> "+
                               string+" </identifier>")
                
            self.tknzr.advance(self.token_list[self.tknzr.count:])
            
            
        elif(self.tknzr.classification == "INT_CONST"):
            self.output.append(self.count*self.inden*" "+"<integerConstant> "+
                               string+" </integerConstant>")
            self.tknzr.advance(self.token_list[self.tknzr.count:])
            
        elif(self.tknzr.classification == "STRING_CONST"):
            self.output.append(self.count*self.inden*" "+"<stringConstant> "+
                               string+" </stringConstant>")
            self.tknzr.advance(self.token_list[self.tknzr.count:])
            
    def write(self):
        with open(self.new_data, 'w') as f:
            self.output = [line + "\n" for line in self.output]
            f.writelines(self.output)
        return
        