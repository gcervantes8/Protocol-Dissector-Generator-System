# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:57:52 2018

@author: Gerardo Cervantes
"""


import StartField
import Field
import EndField
import Expression
import DecisionConstruct
import Protocol
import ReferenceList

def example_protocol():
    sf = StartField.StartField('myProtocol', 'This is an example protocol that says the second byte is the amount of wins I have if the first bit in the first byte is bigger than 8, otherwise it is the number of losses')
    
    sf.set_dependency_pattern('Integer')
    sf.set_dependency_protocol('Dependent protocol')
    
    f1 = Field.Field(1)
    
    sf.set_next_constructs([f1])

    
    f1.set_field_info('TypeBitCheck', 'check', 'Checks first bit', 'ftypes.UINT8', 'base.HEX', '0x80', '?', 'True')
    
    ref_list = ReferenceList.ReferenceList('ref_list')
    ref_list.set_descriptions(['is a value'])
    ref_list.set_values(['13'])
    
    f1.set_ref_list(ref_list)
    
    expr1 = Expression.Expression()
    expr1.set_relational_operators(['>='])
    expr1.set_operands(['8'])
    
    expr2 = Expression.Expression()
    expr2.set_relational_operators(['<'])
    expr2.set_operands(['8'])
    
    
    dc = DecisionConstruct.DecisionConstruct()
    dc.set_expressions([expr1, expr2])
    f1.set_next_constructs([dc])
    
    
    f2 = Field.Field(1)
    f2.set_field_info('Number of wins', 'wins', 'Is the number of wins', 'ftypes.UINT8', 'base.HEX', '0xff', '?', 'True')
    
    f3 = Field.Field(1)
    f3.set_field_info('Number of loses', 'loses', 'Is the number of loses', 'ftypes.UINT8', 'base.HEX', '0xff', '?', 'True')
    
    dc.set_next_constructs([f2,f3])
    end_field = EndField.EndField()
    
    f2.set_next_constructs([end_field])
    f3.set_next_constructs([end_field])
    
    protocol = Protocol.Protocol()
    protocol_structure = protocol.get_protocol_structure(sf)
    return protocol_structure
