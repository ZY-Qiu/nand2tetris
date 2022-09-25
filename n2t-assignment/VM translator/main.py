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
    
    if (isdir):
        full_new_file = []
        for i in range(len(data)):
            parser = Parser(data[i], data_name)
            new = parser.parse()
            full_new_file.extend(new)
        writer = CodeWriter(new_data, full_new_file)
        writer.write()
    else:
        parser = Parser(data, data_name)
        full_new_file = parser.parse()
        writer = CodeWriter(new_data, full_new_file)
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




