# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:07:08 2020

@author: QiuGeGe
"""


class SymbolTable():  #hash table
    
    def __init__(self):
        self.size = 20 # 长度为20
        self.slots = [None]*self.size # 生成slots列表，将所有槽（列表值）初始为None
        self.name = [None]*self.size # 生成data列表，将所有槽中数据设置为None，
        self.type = [None]*self.size # 有name, type, kind, cnt
        self.kind = [None]*self.size
        self.cnt = [None]*self.size
        self.num = 0
        # 列表中的值一一对应，如name[1]与type[1]是一对
        
    def hashfunction(self, key): # 查表函数
        return key%self.size # 该函数的输入为值返回为值对应的槽

    def rehash(self,oldhashvalue): # 解决碰撞问题,寻找返回一个新的槽
        """
        No collision problem here.
        """
        return (oldhashvalue+1)%self.size # 将原来的哈希值+1取余，寻找一个新的槽位

    def put(self, name, typ, kind): # 储存函数
        hashvalue = self.hashfunction(self.num) # 先获得槽，槽就是两个列表共用的索引

        if self.slots[hashvalue] == None: # 如果该槽为空则直接存入即可
            self.slots[hashvalue] = self.num # 将slots列表中对应的位置放入用户设置的键
            self.name[hashvalue] = name # 将data列表中对应位置放入用户设置的值
            self.type[hashvalue] = typ
            self.cnt[hashvalue] = self.VarCount(kind)
            self.kind[hashvalue] = kind
            
        else: # 如果该槽不为空,即哈希值相同且，该哈希值对应的键值对已经被占用了，那么分两种情况
            if self.slots[hashvalue] == self.num: # 如果是同一个键
                self.name[hashvalue] = name # 直接将原有的数据覆盖为新数据
                self.type[hashvalue] = typ
                self.cnt[hashvalue] = self.VarCount(kind)
                self.kind[hashvalue] = kind
                
            else: # 如果不是同一个键则开始寻找某一个哈希值（键值对为None）
                self.size += 20
                self.slots.extend([None]*self.size) # 生成slots列表，将所有槽（列表值）初始为None
                self.name.extend([None]*self.size) # 生成data列表，将所有槽中数据设置为None，
                self.type.extend([None]*self.size) # 有name, type, kind, cnt
                self.kind.extend([None]*self.size)
                self.cnt.extend([None]*self.size)
                nextslot = self.hashfunction(self.num)
                
                if self.slots[nextslot] == None: # 如果找到一个空槽则填入
                    self.slots[nextslot]=self.num
                    self.name[nextslot] = name # 将data列表中对应位置放入用户设置的值
                    self.type[nextslot] = typ
                    self.cnt[nextslot] = self.VarCount(kind)
                    self.kind[nextslot] = kind
                
        self.num += 1
        
    def get(self, name):# 输入键寻找值
        index = [i for i, x in enumerate(self.name) if x == name]
        if(index != []):
            inde = index[0]
            data = [self.type[inde], self.kind[inde], self.cnt[inde]]
        else:
            data = None
            
        return data
    
    def VarCount(self, kind):
        index = [i for i, x in enumerate(self.kind) if x == kind]
        return len(index)
        