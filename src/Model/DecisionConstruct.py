
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:35:55 2018

@author: Gerardo Cervantes
"""

from Expression import Expression
from Construct import Construct

class DecisionConstruct(Construct):
    
    def __init__(self):
        super(DecisionConstruct, self).__init__()
        
    def set_expressions(self, expressions):
        
        if type(expressions) is list:
                for exp in expressions:
                    print('an expr')
                    try:
                        isExpression = exp.isExpression
                    except AttributeError:
                        isExpression = False
                        
                    if not isExpression:
                        self.expressions = None
                        return
        self.expressions = expressions
        
    def get_expressions(self):
        try:
            return self.expressions
        except AttributeError:
            return None

    #Used for dictionary of objects in protocol
    def __hash__(self):
        if self.get_expressions():
            return hash(None)
        return hash(self.get_expressions()[0])
            
    #Used for dictionary of objects in protocol
    def __eq__(self, other):
        try:
            expr = other.get_expressions()
        except AttributeError:
            return False
        return self.get_expressions() == expr
        
        
    