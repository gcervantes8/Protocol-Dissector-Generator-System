from Workspace import Workspace
from Project import Project

w1 = Workspace()
class ProjectManager():

    def guiInfo(self,workspace_name, path, project_name, desc, layout, getter):
        if(workspace_name != None):
            if(path != None):
                w1.setPath(path)
                w1.setName(workspace_name)
            else:
                print ("Invalid1")
                return
        elif (project_name != None):
            if(desc != None):
                print"calling project to create a project"
            else:
                print ("Invalid2")
                return
        #elif(layout != None):
         #   Project.getLayout()
        else:
            if(getter == 0):
                print "check " + w1.getPath()
            elif(getter == 1):
                w1.getName()
            elif(getter == 2):
                a = w1.get_projects_lists()
                print ("\n" . join(a))
            #elif(getter == 3):
             #   Project.getDesc()
            else:
                print ("Invalid3")
                return

if __name__ == "__main__":
    print"test"
