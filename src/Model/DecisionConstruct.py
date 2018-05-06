
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:35:55 2018

@author: Gerardo Cervantes
"""

from Expression import Expression


class DecisionConstruct():
    
    def __init__(self):
        pass
        
    def set_expressions(self, expressions):
        
        if type(expressions) is list:
                for exp in expressions:
                    if not issubclass(type(exp), Expression):
                        self.expressions = None
                        return
        self.expressions = expressions
        
    def get_expressions(self):
        try:
            return self.expressions
        except NameError:
            return None


            
    
        
    
    