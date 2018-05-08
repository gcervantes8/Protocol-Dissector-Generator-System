import os
import xml.etree.ElementTree as et
from Workspace import Workspace


class Project(object):
        name = str()
        desc = str()

        def getPath(self):
            return self.path

        def getDesc(self):
            return self.desc

        def setDesc(self, desc):
            self.path = desc

        def setName(self, name):
            self.name = name

        def loadProject(xml):
            if xml is None:
                return
            else:
                return Project('', '')

        def createProject(self):
            name = self.name
            dirPath = Workspace.current.getPath()
            xml = "<myxmldata/>"
            f = open(dirPath +"/"+name+".xml", "wb")
            f.write(xml)
            f.close()

