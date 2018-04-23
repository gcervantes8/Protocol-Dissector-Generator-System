from Dissector import Dissector
from Packet import Packet
class DissectorManager():
    dis = Dissector()

    def dissector_delegator(self,packet,packet_info,path,format,protocol):
        packet = Packet()
        if(packet == None):
            if(protocol == None):
                self.dis.get_dissector_scripts(path)
            else:
                self.dis.create_dissector_script(protocol,path,file,format)
        else:
            if(packet_info == None):
                self.dis.dissect_packets()
            elif(packet_info == 1):
                packet.get_data()
            elif(packet_info == 2):
                packet.get_name()
            elif(packet_info == 3):
                packet.get_description
            elif(packet_info == 4):
                packet.get_color()
            else:
                print ("Invalid")
                return

if __name__ == "__main__":
    man = DissectorManager()
    man.dissector_delegator("dd",None,None,None,None)
