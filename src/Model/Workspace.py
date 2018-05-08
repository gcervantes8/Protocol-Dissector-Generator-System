import os
from Project import Project

class Workspace(object):
    path = str()
    name = str()

    # Getter Methods
    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def get_projects_lists(self):
        a = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".xml"): # .txt just to test change to .xml later
                    a.append(file)
        return a


    # Setter Methods
    def setPath(self, path):
        self.path = path

    def setName(self, name):
        self.name = name
