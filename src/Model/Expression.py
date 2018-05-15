# -*- coding: utf-8 -*-
"""

@author: Gerardo Cervantes
"""


class Expression():
    
    def __init__(self):
        self.isExpression = True
    
    def set_relational_operators(self, relational_operators):
        if type(relational_operators) is list:
                for op in relational_operators:
                    if not issubclass(type(op), str):
                        self.relational_operators = None
                        return
        self.relational_operators = relational_operators
        print('set relational ops')
        print(relational_operators)
        
    def set_relational_operators_and_operands(self, relational_operators, operands):
        self.set_relational_operators(relational_operators)
        self.set_operands(operands)
        
    #Returns construct if has saved construct
    def get_relational_operators(self):
        try:
            return self.relational_operators
        except AttributeError:
            return None

    def set_operands(self, operands):
        
        if type(operands) is list:
            for op in operands:
                if not issubclass(type(op), str):
                    self.operands = None
                    return
        self.operands = operands
        
    #Returns construct if has saved construct
    def get_operands(self):
        try:
            return self.operands
        except AttributeError:
            return None    

    def set_logical_operators(self, logical_operators):
        if type(logical_operators) is list:
            for op in logical_operators:
                if not op in ['And', 'Or', 'Not']:
                    self.logical_operators = None
                    return
                
        lower_case_logical_ops = []
        for op in logical_operators:
            lower_case_logical_ops.append(op.lower())
        self.logical_operators = lower_case_logical_ops
        
    def get_logical_operators(self):        
        try:
            return self.logical_operators
        except AttributeError:
            return None        
        
    #Used for dictionary of objects in protocol
    def __hash__(self):
        return hash(self.get_operands, self.get_logical_operators(), self.get_relational_operators())
            
    #Used for dictionary of objects in protocol
    def __eq__(self, other):
        
        l_op = self.get_logical_operators()
        op = self.get_operands()
        r_op = self.get_relational_operators()
        try:
            other_l_op = other.get_logical_operators()
            has_logical_operators = True
        except AttributeError:
            has_logical_operators = False
        
        try:
            other_r_op = other.get_relational_operators()
            has_relational_operators = True
        except AttributeError:
            has_relational_operators = False
            
        try:
            other_op = other.get_logical_operands()
            has_operands = True
        except AttributeError:
            has_operands = False
            
        if has_operands and op != None:
            if op != other_op:
                return False
        else:
            #If different return false
            if not has_operands and op != None:
                return False
            
        if has_logical_operators and l_op != None:
            if l_op != other_l_op:
                return False   
        else:
            #If different return false
            if not has_logical_operators and l_op != None:
                return False
            
        if has_relational_operators and r_op != None:
            if r_op != other_r_op:
                return False
        else:
            #If different return false
            if not has_relational_operators and r_op != None:
                return False
        return True
    
        
    
    