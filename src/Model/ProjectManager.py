from Workspace import Workspace
from Project import Project

w1 = Workspace()
class ProjectManager():

    def guiInfo(self,workspace_name, path, project_name, desc, layout, getter):
        project = Project();
        if(workspace_name != None):
            if(path != None):
                w1.setPath(path)
                w1.setName(workspace_name)
                Workspace.current = w1
            else:
                print ("Invalid1")
                return
        elif (project_name != None):
            if(desc != None):
                project.setName(project_name)
                project.setDesc(desc)
                project.createProject()
                Project.current = project
            else:
                project.loadProject(project_name)
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
                return a
            #elif(getter == 3):
             #   Project.getDesc()
            else:
                print ("Invalid3")
                return

if __name__ == "__main__":
    print"test"
