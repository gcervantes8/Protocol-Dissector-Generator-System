# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:35:55 2018

@author: Gerardo Cervantes
"""

from ReferenceList import ReferenceList

class Field():
    
    def __init__(self, field_size):
        self.set_field_size(field_size)
        pass
    
    def set_field_info(self, name, abbrev, desc, ref_list, data_type, base, mask, value_constraint, is_required):
        
        self.name = name
        self.abbrev = abbrev
        self.desc = desc
        self.data_type = data_type
        self.base = base
        self.mask = mask
        self.value_constraint = value_constraint
        self.is_required = is_required


    def get_field_info(self):
        
        return self.name + ',' + self.abbrev + ',' + self.desc + ',' + self.data_type + ',' + self.base + ',' + self.mask + ',' + self.value_constraint + ',' + self.is_required 
        
    def set_ref_list(self, ref_list):
        if issubclass(ref_list, ReferenceList):
            self.ref_list = ref_list
        else:
            self.ref_list = None
        
    def get_ref_list(self):
        try:
            return self.ref_list
        except NameError:
            return None

    def get_field_size(self):        
        try:
            return self.field_size
        except NameError:
            return None
    
    def set_field_size(self, field_size):
        self.field_size = field_size
    
        
    
    