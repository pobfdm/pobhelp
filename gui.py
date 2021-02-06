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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PobHelp", pos = wx.DefaultPosition, size = wx.Size( 318,540 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Ubuntu" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"lifesaver.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.logo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2.SetMinSize( wx.Size( -1,60 ) )
		self.chkListen = wx.CheckBox( self, wx.ID_ANY, u"Give help", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.chkListen, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.chkVpnMode = wx.CheckBox( self, wx.ID_ANY, u"VPN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkVpnMode.SetToolTip( u"VPN upd" )

		bSizer2.Add( self.chkVpnMode, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

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
		self.mnuItemStartVpnClient = wx.MenuItem( self.mnuVpn, wx.ID_ANY, u"Vpn client/server", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuVpn.Append( self.mnuItemStartVpnClient )

		self.m_menubar1.Append( self.mnuVpn, u"Vpn" )

		self.mnuServers = wx.Menu()
		self.mnuFTPserver = wx.MenuItem( self.mnuServers, wx.ID_ANY, u"FTP server", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuServers.Append( self.mnuFTPserver )

		self.m_menubar1.Append( self.mnuServers, u"Servers" )

		self.mnuTools = wx.Menu()
		self.mnuItemBlackboard = wx.MenuItem( self.mnuTools, wx.ID_ANY, u"Blackboard", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuTools.Append( self.mnuItemBlackboard )

		self.m_menubar1.Append( self.mnuTools, u"Tools" )

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
		self.Bind( wx.EVT_MENU, self.runFTPDdialog, id = self.mnuFTPserver.GetId() )
		self.Bind( wx.EVT_MENU, self.showBlackboard, id = self.mnuItemBlackboard.GetId() )
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

	def runFTPDdialog( self, event ):
		event.Skip()

	def showBlackboard( self, event ):
		event.Skip()

	def onAbout( self, event ):
		event.Skip()


###########################################################################
## Class TdlgVpnClient
###########################################################################

class TdlgVpnClient ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Vpn manager", pos = wx.DefaultPosition, size = wx.Size( 703,367 ), style = wx.DEFAULT_DIALOG_STYLE )

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

		bSizerInfo = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"To make the vpn safe, regenerate the \"static.key\" security key (openvpn).", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText10.SetLabelMarkup( u"To make the vpn safe, regenerate the \"static.key\" security key (openvpn)." )
		self.m_staticText10.Wrap( -1 )

		bSizerInfo.Add( self.m_staticText10, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( bSizerInfo, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

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
		self.txtVpn.Bind( wx.EVT_TEXT, self.onText )
		self.txtVpn.Bind( wx.EVT_TEXT_ENTER, self.onText )
		self.btCancel.Bind( wx.EVT_BUTTON, self.stopProcess )
		self.btConnect.Bind( wx.EVT_BUTTON, self.setConn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onText( self, event ):
		event.Skip()


	def stopProcess( self, event ):
		event.Skip()

	def setConn( self, event ):
		event.Skip()


###########################################################################
## Class TdlgFTPD
###########################################################################

class TdlgFTPD ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 691,462 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizerUserPassword = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"User:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizerUserPassword.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.entryUser = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerUserPassword.Add( self.entryUser, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizerUserPassword.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.entryPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizerUserPassword.Add( self.entryPassword, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( bSizerUserPassword, 1, wx.EXPAND, 5 )

		bSizerPortAndRoot = wx.BoxSizer( wx.HORIZONTAL )

		self.lblPort = wx.StaticText( self, wx.ID_ANY, u"Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPort.Wrap( -1 )

		bSizerPortAndRoot.Add( self.lblPort, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.entryPort = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerPortAndRoot.Add( self.entryPort, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Root folder:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizerPortAndRoot.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.dirPkrFTPRoot = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_CHANGE_DIR|wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST|wx.DIRP_SMALL|wx.DIRP_USE_TEXTCTRL )
		bSizerPortAndRoot.Add( self.dirPkrFTPRoot, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( bSizerPortAndRoot, 1, wx.EXPAND, 5 )

		bSizerOutput = wx.BoxSizer( wx.VERTICAL )

		self.txtOutput = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.txtOutput.SetMinSize( wx.Size( -1,500 ) )

		bSizerOutput.Add( self.txtOutput, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer6.Add( bSizerOutput, 1, wx.EXPAND, 5 )

		bSizerStartStop = wx.BoxSizer( wx.HORIZONTAL )

		self.btStop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btStop.Enable( False )

		bSizerStartStop.Add( self.btStop, 1, wx.ALL, 5 )

		self.btStart = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btStart.SetDefault()
		bSizerStartStop.Add( self.btStart, 1, wx.ALL, 5 )


		bSizer6.Add( bSizerStartStop, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.txtOutput.Bind( wx.EVT_TEXT, self.onText )
		self.btStop.Bind( wx.EVT_BUTTON, self.stopServer )
		self.btStart.Bind( wx.EVT_BUTTON, self.startServer )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onText( self, event ):
		event.Skip()

	def stopServer( self, event ):
		event.Skip()

	def startServer( self, event ):
		event.Skip()


###########################################################################
## Class TfrmBlackboard
###########################################################################

class TfrmBlackboard ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Blackboard", pos = wx.DefaultPosition, size = wx.Size( 682,507 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizerTxtBlackboard = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Write here:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizerTxtBlackboard.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.txtBlackboard = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.txtBlackboard.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizerTxtBlackboard.Add( self.txtBlackboard, 1, wx.EXPAND |wx.ALL, 5 )

		self.btClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerTxtBlackboard.Add( self.btClose, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizerTxtBlackboard )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onclose )
		self.btClose.Bind( wx.EVT_BUTTON, self.onclose )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onclose( self, event ):
		event.Skip()



