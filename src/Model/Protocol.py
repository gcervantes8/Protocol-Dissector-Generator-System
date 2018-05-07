# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:02:04 2018

@author: Gerardo Cervantes
"""

import Field
import DecisionConstruct
import StartField
import EndField
import xml.etree.cElementTree as ET
import xml.dom.minidom

class Protocol():
    
    def __init__(self):
        pass
    
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
                if not hash(next_construct) in self.construct_dictionary:
                    
                    print(hash(next_construct))
                    #Add to dictionary and give is a variable name
                    self.construct_dictionary[hash(next_construct)] = 'c' + str(construct_count)
                    construct_count += 1
                    constructs_to_add.append(next_construct)
                    
            if not construct in constructs_added_to_xml:
                
                print(self.construct_dictionary)
                self._add_xml(construct, root)
                constructs_added_to_xml.append(construct)
            
        
        #Write and print
        xmlstr = ET.tostring(root, encoding='utf8', method='xml')
        
        parsed_xml = xml.dom.minidom.parseString(xmlstr) # or xml.dom.minidom.parseString(xml_string)
        pretty_xml_as_string = parsed_xml.toprettyxml()
        print(pretty_xml_as_string)
        
        #Returns the non-pretty xml to prevent possible spacing errors
        return xmlstr
#        tree = ET.ElementTree(root)
#        tree.write("filename.xml")
#        print(xmlstr)
    
    def _add_xml(self, construct, element_tree):
        if issubclass(type(construct), Field.Field):
            self._add_field_xml(construct, element_tree)
        elif issubclass(type(construct), StartField.StartField):
            print('Start field found')
            self._add_start_field_xml(construct, element_tree)
        elif issubclass(type(construct), EndField.EndField):
            self._add_end_field_xml(construct, element_tree)
        elif issubclass(type(construct), DecisionConstruct.DecisionConstruct):
            self._add_decision_construct_xml(construct, element_tree)
            
    def _add_start_field_xml(self, start_field, element_tree):
        start_node = ET.SubElement(element_tree, "StartField")
        ET.SubElement(start_node, "var").text = 'c'
        
        #Add startfield
        ET.SubElement(start_node, "name").text = self._to_none(start_field.get_protocol_name())        
        ET.SubElement(start_node, "description").text = self._to_none(start_field.get_protocol_description())
        ET.SubElement(start_node, "dependency_protocol").text = self._to_none(start_field.get_dependency_protocol())
        ET.SubElement(start_node, "dependency_pattern").text = self._to_none(start_field.get_dependency_pattern())
        self._add_next_constructs(start_field, start_node)
        
    def _add_decision_construct_xml(self, decision_construct, element_tree):
        decision_node = ET.SubElement(element_tree, "DecisionConstruct")
        
        ET.SubElement(decision_node, "var").text = self.construct_dictionary[hash(decision_construct)]
        expressions = decision_construct.get_expressions()
        
        if expressions != None:
            for expr in expressions:
                self._add_expression_construct_xml(expr, decision_node)
        self._add_next_constructs(decision_construct, decision_node)
                    
    def _add_next_constructs(self, construct, element_tree):
        for construct in construct.get_next_constructs():
            var_name = self.construct_dictionary[hash(construct)]
            ET.SubElement(element_tree, "next").text = self._to_none(var_name)
    
    def _add_expression_construct_xml(self, expression, element_tree):
        expr_node = ET.SubElement(element_tree, "Expression")
        op, r_op, l_op = expression.get_operands(), expression.get_relational_operators(), expression.get_logical_operators()
        if op != None:
            for item in op:
                ET.SubElement(expr_node, "operands").text = self._to_none(item)
        if r_op != None:
            for item in r_op:
                ET.SubElement(expr_node, "RelationalOperators").text = self._to_none(item)
        if l_op != None:
            for item in l_op:
                ET.SubElement(expr_node, "LogicalOperators").text = self._to_none(item)
            
        
    #element_tree is tree from xml ElementTree ET
    def _add_field_xml(self, field, element_tree):
        field_node = ET.SubElement(element_tree, "Field")
        ET.SubElement(field_node, "var").text = self.construct_dictionary[hash(field)]
        str_field_info = field.get_field_info()
        field_info = str_field_info.split(',')
        #Add startfield
        ET.SubElement(field_node, "size").text = self._to_none(str(field.get_field_size()))
        items = ['name', 'abbrev', 'desc', 'data_type', 'base', 'mask', 'value_constraint', 'is_required']
        
        for i, item in enumerate(items):
            ET.SubElement(field_node, item).text = self._to_none(field_info[i])
            
        ref_list = field.get_ref_list()
        if ref_list != None:
            ref_node = ET.SubElement(field_node, "ReferenceList")
            values = ref_list.get_values()
            descs = ref_list.get_descriptions()
            for value in values:
                ET.SubElement(ref_node, "value").text = self._to_none(value)
            for desc in descs:
                ET.SubElement(ref_node, "desc").text = self._to_none(desc)                
                
        self._add_next_constructs(field, field_node)
        
    def _add_end_field_xml(self, end_field, element_tree):
        end_node = ET.SubElement(element_tree, "EndField")  
        ET.SubElement(end_node, "var").text = self.construct_dictionary[hash(end_field)]
        
    def _to_none(self, item):
        if item == None:
            return 'NONE'
        return item

    #To meet our design we should have these functions
    
#    def set_name(self, name):
#        self.name = name
#        
#    def get_name(self):
#        try:
#            return self.name
#        except NameError:
#            return None
    
#    def set_description(self, description):
#        self.description = description
#        
#    def get_description(self):
#        try:
#            return self.description
#        except NameError:
#            return None
    
#    def set_dependency(self, dependency):
#        self.dependency = dependency
#        
#    def get_dependency(self):
#        try:
#            return self.dependency
#        except NameError:
#            return None
#
#    def get_dependency_pattern(self, dependency_pattern):
#        
#        try:
#            return self.dependency_pattern
#        except NameError:
#            return None
#        
#    def set_dependency_pattern(self, dependency_pattern):
#        if dependency_pattern in ['Integer', 'String', 'Range']:
#            self.dependency_pattern = dependency_pattern
            

            
    
        
    

