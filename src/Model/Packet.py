

class Packet(object):
    name = str()
    description = str()
    color = str()
    data = str()




    #Getter Methods
    def get_data(self):
        return self.data

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description


    #Setter Methods
    def set_data(self,data):
        self.data = data

    def set_color(self,color):
        self.color = color

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description
