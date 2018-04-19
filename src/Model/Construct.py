# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:14:22 2018

@author: Gerardo Cervantes
"""

#Has a reference to another Construct (or subclasses)
class Construct():
    
    def __init__(self, next_construct):
        self.set_next_construct(next_construct)
    
    def set_next_construct(self, next_construct):
        self.next = next_construct
        
    #Returns construct if has saved construct
    def get_next_construct(self):
        try:
            next_construct = self.next
            if issubclass(next_construct, Construct):
                return next_construct
        except NameError:
            pass            
        return None
        
    
    