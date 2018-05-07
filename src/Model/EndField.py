# -*- coding: utf-8 -*-
"""
Created on Sat May  5 17:36:13 2018

@author: Gerardo Cervantes
"""

import Construct

class EndField(Construct.Construct):
    def __init__(self):
        super(EndField, self).__init__()
        
        
        #Used for dictionary of objects in protocol
    def __hash__(self):
        
        return hash('EndField')
    #Used for dictionary of objects in protocol
    def __eq__(self, other):
        return self.__hash__ == other.__hash__
        