#!/usr/bin/env python
# coding: utf-8

# In[1]:


#main
from Parser import Parser
from CodeWriter import CodeWriter

import os
import sys
import glob

def main():
    if len(sys.argv) == 2:
        data, data_name, new_data, isdir = prepare_data(sys.argv[1])
    else:
        print("Missing arugment, you must specify a VM file or folder to translate.")
        return
    
    new = []
    new.append('@256\n')
    new.append('D = A\n')
    new.append('@SP\n')
    new.append('M = D\n')

    new.append('@1500\n')
    new.append('D = A\n')
    new.append('@LCL\n')
    new.append('M = D\n')
    new.append('@1600\n')
    new.append('D = A\n')
    new.append('@ARG\n')
    new.append('M = D\n')
    new.append('@1700\n')
    new.append('D = A\n')
    new.append('@THIS\n')
    new.append('M = D\n')
    new.append('@1800\n')
    new.append('D = A\n')
    new.append('@THAT\n')
    new.append('M = D\n')

    #append: Call Sys.init 0
    #处理栈和内存段
    #保存return address
    new.append(r'//Call Sys.init 0'+'\n')
    new.append('@{}.0$ret.1\n'.format(data_name))
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
    new.append('@0\n')
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
    new.append("@{}.Sys.init\n".format(data_name))
    new.append("0;JMP\n")
    #(returnAddress)
    new.append("({}.0$ret.1)\n".format(data_name))
    
    if (isdir):
        for i in range(len(data)):
            parser = Parser(data[i], data_name)
            new_file = parser.parse()
            new.extend(new_file)  
    else:
        parser = Parser(data, data_name)
        new_file = parser.parse()
        new.extend(new_file)
    
    new.append('(end)\n')
    new.append('@end\n')
    new.append('0;JMP\n')
    writer = CodeWriter(new_data, new)
    writer.write()
        
    return


# In[2]:


def prepare_data(dataset):
    isdir = os.path.isdir(dataset)
    if (isdir):
        data_dir = os.path.join(os.getcwd(), dataset)
        data = glob.glob(os.path.join(data_dir, "*.vm"))
        data_name = os.path.split(dataset)[-1]
        new_data = "%s%s"%(data_name, '.asm')
    else:
        data = os.path.join(os.getcwd(), dataset)
        data_name = os.path.splitext(dataset)[0] #返回元组中的第一个str元素
        new_data = "%s%s"%(data_name, '.asm')
    print("new_data_name:", new_data)
    return data, data_name, new_data, isdir


# In[3]:


if __name__ == '__main__':
    main()


# In[ ]:




