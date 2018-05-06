# -*- coding: utf-8 -*-
"""

@author: Gerardo Cervantes
"""


class Expression():
    
    def __init__(self):
        pass
    
    def set_relational_operators(self, operators):
        if type(operators) is list:
                for op in operators:
                    if not issubclass(type(op), str):
                        self.operators = None
                        return
        self.operators = operators
        
    #Returns construct if has saved construct
    def get_relational_operators(self):
        try:
            return self.operators
        except NameError:
            return None
        
    #Returns construct if has saved construct
    def get_operands(self):
        try:
            return self.operands
        except NameError:
            return None    

    def set_operands(self, operands):
        
        if type(operands) is list:
            for op in operands:
                if not issubclass(type(op), str):
                    self.operands = None
                    return
        self.operands = operands
        
    def get_logical_operators(self):        
        try:
            return self.logical_operators
        except NameError:
            return None
    
    def set_logical_operators(self, logical_operators):
        if type(logical_operators) is list:
            for op in logical_operators:
                if not op in ['And', 'Or', 'Not']:
                    self.logical_operators = None
                    return
        self.logical_operators = logical_operators
            
    
        
    
    