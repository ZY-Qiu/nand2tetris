#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Parser

class Parser():
    
    def __init__(self, data, data_name):
        self.data = data
        self.data_name = data_name
        
    def parse(self):
        new = []
        with open(self.data, 'r') as f:
            lines = f.readlines()
            #print(lines)
            #print("*"*20)
            func_name = 0
            function_name = [0]
            j = 1
            
            for i in range(0, len(lines)):
                #print(lines[i])
                new.append('//' + lines[i])
                #lines[i] = lines[i].rstrip('\n') //split函数已去除所有空格和换行符和制表符
                #parse the line, 在翻译完后添加换行符\n
                cmd = lines[i].split()
                print(cmd)
                print("*"*20)
                
                if (cmd == []):
                    continue
                
                if (cmd[0] == "label"):
                    new.append("({}.{}${})\n".format(self.data_name, function_name[func_name], cmd[1]))
    
                if (cmd[0] == "goto"):
                    new.append("@{}.{}${}\n".format(self.data_name, function_name[func_name], cmd[1]))
                    new.append("0;JMP\n")
            
                if (cmd[0] == "if-goto"):
                    new.append("@SP\n")
                    new.append("M = M-1\n")
                    new.append("A = M\n")
                    new.append("D = M\n")
                    new.append("@{}.{}${}\n".format(self.data_name, function_name[func_name], cmd[1]))
                    new.append("D;JNE\n")

                if (cmd[0] == "function"):
                    #记录当前函数名
                    function_name.append(cmd[1])
                    func_name += 1
                    new.append("({}.{})\n".format(self.data_name, cmd[1]))
                    for a in range(int(cmd[2])):
                        #push 0
                        new.append('@0\n')
                        new.append('D = A\n')
                        new.append('@SP\n')
                        new.append('M = M+1\n')
                        new.append('A = M-1\n')
                        new.append('M = D\n')
                
                if (cmd[0] == "call"):
                    #加一指示参数，并保存
                    j += 1
                    #处理栈和内存段
                    #push return address
                    new.append('@{}.{}$ret.{}\n'.format(self.data_name, function_name[func_name], j))
                    new.append('D = A\n')
                    new.append('@SP\n')
                    new.append('M = M+1\n')
                    new.append('A = M-1\n')
                    new.append('M = D\n')
                    
                    #push LCL
                    new.append('@LCL\n')
                    new.append('D = M\n')
                    new.append('@SP\n')
                    new.append('M = M+1\n')
                    new.append('A = M-1\n')
                    new.append('M = D\n')
                    #push ARG
                    new.append('@ARG\n')
                    new.append('D = M\n')
                    new.append('@SP\n')
                    new.append('M = M+1\n')
                    new.append('A = M-1\n')
                    new.append('M = D\n')
                    #push THIS
                    new.append('@THIS\n')
                    new.append('D = M\n')
                    new.append('@SP\n')
                    new.append('M = M+1\n')
                    new.append('A = M-1\n')
                    new.append('M = D\n')
                    #push THAT
                    new.append('@THAT\n')
                    new.append('D = M\n')
                    new.append('@SP\n')
                    new.append('M = M+1\n')
                    new.append('A = M-1\n')
                    new.append('M = D\n')
                    #ARG = SP-5-nArgs
                    new.append('@5\n')
                    new.append('D = A\n')
                    new.append('@{}\n'.format(int(cmd[2])))
                    new.append('D = D + A\n')
                    new.append('@SP\n')
                    new.append('D = M - D\n')
                    new.append('@ARG\n')
                    new.append('M = D\n')
                    #LCL = SP
                    new.append('@SP\n')
                    new.append('D = M\n')
                    new.append('@LCL\n')
                    new.append('M = D\n')
                    #goto func
                    new.append("@{}.{}\n".format(self.data_name, cmd[1]))
                    new.append("0;JMP\n")
                    #(returnAddress)
                    new.append("({}.{}$ret.{})\n".format(self.data_name, function_name[func_name], j))
    
                if (cmd[0] == "return"):
                    #将返回值push进栈，再goto返回位置
                    #恢复之前储存的状态
                    #endFrame = LCL
                    new.append('@LCL\n')
                    new.append('D = M\n')
                    new.append('@endFrame\n')
                    new.append('M = D\n')
                    #returnAddress = *(endFrame - 5)
                    new.append('@5\n')
                    new.append('D = A\n')
                    new.append('@endFrame\n')
                    new.append('A = M-D\n')
                    new.append('D = M\n')
                    new.append('@retAddr\n')
                    new.append('M = D\n')
                    #*ARG = pop()
                    new.append('@SP\n')
                    new.append('M = M-1\n')
                    new.append('A = M\n')
                    new.append('D = M\n')
                    new.append('@ARG\n')
                    new.append('A = M\n')
                    new.append('M = D\n')
                    #SP = ARG+1
                    new.append('@ARG\n')
                    new.append('D = M+1\n')
                    new.append('@SP\n')
                    new.append('M = D\n')
                    #THAT = *(endFrame - 1)
                    new.append('@endFrame\n')
                    new.append('A = M-1\n')
                    new.append('D = M\n')
                    new.append('@THAT\n')
                    new.append('M = D\n')
                    #THIS = *(endFrame - 2)
                    new.append('@2\n')
                    new.append('D = A\n')
                    new.append('@endFrame\n')
                    new.append('A = M-D\n')
                    new.append('D = M\n')
                    new.append('@THIS\n')
                    new.append('M = D\n')
                    #ARG = *(endFrame - 3)
                    new.append('@3\n')
                    new.append('D = A\n')
                    new.append('@endFrame\n')
                    new.append('A = M-D\n')
                    new.append('D = M\n')
                    new.append('@ARG\n')
                    new.append('M = D\n')
                    #LCL = *(endFrame - 4)
                    new.append('@4\n')
                    new.append('D = A\n')
                    new.append('@endFrame\n')
                    new.append('A = M-D\n')
                    new.append('D = M\n')
                    new.append('@LCL\n')
                    new.append('M = D\n')
                    #goto returnAddress
                    new.append('@retAddr\n')
                    new.append('A = M\n')
                    new.append('0;JMP\n')
                    #for return only in function command
                    #new.append('({}.0$ret.0)\n'.format(self.data_name))
                
                if (cmd[0] == "pop"):
                    if (cmd[1] == "local"): #int(cmd[2])
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@LCL\n')
                        new.append('M = M + D\n')
                        new.append('@SP\n')
                        new.append('M = M-1\n')
                        new.append('A = M\n')
                        new.append('D = M\n')
                        new.append('@LCL\n')
                        new.append('A = M\n')
                        new.append('M = D\n')
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@LCL\n')
                        new.append('M = M - D\n')
                        
                    if (cmd[1] == "argument"):
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@ARG\n')
                        new.append('M = M + D\n')
                        new.append('@SP\n')
                        new.append('M = M-1\n')
                        new.append('A = M\n')
                        new.append('D = M\n')
                        new.append('@ARG\n')
                        new.append('A = M\n')
                        new.append('M = D\n')
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@ARG\n')
                        new.append('M = M - D\n')
                        
                    if (cmd[1] == "this"):
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@THIS\n')
                        new.append('M = M + D\n')
                        new.append('@SP\n')
                        new.append('M = M-1\n')
                        new.append('A = M\n')
                        new.append('D = M\n')
                        new.append('@THIS\n')
                        new.append('A = M\n')
                        new.append('M = D\n')
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@THIS\n')
                        new.append('M = M - D\n')
                        
                    if (cmd[1] == "that"):
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@THAT\n')
                        new.append('M = M + D\n')
                        new.append('@SP\n')
                        new.append('M = M-1\n')
                        new.append('A = M\n')
                        new.append('D = M\n')
                        new.append('@THAT\n')
                        new.append('A = M\n')
                        new.append('M = D\n')
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@THAT\n')
                        new.append('M = M - D\n')
                        
                    if (cmd[1] == "constant"):
                        new.append('//Meaningless command!\n')
                        
                    if (cmd[1] == "static"):
                        new.append('@SP\n')
                        new.append('M = M-1\n')
                        new.append('A = M\n')
                        new.append('D = M\n')
                        new.append('@{}.{}\n'.format(self.data_name, int(cmd[2])))
                        new.append('M = D\n')
                        
                    if (cmd[1] == "pointer"):
                        if (int(cmd[2]) == 0):
                            new.append('@SP\n')
                            new.append('M = M-1\n')
                            new.append('A = M\n')
                            new.append('D = M\n')
                            new.append('@THIS\n')
                            new.append('M = D\n')
                        if (int(cmd[2]) == 1):
                            new.append('@SP\n')
                            new.append('M = M-1\n')
                            new.append('A = M\n')
                            new.append('D = M\n')
                            new.append('@THAT\n')
                            new.append('M = D\n')
                            
                    if (cmd[1] == "temp"):
                        if (int(cmd[2]) > 7):
                            print("//Meaningless parameter!")
                        else:
                            new.append('@5\n')
                            new.append('D = A\n')
                            new.append('@TEMP\n')
                            new.append('M = D\n')
                            new.append('@{}\n'.format(int(cmd[2])))
                            new.append('D = A\n')
                            new.append('@TEMP\n')
                            new.append('M = M + D\n')
                            new.append('@SP\n')
                            new.append('M = M-1\n')
                            new.append('A = M\n')
                            new.append('D = M\n')
                            new.append('@TEMP\n')
                            new.append('A = M\n')
                            new.append('M = D\n')
                        
                    
                elif (cmd[0] == "push"):
                    if (cmd[1] == "local"):
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@LCL\n')
                        new.append('D = M + D\n')
                        new.append('A = D\n')
                        new.append('D = M\n')
                        new.append('@SP\n')
                        new.append('M = M+1\n')
                        new.append('A = M-1\n')
                        new.append('M = D\n')
                        
                    if (cmd[1] == "argument"):
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@ARG\n')
                        new.append('D = M + D\n')
                        new.append('A = D\n')
                        new.append('D = M\n')
                        new.append('@SP\n')
                        new.append('M = M+1\n')
                        new.append('A = M-1\n')
                        new.append('M = D\n')
                        
                    if (cmd[1] == "this"):
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@THIS\n')
                        new.append('D = M + D\n')
                        new.append('A = D\n')
                        new.append('D = M\n')
                        new.append('@SP\n')
                        new.append('M = M+1\n')
                        new.append('A = M-1\n')
                        new.append('M = D\n')
                        
                    if (cmd[1] == "that"):
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@THAT\n')
                        new.append('D = M + D\n')
                        new.append('A = D\n')
                        new.append('D = M\n')
                        new.append('@SP\n')
                        new.append('M = M+1\n')
                        new.append('A = M-1\n')
                        new.append('M = D\n')
                        
                    if (cmd[1] == "constant"):
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@SP\n')
                        new.append('M = M+1\n')
                        new.append('A = M-1\n')
                        new.append('M = D\n')
                        
                    if (cmd[1] == "static"):
                        new.append('@{}.{}\n'.format(self.data_name, int(cmd[2])))
                        new.append('D = M\n')
                        new.append('@SP\n')
                        new.append('M = M+1\n')
                        new.append('A = M-1\n')
                        new.append('M = D\n')
                        
                    if (cmd[1] == "pointer"):
                        if (int(cmd[2]) == 0):
                            new.append('@THIS\n')
                            new.append('D = M\n')
                            new.append('@SP\n')
                            new.append('M = M+1\n')
                            new.append('A = M-1\n')
                            new.append('M = D\n')
                        if (int(cmd[2]) == 1):
                            new.append('@THAT\n')
                            new.append('D = M\n')
                            new.append('@SP\n')
                            new.append('M = M+1\n')
                            new.append('A = M-1\n')
                            new.append('M = D\n')
                        
                    if (cmd[1] == "temp"):
                        new.append('@{}\n'.format(int(cmd[2])))
                        new.append('D = A\n')
                        new.append('@5\n')
                        new.append('A = A + D\n')
                        new.append('D = M\n')
                        new.append('@SP\n')
                        new.append('M = M+1\n')
                        new.append('A = M-1\n')
                        new.append('M = D\n')
                        
                elif (cmd[0] == "add"):
                    new.append('@SP\n')
                    new.append('M = M-1\n')
                    new.append('A = M\n')
                    new.append('D = M\n')
                    new.append('A = A-1\n')
                    new.append('M = D+M\n')
                    
                elif (cmd[0] == "neg"):
                    new.append('@SP\n')
                    new.append('A = M-1\n')
                    new.append('M = -M\n')
                    
                elif (cmd[0] == "sub"):
                    new.append('@SP\n')
                    new.append('M = M-1\n')
                    new.append('A = M\n')
                    new.append('D = M\n')
                    new.append('A = A-1\n')
                    new.append('M = M-D\n')
                    
                elif (cmd[0] == "lt"):
                    new.append('@SP\n')
                    new.append('M = M-1\n')
                    new.append('A = M\n')
                    new.append('D = M\n')
                    new.append('A = A-1\n')
                    new.append('D = M-D\n')
                    new.append('@lt{}\n'.format(i))
                    new.append('D;JLT\n')
                    new.append('@SP\n')
                    new.append('A = M-1\n')
                    new.append('M = 0\n')
                    new.append('@continue{}\n'.format(i))
                    new.append('0;JMP\n')
                    new.append('(lt{})\n'.format(i))
                    new.append('@SP\n')
                    new.append('A = M-1\n')
                    new.append('M = 1\n')
                    new.append('(continue{})\n'.format(i))
                    
                elif (cmd[0] == "eq"):
                    new.append('@SP\n')
                    new.append('M = M-1\n')
                    new.append('A = M\n')
                    new.append('D = M\n')
                    new.append('A = A-1\n')
                    new.append('D = M-D\n')
                    new.append('@eq{}\n'.format(i))
                    new.append('D;JEQ\n')
                    new.append('@SP\n')
                    new.append('A = M-1\n')
                    new.append('M = 0\n')
                    new.append('@continue{}\n'.format(i))
                    new.append('0;JMP\n')
                    new.append('(eq{})\n'.format(i))
                    new.append('@SP\n')
                    new.append('A = M-1\n')
                    new.append('M = 1\n')
                    new.append('(continue{})\n'.format(i))
                    
                elif (cmd[0] == "gt"):
                    new.append('@SP\n')
                    new.append('M = M-1\n')
                    new.append('A = M\n')
                    new.append('D = M\n')
                    new.append('A = A-1\n')
                    new.append('D = M-D\n')
                    new.append('@gt{}\n'.format(i))
                    new.append('D;JGT\n')
                    new.append('@SP\n')
                    new.append('A = M-1\n')
                    new.append('M = 0\n')
                    new.append('@continue{}\n'.format(i))
                    new.append('0;JMP\n')
                    new.append('(gt{})\n'.format(i))
                    new.append('@SP\n')
                    new.append('A = M-1\n')
                    new.append('M = 1\n')
                    new.append('(continue{})\n'.format(i))
                    
                elif (cmd[0] == "and"):
                    new.append('@SP\n')
                    new.append('M = M-1\n')
                    new.append('A = M\n')
                    new.append('D = M\n')
                    new.append('A = A-1\n')
                    new.append('M = M&D\n')
                    
                elif (cmd[0] == "or"):
                    new.append('@SP\n')
                    new.append('M = M-1\n')
                    new.append('A = M\n')
                    new.append('D = M\n')
                    new.append('A = A-1\n')
                    new.append('M = M|D\n')
                    
                elif (cmd[0] == "not"):
                    new.append('@SP\n')
                    new.append('A = M-1\n')
                    new.append('M = !M\n')
                
        return new
       

