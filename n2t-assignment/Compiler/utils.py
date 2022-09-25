# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:07:41 2020

@author: QiuGeGe
"""

import os
import glob

Keyword = ["class", "constructor", "function", "method", "field",
           "static", "var", "int", "char", "boolean", "void", 
           "true", "false", "null", "this", "let", "do", "if", 
           "else", "while", "return"]

def prepare_data(data):
    """
    先去除备注，再去除空格和换行符制，最后分解为一个个字符
    """
    new = []
    with open(data, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            
            #print(lines[i])
            # Precess annotation.
            if (lines[i][0] == "/"):
                continue
            elif ('/**' in lines[i] or '*/' in lines[i]):
                continue
            elif(lines[i].strip() == "" or lines[i].strip()[0] == "*"): # 考虑or的优先级问题
                continue
            elif ('//' in lines[i]):
                index_2 = lines[i].index("//")
                line = lines[i][:index_2]
                #print([line])
            else:
                line = lines[i]
            #print(lines[i])
            #print("ori_line:", [line])
            # Split the whole string by ", ( and )
            line = process_str_char(line, '"')
            #print("line", line)
            fir_lst = []
            sec_lst = []
            for j in line:   
                fir_lst.extend(process_str_char(j, "("))
            #print("fir_lst", fir_lst)
            for k in fir_lst:
                sec_lst.extend(process_str_char(k, ")"))
            #print("sec_lst", sec_lst)
            #print("."*80)
            # Join the element within "" and process the string
            count = 0
            str_list = []
            for l in sec_lst:
                if (count == 0):
                    if (l == '"'):
                        count += 1
                        new.append('"')
                        continue
                    else:
                        new.extend(process(l))
                if (count == 1):
                    if (l == '"'):
                        count -= 1
                        new.append("".join(str_list))
                        new.append('"')
                        str_list = []
                    else:
                        str_list.append(l)
    print(new)
    #print("."*80)
    return new

def prepare_data_main(dataset):
    isdir = os.path.isdir(dataset)
    if (isdir):
        data_dir = os.path.join(os.getcwd(), dataset)
        data = glob.glob(os.path.join(data_dir, "*.jack"))
        new_data = []
        for i in data:
            file_name = os.path.split(i)[-1]
            data_name = os.path.splitext(file_name)[0]
            new_data_one = os.path.join(data_dir, "%s%s"%(data_name, '.vm'))
            new_data.append(new_data_one)
    else:
        data = os.path.join(os.getcwd(), dataset)
        data_name = os.path.splitext(dataset)[0] #返回元组中的第一个str元素
        new_data = "%s%s"%(data_name, '.vm')
    print("new_data_name:", new_data)
    return data, data_name, new_data, isdir

def process_string_bracket(lst, stri, str1): #line, ", 
    """
    process string than bracket outside of string
    
    Deprecated!
    """
    
    if (stri == str1):
        new = []
        index = [i for i, x in enumerate(lst) if x == '{}'.format(stri)]
        index.append(-1)
        for i in range(int((len(index)-1)/2)):
            first = lst[index[i*2-1]+1:index[i*2]]
            new.extend(process(first))
            new.extend('{}'.format(stri))
            new.append(lst[index[i*2]+1:index[i*2+1]])
            new.extend('{}'.format(stri))
        last = lst[index[-2]+1:]
        new.extend(process(last))
        
        return new
    else:
        new = []
        index1 = [i for i, x in enumerate(lst) if x == '{}'.format(stri)]
        index2 = [i for i, x in enumerate(lst) if x == '{}'.format(str1)]
        index2.append(-1)
        #print("index2:", len(index2))
        for i in range(len(index1)):
            first = lst[index2[i-1]+1:index1[i]]
            #print("first", first)
            new.extend(process(first))
            new.extend('{}'.format(stri))
            mid = lst[index1[i]+1:index2[i]]
            #print("mid:", mid)
            new.extend(process(mid))
            new.extend('{}'.format(str1))
        #print("lst", lst)
        last = lst[index2[-2]+1:]
        new.extend(process(last))
        #print("new in psb", new)
        #print("*"*80)
        return new

def process_str_char(lst, char):
    """
    'abcd ef"g hij k' => ['abcd ef', '"', 'g hij k']
    """
    sep_lst = list(lst)
    new_lst = []
    new = []
    for i in sep_lst:
        if (i != char):
            new_lst.append(i)
        else:
            temp = "".join(new_lst)
            new.append(temp)
            new.append(char)
            new_lst = []
    new.append("".join(new_lst))
    return new
    
def process(lst):
    new = []
    if (lst != []):
        cmd1 = lst.split()
        for j in cmd1:
            if (j.isalpha()):
                new.append(j)
            else:
                new.extend(j)
    #print("new in p", new)
    return new