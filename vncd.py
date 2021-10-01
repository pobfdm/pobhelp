from gui import *
import os,threading,sys
import pobhelp
import subprocess

def getDatetime():
	from time import gmtime, strftime
	return strftime("%Y-%m-%d %H:%M:%S", gmtime())


def getScriptDir():
	if getattr(sys, 'frozen', False):
		return sys._MEIPASS
	else:
		return os.path.dirname(os.path.abspath(__file__))

class frmVncServer(TdlgVncServer):
	password=None
	port=None
	cmd=None
	
	def init(self,evt):
		if (os.name=="nt"):
			self.entryPassword.Disable()
			self.entryPort.Disable()
			self.entryPassword.SetValue("")
			self.entryPort.SetValue("")
		
	
	def onclose(self,evt):
		self.Hide()
		
	def startServer(self,evt):
		self.btStart.Enable(False)
		self.btStop.Enable(True)
		self.txtOutput.WriteText(' *** ('+getDatetime()+') Running vnc Server ... ***')
		self.txtOutput.Newline()
		
		if (os.name=="posix"):
			thVNC = threading.Thread(target=self.runProcessPosix)
			thVNC.daemon = True
			thVNC.start()
		elif (os.name=="nt"):
			thVNC = threading.Thread(target=self.runProcessWin)
			thVNC.daemon = True
			thVNC.start()	
	
	def stopServer(self,evt):
		self.btStart.Enable(True)
		self.btStop.Enable(False)
		self.txtOutput.WriteText(' *** ('+getDatetime()+') Server Stopped by user ***')
		self.txtOutput.Newline()
		if (os.name=="posix"):
			self.p.kill()
		elif (os.name=="nt"):
			kcmd=[getScriptDir()+"/TightVNC-bundle/tvnserver.exe", "-controlapp","-shutdown"]
			p=subprocess.run(kcmd)
			
	def runProcessPosix(self):
		self.cmd=["x11vnc" ,"-wait" ,"50","-noxdamage", "-passwd", self.entryPassword.GetValue(),"-display",":0","-rfbport", self.entryPort.GetValue(), "-forever"]
		if (self.chkViewOnly.GetValue()==True):
			self.cmd.append("-viewonly")
		
		self.p=subprocess.Popen(self.cmd, bufsize=0 ,stdout=subprocess.PIPE)
		while self.p.poll() is None :
			out = self.p.stdout.readline().decode("utf-8")
			if (out) :
				wx.CallAfter(self.txtOutput.WriteText,out)
				
		
	
	def runProcessWin(self):
		self.cmd=[getScriptDir()+"/TightVNC-bundle/tvnserver.exe"  , "-run"]
		self.p=subprocess.run(self.cmd)
		self.cmd=[getScriptDir()+"/TightVNC-bundle/tvnserver.exe"  , "-controlapp", "-sharefull"]
		self.p=subprocess.run(self.cmd)
