# -*- coding: utf-8 -*-


import xml.etree.cElementTree as ET
import xml.dom.minidom
import Tkinter as tk
from dissector_builder_area import Dissector_builder_area

class ExportProjectXML():
    
    def create_xml(self, Dissector_builder_area):
        
        root = ET.Element('PDGSgui')
        field = ET.Element('Field')
        root.append(field)
        
        fieldType = ET.SubElement(field, 'StartField')
        fieldType.text = 'the stuff'
        xPos = ET.SubElement(field, 'xPos')
        xPos.text = '300'
        yPos = ET.SubElement(field, 'yPos')
        yPos.text = '320'
        
        
        #get postitions of active widgets
        field_items = Dissector_builder_area.canvas.children.values()
        for i, item in enumerate(field_items):
            print(item.winfo_width())


            
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
#        print(xmlst)
        
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    s = ExportProjectXML()
    s.create_xml(Dissector_builder_area(root))
    root.mainloop()