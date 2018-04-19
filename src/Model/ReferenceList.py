# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:24:50 2018

@author: Gerardo Cervantes
"""

#Reference list contains a name, values, and corresponding descriptions for those values


class ReferenceList():
    
    def __init__(self, name):
        self.set_name(name)
    
    def set_name(self, name):
        self.name = name
        
    #List of values
    def set_values(self, values):
        self.values = values
    
    #List of descriptions for each value
    def set_descriptions(self, descriptions):
        self.descriptions = descriptions
        
    def get_name(self):
        try:
            return self.name
        except NameError:  
            return None

    def get_values(self):
        try:
            return self.values
        except NameError:  
            return None
        
    def get_descriptions(self):
        try:
            return self.descriptions
        except NameError:  
            return None
        
        
    
    