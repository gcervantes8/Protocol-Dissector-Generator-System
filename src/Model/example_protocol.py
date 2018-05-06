# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:57:52 2018

@author: Gerardo Cervantes
"""


from StartField import StartField
from Field import Field
from Expression import Expression
from DecisionConstruct import DecisionConstruct


sf = StartField('myProtocol', 'This is an example protocol that says the second byte' + 
           'is the amount of wins I have if the first bit in the first byte is bigger than 8, otherwise it is the number of losses')

sf.set_dependency_pattern('Integer')
sf.set_dependency_protocol('Dependent protocol')

f1 = Field(1)

sf.set_next_constructs([f1])

f1.set_field_info('TypeBitCheck', 'check', 'Checks first bit', 'Integer', 'Integer', '0x80', '?', 'True')
expr1 = Expression()
expr1.set_relational_operators('>=')
expr1.set_operands('8')

expr2 = Expression()
expr2.set_relational_operators('<')
expr2.set_operands('8')


dc = DecisionConstruct()
dc.set_expressions([expr1, expr2])
f1.set_next_constructs([dc])
f2 = Field(1)
f2 = Field(1)