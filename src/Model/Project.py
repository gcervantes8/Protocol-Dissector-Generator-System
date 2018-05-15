import os
import xml.etree.ElementTree as et
from Workspace import Workspace


class Project(object):
        name = str()
        desc = str()

        def getName(self):
            return self.name

        def getDesc(self):
            return self.desc

        def setDesc(self, desc):
            self.desc = desc

        def setName(self, name):
            self.name = name

        def loadProject(self, name):
            if name is None:
                return
            else:
                print name + " this is current project"

        def createProject(self):
            name = self.name
            desc = self.desc
            dirPath = Workspace.current.getPath()
            xml = "<myxmldata/>"
            f = open(dirPath +"/"+name+".xml", "wb")
            f.write("<!-- " + desc + " -->")
            f.write(xml)
            f.close()
