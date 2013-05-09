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
        filemenu.Append(wx.ID_ABOUT, "&About","Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit","Exit this program")

        #Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File") #Adding Filemenu to the MenuBar
        self.SetMenuBar(menuBar) #Adding the menubar to the frame content
        self.Show(True)

app = wx.App(False) #Create a new app, don't redirect stdout/stderr to a window
frame = MyFrame(None, "First Program") #A Frame is a top-level window
#frame.Show(True) #Show the frame
app.MainLoop()
