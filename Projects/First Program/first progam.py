#-------------------------------------------------------------------------------
# Name:        First program
# Purpose:     To Design my first program and learn python
#
# Author:      Matt Lawson
#
# Created:     05/08/2013
# Copyright:   (c) Matt Lawson 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/env python
import wx
ART_SETTINGS = wx.NewId()
ART_HOME = wx.NewId()

class MyProvider(wx.ArtProvider):
    #Creating a New Art Provider for Images
    def __init__(self):
        wx.ArtProvider.__init__(self)
    def CreateBitmap(self, id, client, size):
        if (id == "ART_SETTINGS"):
            return wx.Bitmap("settings.png")
        if (id == "ART_HOME"):
            return wx.Bitmap("home.png")
        if (id == "ART_CALENDAR"):
            return wx.Bitmap("clock.png")
    app = wx.App(False)
    app.MainLoop()

wx.ArtProvider.Push(MyProvider())

FRAMETB = True
TBFLAGS = (wx.TB_VERTICAL | wx.TB_TEXT | wx.NO_BORDER | wx.TB_NODIVIDER)

class MyFrame (wx.Frame):
    #Deriving a new class of Frame
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1500, 800))

        #Setting up the menu
        filemenu = wx.Menu()
        helpmenu = wx.Menu()

        #wx.ID_ABOUT and wx.ID_EXIT are standard IDs
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About","Information about this program")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Exit this program")

        #Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File") #Adding Filemenu to the MenuBar
        menuBar.Append(helpmenu, "&Help") #Adding Help to the menu bar
        self.SetMenuBar(menuBar) #Adding the menubar to the frame content

        #Creating the Tool bar
        client = wx.Panel(self)
        client.SetBackgroundColour(wx.NamedColor("GREY"))

        if FRAMETB:
            tb = self.CreateToolBar(TBFLAGS)
        else:
            tb = wx.ToolBar(client, style = TBFLAGS)
            sizer = wx.BoxSizer(wx.HORIZONTAL)
            sizer.Add(tb, -1, wx.EXPAND)
            client.SetSizer(sizer)

        self.CreateStatusBar() #A Statusbar in the bottom of the window

        #Pull Images from Art Provider
        tsize = (52, 52)
        home = wx.ArtProvider.GetBitmap("ART_HOME", wx.ART_TOOLBAR, tsize)
        calendar = wx.ArtProvider.GetBitmap("ART_CALENDAR", wx.ART_TOOLBAR, tsize)
        settings = wx.ArtProvider.GetBitmap("ART_SETTINGS", wx.ART_TOOLBAR, tsize)

        #Add the Tools to the Bar
        tb.AddSimpleTool(1, home, "Home")
        tb.AddSimpleTool(2, calendar, "Calendar")
        tb.AddSimpleTool(10, settings, "Settings")

        #Render Tool bar
        tb.Realize()

        #Create Events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.Show(True)

    def OnAbout(self,e):
        #A message with dialog box OK
        dlg = wx.MessageDialog(self, "Created By Matt Lawson", "Small Text Editor", wx.OK)
        dlg.ShowModal() #Show it
        dlg.Destroy() #Destroy frame after finishing

    def OnExit(self,e):
        self.Close(True) #Close the frame

    def OnOpen(self,e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


app = wx.App(False) #Create a new app, don't redirect stdout/stderr to a window
frame = MyFrame(None, "First Program") #A Frame is a top-level window
app.MainLoop()
