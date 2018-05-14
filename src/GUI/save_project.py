# -*- coding: utf-8 -*-


import xml.etree.cElementTree as ET
import xml.dom.minidom
import Tkinter as tk
from dissector_script_window import DissectorScriptWindow

class SaveProjectXML():
    
    def __init__(self):
        pass
    
    def create_xml(self):
        root = ET.Element('gui')
        field = ET.Element('Field')
        root.append(field)
        startField = ET.Element('StartField')
        field.append(startField)
        
        
        xPos = ET.SubElement(startField, 'xPos')
        xPos.text = '300'
        yPos = ET.SubElement(startField, 'yPos')
        yPos.text = '320'
        
        
        #get postitions of active widgets
        field_items = DissectorScriptWindow.field_items
        for i, item in enumerate(field_items):
            print(item)
    
        
        construct_items = DissectorScriptWindow.construct_items
        for i, item in enumerate(construct_items):
            print(item)
            
        

        
        
        
            
        print(root)

        
        #Write and print
        xmlstr = ET.tostring(root, encoding='utf8', method='xml')
        
        parsed_xml = xml.dom.minidom.parseString(xmlstr) # or xml.dom.minidom.parseString(xml_string)
        pretty_xml_as_string = parsed_xml.toprettyxml()
        print(pretty_xml_as_string)
        
        #Returns the non-pretty xml to prevent possible spacing errors
        return xmlstr
#        tree = ET.ElementTree(root)
#        tree.write("gui.xml")
#        print(xmlstr)
    
if __name__ == "__main__":
    SaveProjectXML()