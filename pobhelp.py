#!/usr/bin/env python3

import wx,wx.html,sys
from gui import *
from ftpd import *
from vncd import *
from guiUtils import *
import subprocess,os, urllib3 ,threading, ctypes,socket,time

# Python deps: wxpython4, urllib3, pyftpdlib, psutil(only win32)
# Linux deps: x11vnc,tigervnc,openvpn,pkexec(polkit)
# Windows deps: all included in bundle

VERSION="0.1"

import locale, gettext

try:
	current_locale, encoding = locale.getdefaultlocale()
	locale_path = getScriptDir()+os.sep+'locale'+os.sep
	language = gettext.translation ('pobhelp', locale_path, [current_locale] )
	_ = gettext.gettext
	language.install()

except:
	_ = gettext.gettext



def find_procs_by_name(name):
	import psutil
	ls = []
	for p in psutil.process_iter(['name']):
		if p.info['name'] == name:
			ls.append(p)
	return ls


def getConfigDirPath():
	from os.path import expanduser
	home = expanduser("~")
	if sys.platform == 'win32': 
		configDir=home+"\\AppData\\Local\\pobhelp\\"
	elif  sys.platform == 'linux':
		configDir=home+"/.config/pobhelp/"
	elif sys.platform== "darwin":
		configDir=home+"/.config/pobhelp/"	
	else:
		configDir=home+"/.config/pobhelp/"
	
	return configDir

def getHomePath():
	from os.path import expanduser
	home = expanduser("~")
	if sys.platform == 'win32': 
		configDir=home
	elif  sys.platform == 'linux':
		configDir=home
	elif sys.platform== "darwin":
		configDir=home
	else:
		configDir=home
	
	return configDir 	 

def getScriptDir():
	if getattr(sys, 'frozen', False):
		return sys._MEIPASS
	else:
		return os.path.dirname(os.path.abspath(__file__))



class frmblackboard(TfrmBlackboard):
	
	def onclose(self,evt):
		self.Hide()


		

class dialogVpnClient(TdlgVpnClient):
	host=None
	port=None
	p=None
	
	
	def onText(self,evt):
		p=self.txtVpn.GetCaretPosition()
		self.txtVpn.ScrollIntoView(p,wx.WXK_END)

	
	def stopProcess(self,evt):
		if (os.name=="posix"):
			os.system("pkexec kill -9 "+str(self.p.pid) )
		elif (os.name=="nt"):
			os.system("taskkill /T /F /pid "+str(self.p.pid))
			
	def runProcessPosix(self,cmd):
		self.p=subprocess.Popen(cmd, bufsize=0 ,stdout=subprocess.PIPE)
		wx.CallAfter(self.btConnect.Enable, False)
		while self.p.poll() is None :
			out = self.p.stdout.readline().decode("utf-8")
			if (out) :
				wx.CallAfter(self.txtVpn.WriteText,out)
				
		
		wx.CallAfter(self.btConnect.Enable, True)
		wx.CallAfter(self.txtVpn.WriteText,"*** VPN terminated. ***")
	
	def runProcessWin(self,cmd):
		self.p=subprocess.Popen(cmd, shell=True,bufsize=0 ,stdout=subprocess.PIPE)
		wx.CallAfter(self.btConnect.Enable, False)
		while self.p.poll() is None :
			out = self.p.stdout.readline().decode("utf-8")
			if (out) :
				wx.CallAfter(self.txtVpn.WriteText,out)
		
		wx.CallAfter(self.btConnect.Enable, True)
		wx.CallAfter(self.txtVpn.WriteText,"*** VPN terminated. ***")							
	
	def setConn(self,event):
		host=self.entryHostVpn.GetValue()
		port=self.entryPortVpn.GetValue()
		self.txtVpn.Clear()
		
		if (self.chkServerMode.GetValue()==False):
		#Client Mode Vpn
			if (os.name=="posix"):
				cmd=["pkexec" ,"openvpn" ,"--cd",getScriptDir(), "--config", "client.ovpn", "--remote", host ,port]
				thCmd = threading.Thread(target=self.runProcessPosix,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
				
			elif (os.name=="nt"):
				cmd=[getScriptDir()+"\Openvpn-bundle\openvpn.exe" ,"--cd",getScriptDir(), "--config", "client.ovpn", "--remote", host ,port]
				print(cmd)	
				thCmd = threading.Thread(target=self.runProcessWin,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
		
		else:
		#Server mode Vpn
			if (os.name=="posix"):
				cmd=["pkexec" ,"openvpn" ,"--cd",getScriptDir(), "--config", "server.ovpn", "--port", port]
				thCmd = threading.Thread(target=self.runProcessPosix,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
				
			elif (os.name=="nt"):
				cmd=[getScriptDir()+"\Openvpn-bundle\openvpn.exe" ,"--cd",getScriptDir(), "--config", "server.ovpn", "--port", port]
				thCmd = threading.Thread(target=self.runProcessWin,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
	
class mainWin(TPobhelpGui):
	clientVpn=None
	ftpdDialog=None
	blackboard=None
	vncServer=None
	p=None
	
	
	def showBlackboard(self,evt):
		self.blackboard.Show()
	
	def onAbout(self, evt):
		import wx.adv
		aboutInfo = wx.adv.AboutDialogInfo()
		aboutInfo.SetName("Pobhelp")
		aboutInfo.SetVersion(VERSION)
		icon=os.path.join(getScriptDir(),'lifesaver.png')
		aboutInfo.SetIcon(wx.Icon(icon, wx.BITMAP_TYPE_PNG))
		aboutInfo.SetDescription(_("A simple gui for helpdesking"))
		aboutInfo.SetCopyright(_("Released under GNU/GPL v2 License \n\n Author: Fabio Di Matteo - fadimatteo@gmail.com"))
		aboutInfo.SetWebSite("https://github.com/pobfdm/pobhelp")
		aboutInfo.AddDeveloper("Fabio Di Matteo - fadimatteo@gmail.com")
		#aboutInfo.AddArtist("")
		wx.adv.AboutBox(aboutInfo)
		
	def genRemminaFile(self,port):
		fileRemmina = '''
[remmina]
keymap=
colordepth=16
listenport=''' +port +'''
quality=9
ssh_tunnel_password=
postcommand=
server=
username=
name=VNC Listen Mode
ssh_tunnel_enabled=0
enable-autostart=0
password=
precommand=
disableclipboard=0
group=Casa
disablepasswordstoring=0
protocol=VNCI
disableencryption=0
viewonly=0
ssh_tunnel_server=
ssh_tunnel_loopback=0
ssh_tunnel_auth=0
ignore-tls-errors=1
ssh_tunnel_username=
ssh_tunnel_passphrase=
ssh_tunnel_privatekey=
notes_text=
showcursor=0
disableserverinput=0
window_maximize=0
window_width=1148
window_height=510
viewmode=1
scale=1

		'''	
		textfile = open(getHomePath()+"/.config/pobhelp/inverse.remmina", "w")
		textfile.write(fileRemmina)
		textfile.close()
		
		
	def getPublicIpRaw(self):
		url = "http://api.ipify.org/?format=raw"
		http = urllib3.PoolManager()
		r = http.request('GET', url)
		wx.CallAfter(self.entryHost.SetValue, r.data)
	
	def saveLast(self):
		f=os.path.join(getConfigDirPath(),"lastHost.conf")
		self.entryHost.SaveFile(f)
		f=os.path.join(getConfigDirPath(),"lastPort.conf")
		self.entryPort.SaveFile(f)		
		
	def runCmd(self,cmd):
		wx.CallAfter(self.statusBar.SetStatusText, "Connecting...")
		time.sleep(1)
		
		
		if (self.chkListen.GetValue()==True):
			#Listen Mode
			try:
				self.p=subprocess.Popen(cmd,bufsize=50 ,stderr=subprocess.PIPE)
			except:
				cmd=(["vncviewer","-AlertOnFatalError","-Shared","-listen",self.entryPort.GetValue()])
				self.p=subprocess.Popen(cmd,bufsize=50 ,stderr=subprocess.PIPE)
			
			while self.p.poll() is None :
				line = self.p.stderr.readline()
				if ("Listening" in str(line)):
					wx.CallAfter(self.statusBar.SetStatusText, "Listening...")
					
			wx.CallAfter(self.statusBar.SetStatusText, "Disconnected.")	
			wx.CallAfter(self.btConnect.Enable, True)
			wx.CallAfter(self.btDisconnect.Enable, False)
			wx.CallAfter(self.entryHost.Enable, True)
			wx.CallAfter(self.entryPort.Enable, True)
		else:
			#Connect Mode
			self.p=subprocess.Popen(cmd,bufsize=50 ,stderr=subprocess.PIPE)
			
			while self.p.poll() is None :
				line = self.p.stderr.readline()
				if ("link_rate" in str(line)):
					wx.CallAfter(self.statusBar.SetStatusText, "Connected.")
					
			wx.CallAfter(self.statusBar.SetStatusText, "Disconnected.")	
			wx.CallAfter(self.btConnect.Enable, True)
			wx.CallAfter(self.btDisconnect.Enable, False)
			wx.CallAfter(self.entryHost.Enable, True)
			wx.CallAfter(self.entryPort.Enable, True)	
		
				
	def runCmdWin(self,cmd):
		
		if (self.chkListen.GetValue()==True):
			#Listen Mode
			p=subprocess.Popen(cmd,shell=True)
			startCheck=True
			while(startCheck==True):
				time.sleep(3)
				if (len(find_procs_by_name("tvnviewer.exe"))>0):
					wx.CallAfter(self.statusBar.SetStatusText, "Listening...")
				else:
					startCheck=False
					wx.CallAfter(self.statusBar.SetStatusText, "Disconnected.")	
					wx.CallAfter(self.btConnect.Enable, True)
					wx.CallAfter(self.btDisconnect.Enable, False)
					wx.CallAfter(self.entryHost.Enable, True)
					wx.CallAfter(self.entryPort.Enable, True)	
		else:
			#Connect mode
			p=subprocess.Popen(cmd,shell=True)
			startCheck=True
			while(startCheck==True):
				time.sleep(3)
				if (len(find_procs_by_name("tvnserver.exe"))>2):
					wx.CallAfter(self.statusBar.SetStatusText, "Connected.")
				else:
					startCheck=False
					wx.CallAfter(self.statusBar.SetStatusText, "Disconnected.")	
					wx.CallAfter(self.btConnect.Enable, True)
					wx.CallAfter(self.btDisconnect.Enable, False)
					wx.CallAfter(self.entryHost.Enable, True)
					wx.CallAfter(self.entryPort.Enable, True)					
					
	
			
	
	
	def quit(self, event):
		print("Quitting...")
		try:
			if (self.vncServer.p!=None):
				self.vncServer.p.kill()
		except:
			print("Vnc server is sill alive!")	
		
		wx.CallAfter(sys.exit)
	
	def chkListenClicked(self,event):
		if (self.chkListen.GetValue()==True):
			self.entryHost.SetValue("localhost")
			publicIP = threading.Thread(target=self.getPublicIpRaw, args=())
			publicIP.daemon = True
			publicIP.start()
			
			
			self.entryHost.Disable()
		else:
			self.entryHost.SetValue("")	
			self.entryHost.Enable()
			self.entryPort.SetValue("")
	
	
	def runRemminaVNCI(self,evt):
		if not (self.entryPort.GetValue()):
			Warn(self,"Fill port please!", 'Warning')
			return
		
		self.genRemminaFile(self.entryPort.GetValue())
		cmd=(["remmina", "-c",getHomePath()+"/.config/pobhelp/inverse.remmina"])
		try:
			subprocess.Popen(cmd)
		except:	
			Warn(self,"Remmina is not installed!", 'Warning')
	
	
	def connect(self,event):
		if not (self.entryHost.GetValue() and self.entryPort.GetValue()):
			Warn(self,"Fill host and port please!", 'Warning')
			return
		
		if (self.chkVpnMode.GetValue()==True):
			win.clientVpn.entryHostVpn.SetValue(self.entryHost.GetValue())
			win.clientVpn.entryPortVpn.SetValue(self.entryPort.GetValue())
			win.clientVpn.setConn(None)
				
		
		self.btConnect.Disable()
		self.btDisconnect.Enable()
		self.entryHost.Disable()
		self.entryPort.Disable()
		self.saveLast()	
		if (self.chkListen.GetValue()==True):
			
			#Listen Mode
			self.statusBar.SetStatusText("Listen to port %s" % self.entryPort.GetValue())
			if (os.name=="posix"):
				self.genRemminaFile(self.entryPort.GetValue())
				cmd=(["remmina", "-c",getHomePath()+"/.config/pobhelp/inverse.remmina"])
				thCmd = threading.Thread(target=self.runCmd ,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
					
			
			elif (os.name=="nt"):
				cmd=([getScriptDir()+"/TightVNC-bundle/tvnviewer.exe", "-listen", "-port",self.entryPort.GetValue()])
				self.entryPort.SetValue("5500")
				thCmd = threading.Thread(target=self.runCmdWin ,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
				
		else:
			#Connect Mode
			if (os.name=="posix"):
				self.startChecking=True
				wx.CallAfter(self.statusBar.SetStatusText, "Connecting...")
				cmd=(["x11vnc","--connect_or_exit",self.entryHost.GetValue()+":"+self.entryPort.GetValue()])
				thCmd = threading.Thread(target=self.runCmd ,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
			
			elif (os.name=="nt"):
				self.startChecking=True
				wx.CallAfter(self.statusBar.SetStatusText, "Connecting...")
				cmd=([getScriptDir()+"/TightVNC-bundle/tvnserver.exe", "-controlservice",  "-connect", self.entryHost.GetValue()+"::"+self.entryPort.GetValue()])
				thCmd = threading.Thread(target=self.runCmdWin ,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
				
				
			
				
				
	
	def disconnect(self,event):
		self.btConnect.Enable()
		self.btDisconnect.Disable()
		
		if (self.chkListen.GetValue()==True):
			#Listen Mode
			self.statusBar.SetStatusText("Disconnected to port %s" % self.entryPort.GetValue())
			
			
			if (os.name=="posix"):
				#cmd=(["killall","vncviewer"])
				#thCmd = threading.Thread(target=self.runCmd ,args=(cmd,))
				#thCmd.daemon = True
				#thCmd.start()
				self.p.kill()
			
			elif (os.name=="nt"):
				cmd=(["taskkill","/im","tvnviewer.exe","/f"])	
				thCmd = threading.Thread(target=self.runCmd ,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
		else:
			#Connect Mode
			if (os.name=="posix"):
				cmd=(["x11vnc","-remote","stop"])
				thCmd = threading.Thread(target=self.runCmd ,args=(cmd,))
				thCmd.daemon = True
				thCmd.start()
			
			elif (os.name=="nt"):
				cmd=([getScriptDir()+"/TightVNC-bundle/tvnserver.exe","-controlservice", "-disconnectall" ])
				p=subprocess.run(cmd,shell=True)
				
		
	def runVpnClient(self,event):
		self.clientVpn.Show()
	
	def	runFTPDdialog(self, event):
		self.ftpdDialog.Show()
	
	def runVncServerDialog(self, event):
		self.vncServer.Show()
		
			
if __name__ == '__main__':
	
	#Change to script dir
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	
	import locale, gettext
	try:
		current_locale, encoding = locale.getdefaultlocale()
		locale_path = 'locale'
		language = gettext.translation ('pobhelp', locale_path, [current_locale] )
		language.install()
		
	except:
		_ = gettext.gettext				
	
	
	
	
	
	
	app = wx.App()
	
	win = mainWin(None)
	win.clientVpn=dialogVpnClient(win)
	win.ftpdDialog=dlgFTPD(win)
	win.vncServer=frmVncServer(win)
	
	win.ftpdDialog.entryUser.SetValue("admin")
	win.ftpdDialog.entryPassword.SetValue("admin")
	win.ftpdDialog.entryPort.SetValue("2121")
	win.ftpdDialog.dirPkrFTPRoot.SetPath(getHomePath())
	
	win.blackboard=frmblackboard(win)
	win.blackboard.SetIcon(wx.Icon(getScriptDir()+"/lifesaver.ico"))
	
	if (os.name=="nt"):
		win.mnuVncServer.Enable(False)
	
	
	
	try:
		os.makedirs( getConfigDirPath(), 0o755 );
	except FileExistsError:
		f=os.path.join(getConfigDirPath(),"lastHost.conf")
		if (os.path.isfile(f)):
			win.entryHost.LoadFile(f)
		f=os.path.join(getConfigDirPath(),"lastPort.conf")
		if (os.path.isfile(f)):
			win.entryPort.LoadFile(f)
	
	win.statusBar.SetStatusText("Ready.")
	win.SetIcon(wx.Icon(getScriptDir()+"/lifesaver.ico"))
	
	win.btDisconnect.Disable()
	win.Show(True)
	app.MainLoop()
