# -*- coding: utf-8 -*-
"""

@author: Gerardo Cervantes
"""


class Expression():
    
    def __init__(self):
        pass
    
    def set_operator(self, operator):
        self.operator = operator
        
    def set_operand(self, operand):
        self.operand = operand    
        
    #Returns construct if has saved construct
    def get_operator(self):
        try:
            return self.operator
        except NameError:
            return None
        
    #Returns construct if has saved construct
    def get_operand(self):
        try:
            return self.operand
        except NameError:
            return None    
    
        
    
    