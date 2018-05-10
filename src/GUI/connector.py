from Tkinter import *

count = 1
IPvar = 256
f = 0
ConnectCount = 1
a = 0
temp = 0
temp2 = 0

itemsconnectors = []
itemlist = []
LinkedItems = []
#______________________________________________________________________________________________________________________________________________________________________

class Window:

    #______________________________________________________________________________________________________________________________________________________________________

    def __init__(self, window, colour = 'White', width = 1440, height = 720):
        #window variables
        self.colour = colour
        self.screenwidth = width
        self.screenheight = height
        #create the panes
        self.MainCanvas = Canvas(window, background = self.colour, width = self.screenwidth, height = self.screenheight)
        self.MainCanvas.pack()

        #This dictionary is used to keep track of an item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        #This dictionary is used to keep track of an item having it's state changed
        self._state_change = {"item": None, "tag": "PCchange1", "colour": "Black"}

        #This dictionary is used to keep track of the items being connected
        self._connector = {"connector": None, "item": None, "item2": None, "x": 0, "y": 0, "x2": 0, "y2": 0, "tag": "False"}

        self._object_data = []

        #Add bindings for clicking, dragging and releasing over any object with the "PCdrag" tag
        self.MainCanvas.tag_bind("PCdrag", "<ButtonPress-1>", self.OnButtonPress)
        self.MainCanvas.tag_bind("PCdrag", "<ButtonRelease-1>", self.OnButtonRelease)
        self.MainCanvas.tag_bind("PCdrag", "<B1-Motion>", self.OnMotion)

        self.MainCanvas.tag_bind("ColourSwitch", "<ButtonPress-3>", self.ColourChange)
        #self.MainCanvas.tag_bind("ColourSwitch", "<ButtonRelease-3>", self.ColourChangeRelease)
        #self.MainCanvas.tag_bind("PCchange", "<B3-Motion>", self.ColourChange)

        self.MainCanvas.tag_bind("text", "<Return>", self.OnEnter)

    #______________________________________________________________________________________________________________________________________________________________________

    def OnEnter(self, event):
        print 'hi'

    #______________________________________________________________________________________________________________________________________________________________________

    def ChangeClick(self):
        #This will change the binding of the mouse while the connector process is active
        self.MainCanvas.tag_bind("PCdrag", "<ButtonPress-1>", self.LocateObject)
        self.MainCanvas.tag_bind("PCdrag", "<ButtonRelease-1>", self.LocateObject2)
        self.MainCanvas.tag_bind("PCdrag", "<B1-Motion>", self.Ignore)

    #this is a temporary function to get rid of the OnMotion function which is usually called when the item is dragged
    def Ignore(self, event):
        a = 1
        #print "Ignore"
    #______________________________________________________________________________________________________________________________________________________________________

    #This is used to draw the computer on the canvas, notice the tag that has been added as an attribute
    def CreateComputer(self, x_start, y_start, color, tag):

        #count = count + 1
        #self._state_change["count"] = self._state_change["count"] + 1
        #Creates a list of tags that are going to be added on to each computer object
        #The second tag is defined elsewhere in the program as it changes depending on the state of the computer
        #tag = ["PCdrag", self._state_change["count"], self._state_change["tag"], "ColourSwitch", self._connector["tag"]]
        if temp <= temp2:
            self._object_data.append(dict(item=count, CoCount=0))

            #creates the object and takes properties from the DragItem class
            self.MainCanvas.create_rectangle(x_start-40, y_start-25, x_start+40, y_start+25, outline=color, fill=color, tags = ("PCdrag", self._state_change["tag"], "ColourSwitch", self._connector["tag"], tag))

            itemlist.append(self._state_change)
            #print itemlist
    #______________________________________________________________________________________________________________________________________________________________________

    #This is used to draw text on top of the object on the canvas
    def CreateText(self, x_start, y_start, Node, tag):
        global count
        global f
        global IPvar
        global temp
        global temp2

        IP = "192.168.0."

        if f == 0:
            temp2 = Node - 1
            #IPvar = (IPvar - Node) + 1
            #temp = IPvar
            temp = 1
            f = 1
        else:
            f = 1

        if temp <= temp2:
            self.MainCanvas.create_text(x_start, y_start, text = (IP, temp), fill = 'white', tag = ('PCdrag','text', tag))
            count = count + 1
            temp = temp + 1
        else:
            print 'fail'
    #______________________________________________________________________________________________________________________________________________________________________

    #this function will be called before the line is created. it sets all the variables for the line
    def CreateLine(self):
        global ConnectCount
        #sets the four variables that will determine the coords of the line
        xstart = self._connector["x"]
        ystart = self._connector["y"]
        xend = self._connector["x2"]
        yend = self._connector["y2"]

        #this will reset the _connector dictionary
        self._connector["x"] = 0
        self._connector["y"] = 0
        self._connector["x2"] = 0
        self._connector["y2"] = 0

        #this will set the tag bindings back to their original ones to allow you to drag the item again
        self.MainCanvas.tag_bind("PCdrag", "<ButtonPress-1>", self.OnButtonPress)
        self.MainCanvas.tag_bind("PCdrag", "<ButtonRelease-1>", self.OnButtonRelease)
        self.MainCanvas.tag_bind("PCdrag", "<B1-Motion>", self.OnMotion)

        #print self._object_data
        #tag = ["Linedrag", self._connector("item"), self._connector("item2")]

        #this will create the line and put it on the main canvas
        self.MainCanvas.create_line(xstart, ystart, xend , yend, tags = ("Linedrag", ConnectCount), width = 5, smooth = 1)
        self.MainCanvas.tag_raise("PCdrag")
        ConnectCount = ConnectCount + 1

    #______________________________________________________________________________________________________________________________________________________________________

    def LocateObject(self, event):
        global ConnectCount
        #sets the key "item" in the _connector dictionary to be equal to the object closest to the mouse
        #sets the key "x" and the key "y" to be equal to the x and y coords of the object
        self._connector["item"] = self.MainCanvas.find_closest(event.x, event.y)[0]

        if self._connector["item"] % 2 == 0:
            temp = self._connector["item"] / 2

            for d in range(len(self._object_data)):

                if self._object_data[d]["item"] == temp:

                    self._object_data[d]["CoCount"] = self._object_data[d]["CoCount"] + 1
                    self._object_data[d]["Connect" + str(self._object_data[d]["CoCount"])] = ConnectCount
            self._connector["item"] = self._connector["item"] - 1

        else:
            self._connector["item"] = self._connector["item"] + 1
            temp = self._connector["item"] / 2
            for d in range(len(self._object_data)):

                if self._object_data[d]["item"] == temp:

                    self._object_data[d]["CoCount"] = self._object_data[d]["CoCount"] + 1
                    self._object_data[d]["Connect" + str(self._object_data[d]["CoCount"])] = ConnectCount

            self._connector["item"] = self._connector["item"] - 1

        #print self._object_data, 'test1'

        self._connector["x"] = self.MainCanvas.coords(self._connector["item"])[0] + 40
        self._connector["y"] = self.MainCanvas.coords(self._connector["item"])[1] + 25
    #______________________________________________________________________________________________________________________________________________________________________

    def LocateObject2(self, event):
        global ConnectCount
        #sets the key "item" in the _connector dictionary to be equal to the object closest to the mouse
        #sets the key "x2" and the key "y2" to be equal to the x and y coords of the object
        #self._connector["connector"] = self.MainCanvas.find_closest(event.x, event.y)
        self._connector["item2"] = self.MainCanvas.find_closest(event.x, event.y)[0]

        if self._connector["item2"] % 2 == 0:
            temp = self._connector["item2"] / 2

            for d in range(len(self._object_data)):

                if self._object_data[d]["item"] == temp:

                    self._object_data[d]["CoCount"] = self._object_data[d]["CoCount"] + 1
                    self._object_data[d]["Connect" + str(self._object_data[d]["CoCount"])] = ConnectCount
            self._connector["item2"] = self._connector["item2"] - 1

        else:
            self._connector["item2"] = self._connector["item2"] + 1
            temp = self._connector["item2"] / 2
            for d in range(len(self._object_data)):

                if self._object_data[d]["item"] == temp:

                    self._object_data[d]["CoCount"] = self._object_data[d]["CoCount"] + 1
                    self._object_data[d]["Connect" + str(self._object_data[d]["CoCount"])] = ConnectCount

            self._connector["item2"] = self._connector["item2"] - 1

        #print self._object_data, 'test2'

        self._connector["x2"] = self.MainCanvas.coords(self._connector["item2"])[2] - 40
        self._connector["y2"] = self.MainCanvas.coords(self._connector["item2"])[3] - 25

        #an if statement to check whether the items are the same or if there is no item selected
        if self._connector["item"] != self._connector["item2"]:

            self._connector["tag"] = "True"

            #sets the tags of the objects again to compensate for the tag change in the if statements previously
            #tag = ["PCdrag", self._state_change["count"], self._state_change["tag"], "ColourSwitch", self._connector["tag"]]
            #tag = ["PCdrag", self._state_change["tag"], "ColourSwitch", self._connector["tag"]]

            #configures the items to change the tags of the items accordingly
            #self.MainCanvas.itemconfig(self._connector["item"], tags = tag)
            #self.MainCanvas.itemconfig(self._connector["item2"], tags = tag)
            self.CreateLine()

            self._connector["item"] = None
            self._connector["connector"] = None
            self._connector["item2"] = None
            self._connector["x"] = 0
            self._connector["y"] = 0
            self._connector["x2"] = 0
            self._connector["y2"] = 0


        elif self._connector["item"] and self._connector["item2"] == 0:
            self.Fail()
        else:
            self.Fail()
    #______________________________________________________________________________________________________________________________________________________________________
    #function that is called if the connector cannot be made
    def Fail(self):

        print 'Fail'

        self._connector = {"connector": None, "item": None, "item2": None, "x": 0, "y": 0, "x2": 0, "y2": 0, "tag": "False"}
        #this will set the tag bindings back to their original ones to allow you to drag the item again
        self.MainCanvas.tag_bind("PCdrag", "<ButtonPress-1>", self.OnButtonPress)
        self.MainCanvas.tag_bind("PCdrag", "<ButtonRelease-1>", self.OnButtonRelease)
        self.MainCanvas.tag_bind("PCdrag", "<B1-Motion>", self.OnMotion)

    #______________________________________________________________________________________________________________________________________________________________________

    #This uses the find_closest method to get store the x and y positions of the nearest item into the dictionary
    def OnButtonPress(self, event):
        global itemsconnectors
        global a

        def Search(a):
            for d in range(len(self._object_data)):
                print 'hi1'
                print self._object_data
                if a in self._object_data[d]:
                    print 'hi'

##        def Search():
##            for d in range(len(a)):
##                if 15 in a[d]["CoCount"]:
##                    print 'hi'
##                else:
##                    print 'fail'

        p = 0
        item = self.MainCanvas.find_closest(event.x, event.y)[0]
        tags = self.MainCanvas.gettags(item)
        for tag in tags:
            if tag.startswith("circle-"):
                break
        self._drag_data["item"] = tag
        '''Begin drag of an object'''
        # record the item and its location
        #self._drag_data["item"] = self.MainCanvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

        if item % 2 == 0:
            item = item / 2

        #runs for loop for the amount of nodes on screen
        for d in range(len(self._object_data)):
                #checks to find the current items dictionary
                if self._object_data[d]["item"] == item:
                    #checks if the item has a connector
                    if self._object_data[d]["CoCount"] > 0:
                        #sets the amount of connectors the object has
                        connectors = len(self._object_data[d]) - 2
                        #runs a loop for the amount of connectors it has
                        for i in range(connectors):
                            #sets a to be equal to the current connector in the loop
                            a = self._object_data[d]["Connect" + str(i + 1)]
                            #prints the coords of the current connector
                            print self.MainCanvas.coords(len(itemlist) + a)
                            #appends that connector to a list
                            itemsconnectors.append(a)
                            print itemsconnectors
                            #runs loop for the amount of nodes on screen
                            for o in range(len(self._object_data)):
                                #LinkedItems.append(Search(self._object_data[d], a))
                                #checks if each node is connected to current connector
                                LinkedItems.append(Search(a))

                    else:
                        print 'No Connectors'

        #print LinkedItems

        #print itemlist
        #print list(self.MainCanvas.gettags(self.MainCanvas.find_closest(event.x, event.y)))


    #______________________________________________________________________________________________________________________________________________________________________

    #This clears the dictionary once the mouse button has been released
    def OnButtonRelease(self, event):
        '''End drag of an object'''
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    #______________________________________________________________________________________________________________________________________________________________________

    def OnMotion(self, event):

        b = len(self._object_data) + a

        '''Handle dragging of an object'''
        # compute how much this object has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.MainCanvas.move(self._drag_data["item"], delta_x, delta_y)
        #self.MainCanvas.coords(b, 10, 10 ,100 ,100)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    #______________________________________________________________________________________________________________________________________________________________________

    def Delete_Object(self):
        global IPvar
        temp = IPvar

        #deletes all the objects on the canvas
        self.MainCanvas.delete('all')

        #This dictionary is used to keep track of an item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        #This dictionary is used to keep track of an item having it's state changed
        self._state_change = {"item": None, "tag": "PCchange1", "colour": "Black"}

        #This dictionary is used to keep track of the items being connected
        self._connector = {"connector": None, "item": None, "item2": None, "x": 0, "y": 0, "x2": 0, "y2": 0, "tag": "False"}

        self._data_store = {"item": None, "tag": self._state_change["tag"]}
    #______________________________________________________________________________________________________________________________________________________________________

    def ColourChange(self, event):

        #sets the key "item" in the _state_change dictionaryto be equal to the object closest to the mouse
        self._state_change["item"] = self.MainCanvas.find_closest(event.x, event.y)[0]

        #a set of if statements to check what the current object colour is and change it depending on its colour
        if self._state_change["colour"] == "Black":
            self._state_change["colour"] = "Red"
            #changes the tag of the object to reflect what colour it is
            #this will then be used to set the PC to be either a sender, receiver or a router
            self._state_change["tag"] = "PCchange2"

        elif self._state_change["colour"] == "Red":
            self._state_change["colour"] = "Blue"
            self._state_change["tag"] = "PCchange3"

        elif self._state_change["colour"] == "Blue":
            self._state_change["colour"] = "Black"
            self._state_change["tag"] = "PCchange1"
        #an else for error checking. incase none of the if statements work
        else:
            print "Error"

        #sets the tags of the objects again to compensate for the tag change in the if statements previously
        #tag = ["PCdrag", self._state_change["count"], self._state_change["tag"], "ColourSwitch", self._connector["tag"]]
        #tag = ["PCdrag", self._state_change["tag"], "ColourSwitch", self._connector["tag"]]
        #configures the items to change the colour and the tags of the items accordingly
        self.MainCanvas.itemconfig(self._state_change["item"], fill = self._state_change["colour"])
        #print self.MainCanvas.gettags(self.MainCanvas.find_closest(event.x, event.y))
#______________________________________________________________________________________________________________________________________________________________________

class DragItem:
    #Constructor
    #Initiates when the class is called
    #all the arguements are passed through
    #the aruements have pre-set values that can be over written incase the program doesnt get passed anything
    def __init__(self, window, width=100, height=100, colour="black", x_start=0, y_start=0, node = 5):
        #window variables
        self.window = window
        tag = "circle-%d" % id(self)
        #calls a method to create the computer object
        self.circle = self.window.CreateComputer(x_start, y_start, colour, tag)
        self.circle_text = self.window.CreateText(x_start, y_start, node, tag)

class Connector:
    #Constructor
    #Initiates when the class is called
    #all the arguements are passed through
    #the aruements have pre-set values that can be over written incase the program doesnt get passed anything
    def __init__(self, window):
        #window variables
        self.window = window
        self.window.ChangeClick()