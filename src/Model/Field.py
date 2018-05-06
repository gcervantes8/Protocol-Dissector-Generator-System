# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:35:55 2018

@author: Gerardo Cervantes
"""

import Construct
import ReferenceList

class Field(Construct.Construct):
    
    def __init__(self, field_size):
        super(Field, self).__init__()
        self.set_field_size(field_size)
        pass
    
    def set_field_info(self, name, abbrev, desc, data_type, base, mask, value_constraint, is_required):
        
        self.name = name
        self.abbrev = abbrev
        self.desc = desc
        self.data_type = data_type
        self.base = base
        self.mask = mask
        self.value_constraint = value_constraint
        self.is_required = is_required


    def get_field_info(self):
        name = self.name.replace(',', ';')
        abbrev = self.abbrev.replace(',', ';')
        desc = self.desc.replace(',', ';')
        data_type = self.data_type.replace(',', ';')
        base = self.base.replace(',', ';')
        mask = self.mask.replace(',', ';')
        value_constraint = self.value_constraint.replace(',', ';')
        is_required = self.is_required.replace(',', ';')
        return name + ',' + abbrev + ',' + desc + ',' + data_type + ',' + base + ',' + mask + ',' + value_constraint + ',' + is_required 
        
    def set_ref_list(self, ref_list):
        if ref_list.isRefList:
            self.ref_list = ref_list
        else:
            self.ref_list = None
        
    def get_ref_list(self):
        try:
            return self.ref_list
        except AttributeError:
            return None

    def get_field_size(self):        
        try:
            return self.field_size
        except AttributeError:
            return None
    
    def set_field_size(self, field_size):
        self.field_size = field_size
        
    
    #Used for dictionary of objects in protocol
    def __hash__(self):
        try:
            return hash((self.name, self.abbrev, self.desc, self.data_type, self.base, self.mask, self.value_constraint, self.is_required, self.field_size))    
        except AttributeError:
            return hash(self.field_size)
    #Used for dictionary of objects in protocol
    def __eq__(self, other):
        try:
            a = self.mask
            has_field_info = True
        except AttributeError:
            has_field_info = False
        try:
            a = other.mask
            other_has_field_info = True
        except AttributeError:
            other_has_field_info = False
            
        if not (has_field_info == other_has_field_info):
            return False
        
        if has_field_info:
            return self.name == other.name and self.abbrev == other.abbrev and self.desc == other.desc and self.data_type == other.data_type and self.base == other.base and self.mask == other.mask and self.value_constraint == other.value_constraint and self.is_required == other.is_required and self.field_size == other.field_size    
        else:
            return self.field_size == other.field_size
        
        
    
        
    
    