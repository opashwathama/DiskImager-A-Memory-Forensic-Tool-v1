# -*- coding: utf-8 -*- 

import wx
import wx.xrc
# import info
import hashes
import testdialouge
import cif
Home = 1000
createimagefile = 1001
hash = 1002
exit = 1003
info = 1004
help = 1005

###########################################################################
## Class MemoryForensicImager
###########################################################################
## Disk imaging is the process of copying the contents of a drive and storing it into a single compressed file. Many distinct types of disc images exist. They can be used for backing up files, creating virtual computers in a hypervisor (VMWare, Hyper-V, etc.), as well as for systems deployment.

class MemoryForensicImager ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = Home, title = u"Disk Imaging Tool", pos = wx.Point( 450,450 ), size = wx.Size( 641,523 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Welcome To Disk Imaging Tool", wx.Point( -1,500 ), wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_SLANT, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		
		bSizer2.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap("LOGO1.PNG", wx.BITMAP_TYPE_ANY ), wx.Point( 500,500 ), wx.Size( 700,800 ), 0 )
		bSizer2.Add( self.m_bitmap1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.createImagefile = wx.MenuItem( self.file, createimagefile, "&Create Imagefile\tCtrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.createImagefile )
		
		self.hash = wx.MenuItem( self.file, hash, "&Hash\tCtrl+H", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.hash )
		
		
		self.exit = wx.MenuItem( self.file, exit, "&Quit\tCtrl+E", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.exit )
		
		
		
		self.m_menubar1.Append( self.file, u"File" ) 
		
		self.disk = wx.Menu()
		self.info = wx.MenuItem( self.disk, info, "&Info\tCtrl+I", wx.EmptyString, wx.ITEM_NORMAL )
		self.disk.AppendItem( self.info )
		
		
		self.m_menubar1.Append( self.disk, u"Disk" ) 
		
		self.about = wx.Menu()
		self.help = wx.MenuItem( self.about, help, "&Help\tCtrl+H", wx.EmptyString, wx.ITEM_NORMAL )
		self.about.AppendItem( self.help )
		
		self.m_menubar1.Append( self.about, u"About" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		self.Bind( wx.EVT_MENU, self.createimagefile, id = self.createImagefile.GetId() )
		self.Bind( wx.EVT_MENU, self.Hash, id = self.hash.GetId() )
		self.Bind( wx.EVT_MENU, self.Exit, id = self.exit.GetId() )
		
		self.Bind( wx.EVT_MENU, self.Info, id = self.info.GetId() )
		self.Bind( wx.EVT_MENU, self.Help, id = self.help.GetId() )
		
	def __del__( self ):
		pass
	
	def createimagefile(self,event):
		cif.showCIF()
		pass
	def Hash(self,event):
		hashes.ShowHashes()
		pass
	def Exit( self, event ):
		self.Close()
		pass
	def Info(self,event):
		#callinfo(a)
		testdialouge.call()	
		pass
	def Help(self,event):
		
		pass
	



ex = wx.App()
MemoryForensicImager(None).Show()
ex.MainLoop()


	
