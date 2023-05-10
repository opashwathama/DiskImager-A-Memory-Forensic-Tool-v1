import wx
import wx.xrc
import psutil
from hurry.filesize import size,si,iec
import os,sys
import math
import hashlib

###########################################################################
## Drive Information
###########################################################################

path1=""

class Info ( wx.Frame ):
	hash1=""
	type1=""
	size1=""
	file1=""
	pndrv1=""
	psize=0
	dfree=0
	dsp=0
	path1=""
	psize1=0
	dsp1=0
	hasher = hashlib.md5()
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Drive Information", pos = wx.DefaultPosition, size = wx.Size( 500,211 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		#self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.wx.SYS_COLOUR_WINDOWFRAME) )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lab1 = wx.StaticText( self, wx.ID_ANY, u"Select Your Drive", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lab1.Wrap( -1 )
		self.lab1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.lab1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		combo1Choices = [ u"Select Your Disk" ]
		self.combo1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), combo1Choices, 0 )
		self.combo1.SetSelection( 0 )
		self.combo1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.combo1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		#Set Available ComboBox Value
		val=[" Please Select "]
		temp=[" "]
		f = os.popen ("df -h")
		for i in f.readlines():
			temp=i.split( )
			if temp[0].startswith("/"):
				val.append(temp[0]+" Size: "+temp[1])
				if temp[5].startswith("/media/root/"):
					inti=temp[1].split("G")
					psize=0
					dsp=0
					if type(inti) is int:
						psize=math.ceil(int(inti[0]))
						
					if type(inti) is float:
						psize=math.ceil(inti[0])
					# psize=math.ceil(inti[0])
					
					inti=temp[3].split("G")
					if type(inti) is int:
						dsp=math.floor(int(inti[1]))
					if type(inti) is float:
						dsp=math.floor(int(inti[1]))
					
					if (cmp(psize,dsp)==-1):
						dfree=math.floor(temp[3].split("G"))
						path1=temp[0]
				
		self.combo1.SetItems(val)
			
		#combo1= wx.combo1(self, choices=val)
		#End Set Value

		
		
		self.button1 = wx.Button( self, wx.ID_ANY, u"Generate Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.button1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.alert1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alert1.Wrap( -1 )
		self.alert1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.alert1.Enable( False )
##		
		gSizer1.Add( self.alert1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.combo1.Bind( wx.EVT_COMBOBOX, self.comb1 )
		self.button1.Bind( wx.EVT_BUTTON, self.callcreate )
	
	def __del__( self ):
		pass
		
		
	# Virtual event handlers, overide them in your derived class
	def comb1( self, event ):
		data=self.combo1.GetValue()
		temp=data.split( )
		pndrv1=temp[0]
		#self.alert1.SetLabel("Size of A Disk Is: "+pndrv1)
		
		event.Skip()
	
	
	def callcreate( self, event ):
		
		data=self.combo1.GetValue()
		temp=data.split( )
		if data=="":
			self.alert1.SetLabel("Please Select Infromation")
		else:	
			self.alert1.SetLabel("Generating Information")
			Drive=self.combo1.GetValue()
			self.alert1.SetLabel("Selected Value Is: "+Drive)
			
		event.Skip()
def call():
	ex = wx.App()
	Info(None).Show()
	ex.MainLoop()
	pass
