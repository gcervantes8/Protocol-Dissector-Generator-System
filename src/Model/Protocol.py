# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:02:04 2018

@author: Gerardo Cervantes
"""

from Field import Field
from DecisionConstruct import DecisionConstruct
from StartField import StartField
from EndField import EndField

import xml.etree.cElementTree as ET
class Protocol():
    
    def __init__(self):
        pass
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        try:
            return self.name
        except NameError:
            return None
    
    def get_protocol_structure(self, startField):
        
        #Contains a dictionary 
        self.construct_dictionary = {}
        constructs_added_to_xml = []
        
        construct_count = 1
        
        root = ET.Element("root")
        
        constructs_to_add = [startField]
            
        #Goes through queue of constructs
        while len(constructs_to_add) != 0:
            construct = constructs_to_add.pop(0)
            
            #Goes through next constructs and adds to queue, and gives them a var name
            for next_construct in construct.get_next_constructs():
                
                #If first encounter of construct, give var name and add to construct to add later
                if not construct in self.construct_dictionary:
                    
                    
                    #Add to dictionary and give is a variable name
                    self.construct_dictionary[construct] = 'c' + str(construct_count)
                    construct_count += 1
                    constructs_to_add.append(construct)
                    
            if not construct in constructs_added_to_xml:
                self._add_xml(construct, root)
                constructs_added_to_xml.append(construct)
            
                
                
        
        
        #Write and print
        xmlstr = ET.tostring(root, encoding='utf8', method='xml')
        tree = ET.ElementTree(root)
        tree.write("filename.xml")
        print(xmlstr)
    
    def _add_xml(self, construct, element_tree):
        if issubclass(type(construct), Field):
            self._add_field_xml(self, construct, element_tree)
        elif issubclass(type(construct), StartField):
            self._add_start_field_xml(construct, element_tree)
        elif issubclass(type(construct), EndField):
            self._add_end_field_xml(construct, element_tree)
        elif issubclass(type(construct), DecisionConstruct):
            self._add_decision_construct_xml(construct, element_tree)
            
    def _add_start_field_xml(self, start_field, element_tree):
        start_node = ET.SubElement(element_tree, "StartField")
        
        #Add startfield
        ET.SubElement(start_node, "name").text = start_field.get_protocol_name()        
        ET.SubElement(start_node, "description").text = start_field.get_protocol_description()
        ET.SubElement(start_node, "dependency_protocol").text = start_field.get_dependency_protocol()
        ET.SubElement(start_node, "dependency_pattern").text = start_field.get_dependency_pattern()  
        self._add_next_constructs(self, start_field, start_node)
        
    def _add_decision_construct_xml(self, decision_construct, element_tree):
        decision_node = ET.SubElement(element_tree, "DecisionConstruct")
        expressions = decision_construct.get_expressions()
        for expr in expressions:
            self._add_expression_construct_xml(self, expr, decision_node)
        self._add_next_constructs(self, decision_construct, decision_node)
                    
    def _add_next_constructs(self, construct, element_tree):
        for construct in construct.get_next_constructs():
            ET.SubElement(element_tree, "next").text = self.construct_dictionary[construct]
    
    def _add_expression_construct_xml(self, expression, element_tree):
        expr_node = ET.SubElement(element_tree, "Expression")
        
        for op in expression.get_operands():
            ET.SubElement(expr_node, "operands").text = op
        for op in expression.get_relational_operators():
            ET.SubElement(expr_node, "RelationalOperators").text = op
        for op in expression.get_logical_operators():
            ET.SubElement(expr_node, "LogicalOperators").text = op
            
        
    #element_tree is tree from xml ElementTree ET
    def _add_field_xml(self, field, element_tree):
        field_node = ET.SubElement(element_tree, "Field")
        
        str_field_info = field.get_field_info()
        field_info = str_field_info.split(',')
        #Add startfield
        ET.SubElement(field_node, "size").text = field.get_field_size()        
        ET.SubElement(field_node, "name").text = field_info[0]
        ET.SubElement(field_node, "abbrev").text = field_info[1]
        ET.SubElement(field_node, "desc").text = field_info[2]
        ET.SubElement(field_node, "data_type").text = field_info[3]
        ET.SubElement(field_node, "base").text = field_info[4]
        ET.SubElement(field_node, "mask").text = field_info[5]
        ET.SubElement(field_node, "value_constraint").text = field_info[6]
        ET.SubElement(field_node, "is_required").text = field_info[7]
        
        self._add_next_constructs(self, field, field_node)
        
    def _add_end_field_xml(self, end_field, element_tree):
        end_node = ET.SubElement(element_tree, "EndField")    
    
    def set_description(self, description):
        self.description = description
        
    def get_description(self):
        try:
            return self.description
        except NameError:
            return None
    
    def set_dependency(self, dependency):
        self.dependency = dependency
        
    def get_dependency(self):
        try:
            return self.dependency
        except NameError:
            return None

    def get_dependency_pattern(self, dependency_pattern):
        
        try:
            return self.dependency_pattern
        except NameError:
            return None
        
    def set_dependency_pattern(self, dependency_pattern):
        if dependency_pattern in ['Integer', 'String', 'Range']:
            self.dependency_pattern = dependency_pattern

            
    
        
    

