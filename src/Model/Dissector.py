import platform
import subprocess
import xml.etree.ElementTree as ET
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
    def create_dissector_script(self,xml_file):
        xml_tree = ET.parse(xml_file)
        root = xml_tree.getroot()
        for child in root:
            if (child.tag == 'StartField'):
                for children in child:
                    print("%s"%(children.text))



if __name__ == "__main__":
    dis = Dissector()
    #dis.dissect_packets()
    dis.create_dissector_script('example.xml')
