import wx
import wx.xrc
import psutil
from hurry.filesize import size,si,iec
import os,sys
import math
import hashlib

###########################################################################
## Class CreateImageFile
###########################################################################

path1=""

class CreateImageFile ( wx.Frame ):
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Create Image File", pos = wx.DefaultPosition, size = wx.Size( 500,211 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lab1 = wx.StaticText( self, wx.ID_ANY, u"Available", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lab1.Wrap( -1 )
		self.lab1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.lab1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		combo1Choices = [ u"Select Your Disk" ]
		self.combo1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), combo1Choices, 0 )
		self.combo1.SetSelection( 0 )
		self.combo1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.combo1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		#Set Available ComboBox Value
		val=["Select Your Disk"]
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

		
		self.lab2 = wx.StaticText( self, wx.ID_ANY, u"Image Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lab2.Wrap( -1 )
		self.lab2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.lab2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		combo2Choices = [ u"Select Available", u"Bit-By-Bit"]
		self.combo2 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, combo2Choices, 0 )
		self.combo2.SetSelection( 0 )
		self.combo2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.combo2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lab3 = wx.StaticText( self, wx.ID_ANY, u"Hash", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lab3.Wrap( -1 )
		self.lab3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.lab3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		combo3Choices = [ u"Select Hash", u"MD5", u"SHA1" ]
		self.combo3 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, combo3Choices, 0 )
		self.combo3.SetSelection( 0 )
		self.combo3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.combo3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.button1 = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.button1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.button2 = wx.Button( self, wx.ID_ANY, u"Generate Hash", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.alert1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alert1.Wrap( -1 )
		self.alert1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.alert1.Enable( False )
		
		gSizer1.Add( self.alert1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.combo1.Bind( wx.EVT_COMBOBOX, self.comb1 )
		self.combo2.Bind( wx.EVT_COMBOBOX, self.comb2 )
		self.combo3.Bind( wx.EVT_COMBOBOX, self.comb3 )
		self.button1.Bind( wx.EVT_BUTTON, self.callcreate )
		self.button2.Bind( wx.EVT_BUTTON, self.callcancel )
	
	def __del__( self ):
		pass
		
		
	# Virtual event handlers, overide them in your derived class
	def comb1( self, event ):
		data=self.combo1.GetValue()
		temp=data.split( )
		pndrv1=temp[0]
		#self.alert1.SetLabel("Size of A Disk Is: "+pndrv1)
		
		event.Skip()
	

	def comb2( self, event ):
		type1=self.combo2.GetValue()
		#self.alert1.SetLabel("Selected Value Is: "+type1)
		event.Skip()
	def comb3( self, event ):
		#self.alert1.SetLabel("Selected Value Is: "+self.combo3.GetValue())
		hash1=self.combo3.GetValue()
		event.Skip()
	#Code For Creating ImageFile
	def callcreate( self, event ):
		self.alert1.SetLabel("Creating Imagefile..Please Wait.")
		data=self.combo1.GetValue()
		temp=data.split( )
		pndrv1=temp[0]
		path1="/home"
		hash1=self.combo3.GetValue()
		type1=self.combo2.GetValue()
		#self.alert1.SetLabel("Size of A Pandrive Is: "+pndrv1)
		#self.alert1.SetLabel(" Values: "+path1)
		if hash1=="":
			self.alert1.SetLabel("Please Select All Values")
		elif type1=="":
			self.alert1.SetLabel("Please Select All Values")
		elif pndrv1=="":
			self.alert1.SetLabel("Please Select All Values")
		else:	
			self.alert1.SetLabel("Creating Imagefile..Please Wait.")
			type1=self.combo2.GetValue()
			self.alert1.SetLabel("Selected Value Is: "+type1)
			file="PandriveImage"+"."+type1
			with open(pndrv1,'rb+') as f:
				
				f.seek(0,2)
				point1=f.tell()
				size1=size(point1,system=si)
				f.seek(0,0)
				self.alert1.SetLabel(os.getcwd())
				#os.chdir(path1+"/root/Desktop/")
				os.chdir(path1)
				#if os.path.isdir(path1+"/root/Desktop/Dumps"):
					#os.chdir(path1+"/root/Desktop/Dumps/")
				#else:
				#	os.mkdir("Dumps")
				#	os.chdir(path1+"/root/Desktop/Dumps/")
				#self.alert1.SetLabel(os.getcwd())
				#if os.path.exists(path1+"/root/Desktop/Dumps/PandriveImage.*"):
				#	file="PandriveImage"+type1+"."+type1
				if os.path.isdir(path1+"/Dumps"):
					os.chdir(path1+"/Dumps")
				else:
					os.mkdir("Dumps")
					os.chdir(path1+"/Dumps")
				self.alert1.SetLabel(os.getcwd())
				if os.path.exists(path1+"/Dumps/PandriveImage.*"):
					file="PandriveImage"+type1+"."+type1
				
    				with open(file, "wb+") as i:
					self.alert1.SetLabel("Creating Imagefile..Please Wait.")
     					while True:
						i.write(f.read(1024))
						point2 = i.tell()
						size2 = size(point2,system=iec)
     						if i.write(f.read(1024)) == 0:
							self.alert1.SetLabel("Image File Created Successfully")
    							break
						if size1==size2:
    							self.alert1.SetLabel("Image File Created Successfully")
							break
				f.close()
				i.close()
				self.Close()
				
		event.Skip()
	def callcancel( self, event ):
		self.alert1.SetLabel("Generating Hashfile..Please Wait.")
		data=self.combo1.GetValue()
		temp=data.split( )
		pndrv1=temp[0]
		path1="/home"
		hash1=self.combo3.GetValue()
		type1=self.combo2.GetValue()
		#self.alert1.SetLabel("Size of A Pandrive Is: "+pndrv1)
		#self.alert1.SetLabel(" Values: "+path1)
		if hash1=="":
			self.alert1.SetLabel("Please Select All Values")
		elif type1=="":
			self.alert1.SetLabel("Please Select All Values")
		elif pndrv1=="":
			self.alert1.SetLabel("Please Select All Values")
		else:	
			self.alert1.SetLabel("Generating Hashfile..Please Wait.")
			type1=self.combo2.GetValue()
			self.alert1.SetLabel("Selected Value Is: "+type1)
			file="PandriveImage"+".img"
			MD5= hashlib.md5()
			SHA1=hashlib.sha1()
			with open(pndrv1,'rb') as f:
				while True:
					readfile=f.read(65536)
					if not readfile:
						break
					MD5.update(readfile)
					SHA1.update(readfile)

				md5hash=MD5.hexdigest()
				sha1hash=SHA1.hexdigest()
				self.alert1.SetLabel(md5hash +" and "+sha1hash)
				#os.chdir(path1+"/root/Desktop/")
				os.chdir(path1)
				#if os.path.isdir(path1+"/root/Desktop/Dumps"):
					#os.chdir(path1+"/root/Desktop/Dumps/")
				#else:
				#	os.mkdir("Dumps")
				#	os.chdir(path1+"/root/Desktop/Dumps/")
				#self.alert1.SetLabel(os.getcwd())
				#if os.path.exists(path1+"/root/Desktop/Dumps/PandriveImage.*"):
				#	file="PandriveImage"+type1+"."+type1
				if os.path.isdir(path1+"/Dumps"):
					os.chdir(path1+"/Dumps")
				else:
					os.mkdir("Dumps")
					os.chdir(path1+"/Dumps")
				self.alert1.SetLabel(os.getcwd())
				if os.path.exists(path1+"/Dumps/PandriveImage.*"):
					file1="PandriveImage"+type1+"."+type1
    				with open(file1, "rb") as i:
					while True:
						readfile=i.read(65536)
						if not readfile:
							break
						MD5.update(readfile)
						SHA1.update(readfile)

					md5hash1=MD5.hexdigest()
					sha1hash1=SHA1.hexdigest()
					self.alert1.SetLabel(md5hash1 +" and "+sha1hash1)
					filename=pndrv1+"hash.txt"
					with open(filename,"w+") as hf:
						hf.write("MD5 Hash For "+pndrv1+" File Is: "+md5hash)
						hf.write("SHA1 Hash For "+pndrv1+" File Is: "+sha1hash)
						hf.write("MD5 Hash For "+file1+" File Is: "+md5hash1)
						hf.write("SHA1 Hash For "+file1+" File Is: "+sha1hash1)
		self.Close()				
		event.Skip()
def showCIF():
	ex = wx.App()
	CreateImageFile(None).Show()
	ex.MainLoop()
	pass
