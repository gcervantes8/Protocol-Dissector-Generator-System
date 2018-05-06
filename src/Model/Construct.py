# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:14:22 2018

@author: Gerardo Cervantes
"""

__metaclass__ = type
#Has a reference to next Constructs (or subclasses)
class Construct():
    
    
    def __init__(self):
        self.isConstruct = True
    
    def set_next_constructs(self, next_constructs):
        
        if type(next_constructs) is list:
                for construct in next_constructs:
                    try:
                        if not construct.isConstruct:
                            return
                    except AttributeError:
                        continue;
                
        self.next = next_constructs
        
    #Returns construct if has saved construct
    def get_next_constructs(self):
        try:
            next_constructs = self.next
            return next_constructs
        
        except AttributeError:
            pass            
        return []
    
    
        
    
    