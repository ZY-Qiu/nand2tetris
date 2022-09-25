# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:22:00 2020

@author: QiuGeGe
"""
#没有#define欸


class JackTokenizer():
    """
    传入原始文件创建对象，先运行prepare_data函数得返回值new，再以hasMoreTokens返回
    值为条件运行advance(new)函数，以此改变实例属性。
    """
    
    Keyword = ["class", "constructor", "function", "method", "field",
           "static", "var", "int", "char", "boolean", "void", 
           "true", "false", "null", "this", "let", "do", "if", 
           "else", "while", "return"]
    Symbol = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', 
          '*', '/', '&', '|', '<', '>', '=', '~']

    def __init__(self):
        self.count = 0
        self.classification = 0
        self.token = 0
    
    def hasMoreTokens(self, new):
        if (self.count < len(new)):
            return True
        else:
            return False
    
    def advance(self, char_list):  #可以pass in new[self.count:]吗?
        """
        将字符组成有意义的词，并找出其性质，计数加一
        遇到字母开头，append直到遇到symbol，检查是否与keyword相符，以确定其是identifier还是keyword
        """
        accmu_char = []
        if (char_list[0].isdigit()):
            for i in char_list[0:]:
                if (i.isdigit()):
                    accmu_char.append(i)
                    self.count += 1     #会影响for循环中的count吗？
                else:
                    self.classification = "INT_CONST"
                    self.token = ''.join(accmu_char)
                    break
            return
        
        if (char_list[0].isalpha()):
            for i in char_list[0:]:
                if (len(i) != 1):
                    accmu_char.append(i)
                    self.count += 1
                    if (accmu_char[0] in self.Keyword):
                        self.classification = "KEYWORD"
                        self.token = ''.join(accmu_char)
                        break
                    else:
                        self.classification = "IDENTIFIER"
                        self.token = ''.join(accmu_char)
                        break
                elif (i.isalpha() or i.isdigit()):
                    accmu_char.append(i);
                    self.count += 1     #会影响for循环中的count吗？
                elif(''.join(accmu_char) in self.Keyword):
                    self.classification = "KEYWORD"
                    self.token = ''.join(accmu_char)
                    break
                else:
                    self.classification = "IDENTIFIER"
                    self.token = ''.join(accmu_char)
                    break
            return
        
        if (char_list[0] in self.Symbol):
            accmu_char.append(char_list[0])
            self.count += 1     #会影响for循环中的count吗？
            self.classification = "SYMBOL"
            self.token = ''.join(accmu_char)
            return
        
        if (char_list[0] == '"'):
            self.count += 3
            self.classification = "STRING_CONST"
            self.token = char_list[1]  
            return
    
    def tokenType(self):
        pass
    
    def keyword(self):
        pass
    
    def symbol(self):
        pass
    
    def indentifier(self):
        pass
    
    def intVal(self):
        pass
    
    def stringVal(self):
        pass
    