# -*- coding: utf-8 -*-
"""
Crself.eated on Sat Oct 31 19:26:58 2020

@author: QiuGeGe
"""

from Tokenizer import JackTokenizer
from utils import prepare_data

class CompliationEngine():
    def __init__(self, new_data, data):
        self.new_data = new_data
        self.data = data
        self.tknzr = JackTokenizer()
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
        self.write()
        print("Complete!")
        print("."*80)
        return
    
    def CompileClass(self):
        self.output.append(self.count*self.inden*" "+"<class>")
        self.count += 1
        self.eat("class")
        self.eat(self.tknzr.token)
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
        self.eat(self.tknzr.token)  #field or static
        self.eat(self.tknzr.token)  #int, or class type var
        self.eat(self.tknzr.token)  #x...
        while (self.tknzr.token == ","):
            self.eat(",")
            self.eat(self.tknzr.token)  #y...
        self.eat(";")
        self.count -= 1
        self.output.append(self.count*self.inden*" "+"</classVarDec>")
    
    def CompileSubroutineDec(self):
        self.output.append(self.count*self.inden*" "+"<subroutineDec>")
        self.count += 1
        self.eat(self.tknzr.token) #constructor, function, method
        self.eat(self.tknzr.token) #type
        self.eat(self.tknzr.token) #subroutine name
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
            self.eat(self.tknzr.token)
            self.eat(self.tknzr.token)
            while(self.tknzr.token == ","):
                self.eat(",")
                self.eat(self.tknzr.token)
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
        self.eat("var")
        self.eat(self.tknzr.token) #type
        self.eat(self.tknzr.token) #varName
        while(self.tknzr.token == ","):
            self.eat(",")
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
            self.eat(self.tknzr.token)
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
                self.eat(self.tknzr.token)
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
            self.output.append(self.count*self.inden*" "+"<identifier> "+
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
        