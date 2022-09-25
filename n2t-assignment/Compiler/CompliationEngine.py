# -*- coding: utf-8 -*-
"""
Crself.eated on Sat Oct 31 19:26:58 2020

@author: QiuGeGe
"""

from Tokenizer import JackTokenizer
from SymbolTable import SymbolTable
from utils import prepare_data
from VMWriter import VMWriter

class CompliationEngine():
    def __init__(self, new_data, data, symtab):
        self.new_data = new_data
        self.data = data
        self.tknzr = JackTokenizer()
        self.vmw = VMWriter(self.new_data)
        self.ClassTable = SymbolTable()
        self.SubroutineTable = SymbolTable()
        self.MethodTable = symtab
        self.token_list = 0
        self.classname = ""
        self.subroutinename = ""
        self.localnum = 0
        self.ifnum = -1
        self.whilenum = -1
        self.expnum = 0
        self.subroutinekind = ""
    
    def run(self):
        self.token_list = prepare_data(self.data)
        print("Data prepare complete!")
        self.tknzr.advance(self.token_list[self.tknzr.count:])
        print("Advance! Go compile class!")
        self.CompileClass()
        # 可以两次编译，目的是在第一次更新所有的subroutine定义
        self.vmw.close()
        print("Complete!")
        print("."*80)
        return
    
    def CompileClass(self):
       
        self.eat("class")  # class
        self.classname = self.tknzr.token
        self.advance()  # main...
        
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
    
    def CompileClassVarDec(self):

        if(self.tknzr.token == "static"):
            kind = self.tknzr.token
            self.eat(self.tknzr.token)  #field = this! or static
            typ = self.tknzr.token
            self.advance()  #int, bolean, char or class type var
            self.ClassTable.put(self.tknzr.token, typ, kind)
            self.advance()  #x...
            
        elif(self.tknzr.token == "field"):
            kind = "this"
            self.eat(self.tknzr.token)  #field = this! or static
            typ = self.tknzr.token
            self.advance()  #int, bolean, char or class type var
            self.ClassTable.put(self.tknzr.token, typ, kind)
            self.advance()  #x...
        
        while (self.tknzr.token == ","):
            self.eat(",")
            self.ClassTable.put(self.tknzr.token, typ, kind)
            self.advance()  #y...
        self.eat(";")
        
    def CompileSubroutineDec(self):
        
        self.SubroutineTable = SymbolTable()
        
        self.subroutinekind = self.tknzr.token  # constructor, function, method
        if(self.subroutinekind == "method"):
            kind = "method"
            self.advance()
            typ = self.tknzr.token
            self.advance()  #int, bolean, char or class type var
            self.MethodTable.put(self.tknzr.token, typ, kind)
        else:
            self.advance()
            self.advance()

        self.subroutinename = self.tknzr.token
        
        self.advance()  # main...
        
        self.eat("(")
        print("Advance! Go compile ParameterList!")
        self.CompileParameterList()
        self.eat(")")
        print("Advance! Go compile SubroutineBody!")
        self.CompileSubroutineBody()
    
    def CompileParameterList(self):

        if(self.subroutinekind == "method"): # 使用do subroutinename()无法判断？
            kind = "argument"
            typ = self.classname
            name = "this"
            self.SubroutineTable.put(name, typ, kind)
            print(self.SubroutineTable.name)
            print(self.MethodTable.name)
        if(self.tknzr.token != ")"):
            kind = "argument"
            typ = self.tknzr.token
            self.advance()  # int, bolean, char or class type var
            name = self.tknzr.token
            self.SubroutineTable.put(name, typ, kind)
            self.advance()  # x...
            
            while(self.tknzr.token == ","):
                self.eat(",")
                typ = self.tknzr.token
                self.advance()
                name = self.tknzr.token
                self.SubroutineTable.put(name, typ, kind)
                self.advance()

    def CompileSubroutineBody(self):

        self.localnum = 0
        self.eat("{")
        while(self.tknzr.token == "var"):
            print("Advance! Go compile VarDec!")
            self.CompileVarDec()
            
        self.vmw.writeFunction("{}.{}".format(self.classname, self.subroutinename), 
                               self.localnum)
        if(self.subroutinekind == "constructor"):
            self.vmw.writePush("constant", self.ClassTable.VarCount("this"))
            self.vmw.writeCall("Memory.alloc", 1)
            self.vmw.writePop("pointer", 0)
            
        elif(self.subroutinekind == "method"):
            self.vmw.writePush("argument", 0)
            self.vmw.writePop("pointer", 0)
            
        print("Advance! Go compile Statements!")
        self.CompileStatements()
        self.eat("}")
    
    def CompileVarDec(self):

        kind = "local"
        self.eat("var")  # var
        typ = self.tknzr.token
        self.advance()  # int, bolean, char or class type var
        name = self.tknzr.token
        self.SubroutineTable.put(name, typ, kind)
        self.advance()  # x...
        self.localnum += 1
        
        while(self.tknzr.token == ","):
            self.eat(",")
            self.SubroutineTable.put(self.tknzr.token, typ, kind)
            self.advance() #varName
            self.localnum += 1
        self.eat(";")
        
    def CompileStatements(self):

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
                print("The current token:", self.tknzr.token)
                raise Exception("No string matches the requirments!")
        
    def CompileLet(self):

        self.eat("let") # let x = expression
        #print(self.tknzr.token)
        [temp, seg, num] = self.eat(self.tknzr.token)
        
        if (self.tknzr.token == "["):
            
            self.vmw.writePush(seg, num)
            self.eat("[")
            print("Advance! Go compile Expression!")
            self.CompileExpression()
            self.eat("]")
            self.vmw.writeArithmetic("+")
            self.eat("=")
            print("Advance! Go compile Expression!")
            self.CompileExpression()
            
            self.vmw.writePop("temp", 0)
            self.vmw.writePop("pointer", 1)
            self.vmw.writePush("temp", 0)
            self.vmw.writePop("that", 0)
            self.eat(";")
        else:
            self.eat("=")
            print("Advance! Go compile Expression!")
            self.CompileExpression()
            self.vmw.writePop(seg, num)
            self.eat(";")
            
    def CompileIf(self):

        self.ifnum += 1
        localifnum = self.ifnum
        self.eat("if")
        self.eat("(")
        print("Advance! Go compile Expression!")
        self.CompileExpression()
        self.eat(")")
        self.vmw.writeArithmetic("~")
        self.vmw.writeIf("{}.else.{}".format(self.classname, localifnum))
        
        self.eat("{")
        print("Advance! Go compile Statements!")
        self.CompileStatements()
        self.eat("}")
        self.vmw.writeGoto("{}.ifend.{}".format(self.classname, localifnum))
        
        self.vmw.writeLabel("{}.else.{}".format(self.classname, localifnum))
        if (self.tknzr.token == "else"):
            self.eat("else")
            self.eat("{")
            print("Advance! Go compile Statements!")
            self.CompileStatements()
            self.eat("}")
        self.vmw.writeLabel("{}.ifend.{}".format(self.classname, localifnum))
        
    def CompileWhile(self):

        self.whilenum += 1
        localwhilenum = self.whilenum
        self.eat("while")
        self.vmw.writeLabel("{}.while.{}".format(self.classname, localwhilenum))
        self.eat("(")
        print("Advance! Go compile Expression!")
        self.CompileExpression()
        self.eat(")")
        self.vmw.writeArithmetic("~")
        self.vmw.writeIf("{}.whileend.{}".format(self.classname, localwhilenum))
        
        self.eat("{")
        print("Advance! Go compile Statements!")
        self.CompileStatements()
        self.eat("}")
        self.vmw.writeGoto("{}.while.{}".format(self.classname, localwhilenum))
        
        self.vmw.writeLabel("{}.whileend.{}".format(self.classname, localwhilenum))
    
    def CompileDo(self):
        self.eat("do")
        data = self.eat(self.tknzr.token)
        if(self.tknzr.token == "("): #subroutinName(expressionList)
            if(len(data) == 2):
                self.vmw.writePush("pointer", 0)
            self.eat("(")
            print("Advance! Go compile ExpressionList!")
            self.CompileExpressionList()
            if(len(data) == 2):
                expnum = self.expnum + 1
            else:
                expnum = self.expnum
            self.eat(")")
            self.vmw.writeCall("{}.{}".format(self.classname, data[0]), expnum)
            
        elif(self.tknzr.token == "."): #varName|className.subroutinName(expressionList)
            self.eat(".")
            name = self.tknzr.token
            self.advance()  # subroutine name
            if(len(data) == 3): # varName.subroutinName(expressionList)
                self.vmw.writePush(data[1], data[2])
                self.eat("(")
                print("Advance! Go compile ExpressionList!")
                self.CompileExpressionList()
                self.eat(")")
                print(self.expnum)
                self.vmw.writeCall("{}.{}".format(data[0], name), self.expnum+1)
            else: # className.subroutinName(expressionList)
                self.eat("(")
                print("Advance! Go compile ExpressionList!")
                self.CompileExpressionList()
                self.eat(")")
                print(self.expnum)
                self.vmw.writeCall("{}.{}".format(data[0], name), self.expnum)
        self.vmw.writePop("temp", 0)
        self.eat(";")

    
    def CompileReturn(self):

        self.eat("return")
        if (self.tknzr.token != ";"):
            print("Advance! Go compile Expression!")
            self.CompileExpression()
        else:
            self.vmw.writePush("constant", 0)
        self.vmw.writeReturn()
        self.eat(";")

    
    def CompileExpression(self):

        print("Advance! Go compile Term!")
        self.CompileTerm()
        if (self.tknzr.classification == "SYMBOL"):
            while (self.tknzr.token != "]" and self.tknzr.token != ")" and 
                   self.tknzr.token != ";" and self.tknzr.token != ","):
                op = self.tknzr.token
                self.eat(self.tknzr.token)
                print("Advance! Go compile Term!")
                self.CompileTerm()
                self.vmw.writeArithmetic(op)
                
    def CompileExpressionList(self):

        expnum = 0
        if (self.tknzr.token != ")"):
            print("Advance! Go compile Expression!")
            self.CompileExpression()
            expnum += 1
            while (self.tknzr.token == ","):
                self.eat(",")
                print("Advance! Go compile Expression!")
                self.CompileExpression()
                expnum += 1
        self.expnum = expnum
        print("self.expnum in CompileExpressionList", self.expnum)

    def CompileTerm(self):

        if(self.tknzr.classification == "INT_CONST"):
            [temp, seg, num] = self.eat(self.tknzr.token)
            self.vmw.writePush(seg, num)
            
        elif(self.tknzr.classification == "STRING_CONST"):
            """
            x = String.new(str_len)
            for char in string:
                x.appendChar(char)
            """
            self.vmw.writePush("constant", len(self.tknzr.token))
            self.vmw.writeCall("String.new", 1)

            for char in self.tknzr.token:
                self.vmw.writePush("constant", ord(char))
                self.vmw.writeCall("String.appendChar", 2)
            
            self.advance()
            
        elif(self.tknzr.classification == "KEYWORD"):
            if(self.tknzr.token == "true"):
                self.vmw.writePush("constant", 1)
                self.vmw.writeArithmetic("neg")
            if(self.tknzr.token == "false"):
                self.vmw.writePush("constant", 0)
            if(self.tknzr.token == "null"):
                self.vmw.writePush("constant", 0)
            if(self.tknzr.token == "this"):
                self.vmw.writePush("pointer", 0)
            self.advance()
            
        elif (self.tknzr.classification == "SYMBOL"): # (expression)
            if (self.tknzr.token == "("):
                self.eat("(")
                self.CompileExpression()
                self.eat(")")
            elif(self.tknzr.token == "-" or self.tknzr.token == "~"):           #
                unaryop = self.tknzr.token
                self.eat(self.tknzr.token)
                self.CompileTerm()
                if(unaryop == "-"):
                    self.vmw.writeArithmetic("neg")
                if(unaryop == "~"):
                    self.vmw.writeArithmetic("~")
                    
        elif(self.tknzr.classification == "IDENTIFIER"):
            data = self.eat(self.tknzr.token)
            
            if(self.tknzr.token == "["): # varName[expression]
                self.vmw.writePush(data[1], data[2])
                self.eat("[")
                self.CompileExpression()
                self.eat("]")
                self.vmw.writeArithmetic("+")
                self.vmw.writePop("pointer", 1)
                self.vmw.writePush("that", 0)
            elif(self.tknzr.token == "("): # subroutinName(expressionList)
                if(len(data) == 2):
                    self.vmw.writePush("pointer", 0)
                self.eat("(")
                self.CompileExpressionList()
                if(len(data) == 2):
                    expnum = self.expnum + 1
                else:
                    expnum = self.expnum
                self.eat(")")
                self.vmw.writeCall("{}.{}".format(self.classname, data[0]), expnum)
            elif(self.tknzr.token == "."): # varName|className.subroutinName(expressionList)
                self.eat(".")
                name = self.eat(self.tknzr.token)  # subroutine name
                if(len(data) == 3): 
                    # push the base address of the object on the stack as the firsr argument
                    self.vmw.writePush(data[1], data[2])
                    self.eat("(")
                    print("Advance! Go compile ExpressionList!")
                    self.CompileExpressionList()
                    self.eat(")")
                    self.vmw.writeCall("{}.{}".format(data[0], name[0]), self.expnum+1)

                else:
                    self.eat("(")
                    print("Advance! Go compile ExpressionList!")
                    self.CompileExpressionList()
                    self.eat(")")
                    self.vmw.writeCall("{}.{}".format(data[0], name[0]), self.expnum)

            else: # varName only
                #print(data)
                self.vmw.writePush(data[1], data[2])
                
    def eat(self, string):
        if (self.tknzr.token != string):
            print("Supposed:", string)
            print("Actual:", self.tknzr.token)
            raise Exception("Strings do not match!")
            
        elif(self.tknzr.classification == "IDENTIFIER"):
            
            name = self.tknzr.token
            data = self.ClassTable.get(name)
            data2 = self.SubroutineTable.get(name)
            data3 = self.MethodTable.get(name)
            self.tknzr.advance(self.token_list[self.tknzr.count:])

            if(data2):
                return data2
            
            elif(data):
                return data
            
            elif(data3):
                return [name, 2]
            
            else:
                return [name]
            
        elif(self.tknzr.classification == "INT_CONST"):
            name = self.tknzr.token
            self.tknzr.advance(self.token_list[self.tknzr.count:])
            return [None, "constant", name]

        else:
            if(self.tknzr.hasMoreTokens(self.token_list)):
                self.tknzr.advance(self.token_list[self.tknzr.count:])
                return None
            else:
                return
        
    def advance(self):
        self.tknzr.advance(self.token_list[self.tknzr.count:])
