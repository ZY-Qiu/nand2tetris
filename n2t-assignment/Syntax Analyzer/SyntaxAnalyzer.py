# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:06:44 2020

@author: QiuGeGe
"""

from CompliationEngine import CompliationEngine
from utils import prepare_data_main

import sys

def SyntaxAnalyzer():
    if len(sys.argv) == 2:
        data, data_name, new_data, isdir = prepare_data_main(sys.argv[1]) #xxx.jack, xxx, xxx.xml
    else:
        print("Missing arugment, you must specify a Jack file or folder to translate.")
        return
    
    if (isdir):
        for i in range(len(data)):
            parser = CompliationEngine(new_data[i], data[i])
            parser.run()
        
    else:
        parser = CompliationEngine(new_data, data)
        parser.run()
        
    return



SyntaxAnalyzer()