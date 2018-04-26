# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:02:04 2018

@author: Gerardo Cervantes
"""


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

            
    
        
    

