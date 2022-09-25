#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#CodeWriter

class CodeWriter():
    
    def __init__(self, new_data, new):
        self.new_data = new_data
        self.new = new
        
    def write(self):
        with open(self.new_data, 'w') as f:
            f.writelines(self.new)
        return

