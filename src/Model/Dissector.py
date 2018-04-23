import platform
import subprocess

class Dissector(object):
    eed = str()
    sub = " "



    #Call Tshark and
    def dissect_packets(self):

        host_platform = platform.system()

        if(host_platform == 'Windows'):
            subprocess.call('cd C:\\Program Files\\Wireshark && tshark.exe -r file2.pcap -T json ',shell = True)
        elif(host_platform == 'Linux'):
            print('Linux Method')
            subprocess.call('tshark -T',shell=True)
        else:
            print("Not supported")

    def get_dissector_scripts(self,path):
        print("X")
    def create_dissector_script(self,protocol,path,file,format):
        print("THIS IS HARD")

if __name__ == "__main__":
    dis = Dissector()
    dis.dissect_packets()
