# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:12:15 2020

@author: QiuGeGe
"""


class VMWriter():
    
    def __init__(self, new_data):
        self.output = open(new_data, 'w')
    
    def writePush(self, seg, num):
        self.output.write("push {} {}".format(seg, num)+"\n")
    
    def writePop(self, seg, num):
        self.output.write("pop {} {}".format(seg, num)+"\n")
    
    def writeArithmetic(self, command):
        #add, sub, neg, eq, gt, lt, and, or, not
        if(command == "+"):
            self.output.write("add"+"\n")
        if(command == "-"):
            self.output.write("sub"+"\n")
        if(command == "neg"):
            self.output.write("neg"+"\n")
        if(command == "="):
            self.output.write("eq"+"\n")
        if(command == ">"):
            self.output.write("gt"+"\n")
        if(command == "<"):
            self.output.write("lt"+"\n")
        if(command == "&"):
            self.output.write("and"+"\n")
        if(command == "|"):
            self.output.write("or"+"\n")
        if(command == "~"):
            self.output.write("not"+"\n")
        if(command == "*"):
            self.output.write("call Math.multiply 2"+"\n")
        if(command == "/"):
            self.output.write("call Math.divide 2"+"\n")
    
    def writeLabel(self, label):
        self.output.write("label {}".format(label)+"\n")
    
    def writeGoto(self, label):
        self.output.write("goto {}".format(label)+"\n")
    
    def writeIf(self, label):
        self.output.write("if-goto {}".format(label)+"\n")
    
    def writeCall(self, funcName, nArgs):
        self.output.write("call {} {}".format(funcName, nArgs)+"\n")
    
    def writeFunction(self, funcName, nLocals):
        self.output.write("function {} {}".format(funcName, nLocals)+"\n")
    
    def writeReturn(self):
        self.output.write("return\n")
    
    def close(self):
        self.output.close()