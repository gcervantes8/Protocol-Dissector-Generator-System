
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:35:55 2018

@author: Gerardo Cervantes
"""

from Expression import Expression


class DecisionConstruct():
    
    def __init__(self):
        pass
    
    def set_expression(self, expression):
        if issubclass(expression, Expression):
            self.expression = expression
        else:
            self.expression = None
        
    def get_expression(self):
        try:
            return self.expression
        except NameError:
            return None

    def get_logical_operator(self):        
        try:
            return self.logical_operator
        except NameError:
            return None
    
    def set_logical_operator(self, logical_operator):
        if logical_operator in ['And', 'Or', 'Not']:
            self.logical_operator = logical_operator
            
    
        
    
    