# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:14:22 2018

@author: Gerardo Cervantes
"""

#Has a reference to next Constructs (or subclasses)
class Construct():
    
    def __init__(self, next_constructs):
        self.set_next_constructs(next_constructs)
    
    def set_next_constructs(self, next_constructs):
        
        if type(next_constructs) is list:
                for construct in next_constructs:
                    if not issubclass(type(next_constructs), Construct):
                        return
                
        self.next = next_constructs
        
    #Returns construct if has saved construct
    def get_next_constructs(self):
        try:
            next_constructs = self.next
            return next_constructs
        
        except NameError:
            pass            
        return None
        
    
    