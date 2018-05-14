import platform
import subprocess
import xml.etree.ElementTree as ET
from example_protocol import example_protocol

class Dissector(object):
    eed = str()
    sub = " "



    #Call Tshark and
    def dissect_packets(self):

        host_platform = platform.system()

        if(host_platform == 'Windows'):
            subprocess.call('cd C:\\Program Files\\Wireshark && tshark.exe -r file2.pcap -T json  ',shell = True)
        elif(host_platform == 'Linux'):
            print('Linux Method')
            subprocess.call('tshark -T',shell=True)
        else:
            print("Not supported")

    def get_dissector_scripts(self,path):
        print("X")
    def create_dissector_script(self, xml_string):
        
        xml_tree = ET.ElementTree(ET.fromstring(xml_string))
#        xml_tree = ET.parse(xml_file)
        root = xml_tree.getroot()
        
        lua_script = ""
        start_field_item = self.find_item(root, 'StartField')
        
        end_field_item = self.find_item(root, 'EndField')
        end_field_var = self.find_item(end_field_item, 'var').text
        if start_field_item == None:
            return 'Error Start field found\n'
        
        
        protocol_var = self.find_item(start_field_item, 'var').text
        protocol_name = self.find_item(start_field_item, 'name').text
        protocol_desc = self.find_item(start_field_item, 'description').text
        protocol_next = self.find_item(start_field_item, 'next').text
        
        fields = self.find_all_items(root, 'Field')
        decision_constructs = self.find_all_items(root, 'DecisionConstruct')
        lua_script += 'local ' + protocol_var + ' = Proto(\"' + protocol_name + '\", \"' + protocol_desc + '\")\n\n'
        
        for i, field in enumerate(fields):

            ref_list = self.find_item(field, 'ReferenceList')
            ref_list_var = 'nil'
            if ref_list != None:
                ref_list_var = 'r'+ str(i)
                values = self.find_all_items(ref_list, 'value')
                descs = self.find_all_items(ref_list, 'desc')
                lua_script += 'local ' + ref_list_var + ' = {'
                for i, value in enumerate(values):
                    lua_script += '[' + value.text + '] = \"' + descs[i].text + '\"'
                    
                    #If not last item, then add comma
                    if i != len(values)-1:
                        lua_script += ','
                        
                lua_script += '}\n'
            
            field_var = self.find_item(field, 'var').text
            field_size = self.find_item(field, 'size').text
            field_name = self.find_item(field, 'name').text
            field_abbrev = self.find_item(field, 'abbrev').text
            field_desc = self.find_item(field, 'desc').text
            field_data_type = self.find_item(field, 'data_type').text
            field_base = self.find_item(field, 'base').text
            field_mask = self.find_item(field, 'mask').text
            field_value_constraint = self.find_item(field, 'value_constraint').text
            field_is_required = self.find_item(field, 'is_required').text
            protocol_name = self.find_item(start_field_item, 'name').text
            protocol_desc = self.find_item(start_field_item, 'description').text
            
            
            lua_script += 'local ' + field_var + ' = ProtoField.new("' + field_name + '", "' + field_abbrev + '", "' + field_data_type + '", "' + field_base + '", ' + ref_list_var +', ' + field_mask + '", "' + field_desc + '")\n\n'
        
        
        self.tvbuf = 'tvbuf'
        self.pktinfo = 'pktinfo'
        self.root = 'root'
        
        
        lua_script += 'function ' + protocol_var + '.dissector(' + self.tvbuf + ', ' + self.pktinfo + ', ' + self.root + ')\n\n'
        #Print string when starting dissecting
        lua_script += 'dprint2("dns.dissector called")'
        
        lua_script += self.pktinfo + '.cols.protocol:set("' + protocol_name + '")\n'
        
        
        
        self.offset_str = 'offset'
        self.temp_str = 'temp'
        lua_script += 'local ' + self.offset_str + ' = 0\n'
        lua_script += 'local ' + self.temp_str + ' = 0\n'
        
        lua_code = self.write_lua_field_decisions(protocol_next, fields, decision_constructs, end_field_var)
                
        lua_script += lua_code
        lua_script += 'return ' + self.offset_str + '\n'
        lua_script += 'end' #Function end
        
        return lua_script
    
    def write_lua_field_decisions(self, next_item_var, fields, decision_constructs, end_field_var):
        lua_code = ''
        while next_item_var != end_field_var:
            decision_construct_xml = None
            
            
            field_xml = self.find_item_from_xml_list(fields, next_item_var)
            
            is_field = (field_xml != None)
            if not is_field:
                decision_construct_xml = self.find_item_from_xml_list(decision_constructs, next_item_var)
                
            if is_field:
                field_size = self.find_item(field_xml, 'size').text
                lua_code += self.temp_str + ' = ' + self.tvbuf + ':range(' + self.offset_str + ', ' + str(field_size) + ')\n'
                lua_code += self.root + ':add(' + next_item_var + ', ' + self.temp_str + ')\n'
                next_item_var = self.find_item(field_xml, 'next').text
        
            elif decision_construct_xml != None:
                expressions = self.find_all_items(decision_construct_xml, 'Expression')
                for i, expr in enumerate(expressions):
                    next_vars = self.find_all_items(decision_construct_xml, 'next')
                    next_item = next_vars[i].text
                    relational_operator = self.find_item(expr, 'RelationalOperators').text
                    operands = self.find_item(expr, 'operands').text
                    lua_code += 'if ' + self.temp_str + ' ' + relational_operator + ' ' + operands + ' then\n'
                    if_body_code = self.write_lua_field_decisions(next_item, fields, decision_constructs, end_field_var)
                    lua_code += if_body_code + '\nend\n'
                break
                    
                    
                    
                
        return lua_code
                
    
    #Root is list of xml items, var is the variable name, returns xml item if was there
    def find_item_from_xml_list(self, items_list, tag):
        for xml_item in items_list:
                
                xml_tag = self.find_item(xml_item, 'var').text
                if xml_tag == tag:
                    return xml_item
                
        return None
    
    #Returns list of all items that match tag in xml
    def find_all_items(self, root, tag):
        items = []
        for child in root:
            if (child.tag == tag):
                items.append(child)
        return items
    
    def find_item(self, root, tag):
        for child in root:
            if (child.tag == tag):
                return child


if __name__ == "__main__":
    dis = Dissector()
    #dis.dissect_packets()
    lua_script = dis.create_dissector_script(example_protocol())
    print(lua_script)
