# -*- coding: utf-8 -*-
"""
Created on Mon May 14 20:00:55 2018

@author: Gerardo Cervantes
"""
import xml.etree.ElementTree as ET

def parse_pdml_xml(xml_string):
    
    xml_tree = ET.ElementTree(ET.fromstring(xml_string))
    root = xml_tree.getroot()
#    lua_script = ""
    packet_items = find_all_items(root, 'packet')
    
    field_name_items = []
    
    first_packet = packet_items[0]
    proto_item = find_item(first_packet, 'proto')
    proto_field_items = find_all_items(proto_item, 'field')
    for field_item in proto_field_items:
        field_name_items.append(field_item.attrib['name'])
    
    field_items_values = []
    
    for item in field_name_items:
        field_items_values.append([])
        
    proto_objects_first_packet = find_all_items(packet_items[0], 'proto')
    for packet in packet_items:
#        print('a')
        proto_items = find_all_items(packet, 'proto')
#        print(proto_items)
        proto_field_items = find_all_items(proto_items[0], 'field')
#        print(proto_field_items)
        for i, field in enumerate(proto_field_items):
#            print('b')
            print(field.attrib['show'])
            field_items_values[i].append(field.attrib['show'])
            
    headers = []
    for i, proto_object in enumerate(proto_objects_first_packet):
        
        if i == 0 or i == len(proto_objects_first_packet)-1:
            continue
        header_dict = proto_object.attrib
        headers.append(header_dict['showname'])
        
    dissected_values = []
        
    for i, proto_object in enumerate(proto_objects_first_packet):
        if i == 0 or i == len(proto_objects_first_packet)-1:
            continue
        fields_in_proto = find_all_items(proto_object, 'field')
        
        field_items = ''
        for field_item in fields_in_proto:
            try:
                field_items += (field_item.attrib['showname'] + ' \n')
            except KeyError:
                continue;
                    
            
        dissected_values.append(field_items)
            
#    print('field_items')
#    print(field_name_items)
#    print(field_items_values)
#    
#    print('headers')
#    print(headers)
#    print(dissected_values)
    
    return field_name_items, field_items_values, headers, dissected_values
    

#Root is list of xml items, var is the variable name, returns xml item if was there
def find_item_from_xml_list(items_list, tag):
    for xml_item in items_list:
            
            xml_tag = find_item(xml_item, 'var').text
            if xml_tag == tag:
                return xml_item
            
    return None

#Returns list of all items that match tag in xml
def find_all_items(root, tag):
    items = []
    for child in root:
        if (child.tag == tag):
            items.append(child)
    return items

def find_item(root, tag):
    for child in root:
        if (child.tag == tag):
            return child


if __name__ == "__main__":

#    xml_protocol = example_ICMP_protocol()
#    lua_script = dis.create_dissector_script(xml_protocol)
#    print(lua_script)
    pdml_xml_file = open('pdml.xml', "r")
    pdml_xml = pdml_xml_file.read()
    print(pdml_xml)
    parse_pdml_xml(pdml_xml)
    