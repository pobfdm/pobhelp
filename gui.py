# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 21 2021)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class TPobhelpGui
###########################################################################

class TPobhelpGui ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PobHelp", pos = wx.DefaultPosition, size = wx.Size( 318,507 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"lifesaver.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.logo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.chkListen = wx.CheckBox( self, wx.ID_ANY, u"Give help", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.chkListen, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		self.lblHost = wx.StaticText( self, wx.ID_ANY, u"Hostname", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.lblHost.Wrap( -1 )

		bSizer1.Add( self.lblHost, 0, wx.ALL, 5 )

		self.entryHost = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer1.Add( self.entryHost, 0, wx.ALL|wx.EXPAND, 5 )

		self.lblPort = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPort.Wrap( -1 )

		bSizer1.Add( self.lblPort, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.entryPort = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.entryPort, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btConnect = wx.Button( self, wx.ID_ANY, u"<b>Connect</b>", wx.DefaultPosition, wx.Size( 200,60 ), 0 )
		self.btConnect.SetLabelMarkup( u"<b>Connect</b>" )
		bSizer1.Add( self.btConnect, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btDisconnect = wx.Button( self, wx.ID_ANY, u"<b>Disconnect</b>", wx.DefaultPosition, wx.Size( 200,60 ), 0 )
		self.btDisconnect.SetLabelMarkup( u"<b>Disconnect</b>" )
		bSizer1.Add( self.btDisconnect, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.statusBar.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.mnuFile = wx.Menu()
		self.manuItemQuit = wx.MenuItem( self.mnuFile, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuFile.Append( self.manuItemQuit )

		self.m_menubar1.Append( self.mnuFile, u"File" )

		self.mnuVpn = wx.Menu()
		self.mnuItemStartVpnClient = wx.MenuItem( self.mnuVpn, wx.ID_ANY, u"Start a vpn ", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuVpn.Append( self.mnuItemStartVpnClient )

		self.m_menubar1.Append( self.mnuVpn, u"Vpn" )

		self.mnuHelp = wx.Menu()
		self.mnuItemAbout = wx.MenuItem( self.mnuHelp, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuHelp.Append( self.mnuItemAbout )

		self.m_menubar1.Append( self.mnuHelp, u"Help" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.quit )
		self.chkListen.Bind( wx.EVT_CHECKBOX, self.chkListenClicked )
		self.btConnect.Bind( wx.EVT_BUTTON, self.connect )
		self.btDisconnect.Bind( wx.EVT_BUTTON, self.disconnect )
		self.Bind( wx.EVT_MENU, self.quit, id = self.manuItemQuit.GetId() )
		self.Bind( wx.EVT_MENU, self.runVpnClient, id = self.mnuItemStartVpnClient.GetId() )
		self.Bind( wx.EVT_MENU, self.onAbout, id = self.mnuItemAbout.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def quit( self, event ):
		event.Skip()

	def chkListenClicked( self, event ):
		event.Skip()

	def connect( self, event ):
		event.Skip()

	def disconnect( self, event ):
		event.Skip()


	def runVpnClient( self, event ):
		event.Skip()

	def onAbout( self, event ):
		event.Skip()


###########################################################################
## Class TdlgVpnClient
###########################################################################

class TdlgVpnClient ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"VpnClient", pos = wx.DefaultPosition, size = wx.Size( 703,367 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Host", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.entryHostVpn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.entryHostVpn, 1, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.entryPortVpn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.entryPortVpn, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )

		self.txtVpn = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer3.Add( self.txtVpn, 1, wx.EXPAND |wx.ALL, 5 )

		self.chkServerMode = wx.CheckBox( self, wx.ID_ANY, u"Server mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.chkServerMode, 0, wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.btCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btCancel, 1, wx.ALL, 5 )

		self.btConnect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btConnect.SetDefault()
		bSizer5.Add( self.btConnect, 1, wx.ALL, 5 )


		bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btCancel.Bind( wx.EVT_BUTTON, self.stopProcess )
		self.btConnect.Bind( wx.EVT_BUTTON, self.setConn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def stopProcess( self, event ):
		event.Skip()

	def setConn( self, event ):
		event.Skip()


