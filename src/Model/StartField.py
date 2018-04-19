# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:24:50 2018

@author: Gerardo Cervantes
"""

from Construct import Construct

#StartField keeps track of the protocol name and description.  As well as any
#Dependent protocols and their pattern.

class StartField(Construct):
    
    def __init__(self, protocol_name, protocol_description):
        self.set_protocol_name(self, protocol_name)
        self.set_protocol_description(self, protocol_description)
    
    def set_protocol_name(self, protocol_name):
        self.protocol_name = protocol_name
    
    def set_protocol_description(self, protocol_desc):
        self.protocol_description = protocol_desc
        
    def get_protocol_name(self):
        try:
            return self.protocol_name
        except NameError:  
            return None
        
    def get_protocol_description(self):
        try:
            return self.protocol_description
        except NameError:  
            return None
        
    def get_dependency_protocol(self):
        try:
            return self.dependency
        except NameError:  
            return None
    def set_dependency_protocol(self, dependency_protocol):
        self.dependency = dependency_protocol
        
    #Returns false if was given an invalid parameter, nothing will be set if invalid parameter
    def set_dependency_pattern(self, dependency_pattern):
        if self._is_valid_dependency_pattern(dependency_pattern):
            self.dependency_pattern = dependency_pattern
        else:
            self.dependency_pattern = None
            
        
    def get_dependency_pattern(self):
        try:
            pattern = self.dependency_pattern
            if self._is_valid_dependency_pattern(pattern):
                return pattern
        except NameError:  
            pass
        return None
        
    def _is_valid_dependency_pattern(self, dependency_pattern):
        if dependency_pattern == "Integer" or dependency_pattern == "String" or dependency_pattern == "Range":
            return True
        
        
        
    
    