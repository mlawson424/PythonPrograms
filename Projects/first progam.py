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
class MyFrame (wx.Frame):
    #Deriving a new class of Frame
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(-1,-1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() #A Statusbar in the bottom of the window

        #Setting up the menu
        filemenu = wx.Menu()

        #wx.ID_ABOUT and wx.ID_EXIT are standard IDs
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About","Information about this program")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Exit this program")

        #Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File") #Adding Filemenu to the MenuBar
        self.SetMenuBar(menuBar) #Adding the menubar to the frame content

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
#frame.Show(True) #Show the frame
app.MainLoop()
