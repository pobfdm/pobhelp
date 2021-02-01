from gui import *
import os,threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import pobhelp


def getDatetime():
	from time import gmtime, strftime
	return strftime("%Y-%m-%d %H:%M:%S", gmtime())


class NotifyHandler(FTPHandler):
	txtOutput=None
	
	
	def bindGui(self, gui):
		self.gui=gui
		self.trayIcon=gui.trayIcon
	
	def	appendOutput(self,s):
		count=self.gui.listCtrlStatus.GetItemCount()
		wx.CallAfter(self.gui.listCtrlStatus.InsertItem,count,s)
		wx.CallAfter(self.gui.listCtrlStatus.Focus, count)
	
	def on_connect(self):
		print("User connected.")
		wx.CallAfter(self.txtOutput.WriteText,'('+getDatetime()+') '+"User connected.")
		wx.CallAfter(self.txtOutput.Newline)

	def on_disconnect(self):
		print("User disconnected.")
		wx.CallAfter(self.txtOutput.WriteText,'('+getDatetime()+') '+"User disconnected.")
		wx.CallAfter(self.txtOutput.Newline)

	def on_login(self, username):
		wx.CallAfter(self.txtOutput.WriteText,'('+getDatetime()+') '+"User %s ." % username)
		wx.CallAfter(self.txtOutput.Newline)
		
	def on_logout(self, username):
		wx.CallAfter(self.txtOutput.WriteText,'('+getDatetime()+') '+"User %s  logout." % username)
		wx.CallAfter(self.txtOutput.Newline)

	def on_file_sent(self, file):
		# do something when a file has been sent
		wx.CallAfter(self.txtOutput.WriteText,'('+getDatetime()+') '+"File %s  sent." % str(file))
		wx.CallAfter(self.txtOutput.Newline)

	def on_file_received(self, file):
		# do something when a file has been received
		wx.CallAfter(self.txtOutput.WriteText,'('+getDatetime()+') '+"File %s  received." % str(file))
		wx.CallAfter(self.txtOutput.Newline)

	def on_incomplete_file_sent(self, file):
		# do something when a file is partially sent
		wx.CallAfter(self.txtOutput.WriteText,'('+getDatetime()+') '+"File %s  partially sent" % str(file))
		wx.CallAfter(self.txtOutput.Newline)

	def on_incomplete_file_received(self, file):
		# remove partially uploaded files
		wx.CallAfter(self.txtOutput.WriteText,'('+getDatetime()+') '+"File %s  partially received (deleted)" % str(file))
		wx.CallAfter(self.txtOutput.Newline)
		import os
		os.remove(file)



class dlgFTPD(TdlgFTPD):
	server=None
	handler=None
	
	
	def onText(self,evt):
		p=self.txtOutput.GetCaretPosition()
		self.txtOutput.ScrollIntoView(p,wx.WXK_END)
	
	def thdFTPD(self):
		authorizer = DummyAuthorizer()
		authorizer.add_user(self.entryUser.GetValue(), self.entryPassword.GetValue(), self.dirPkrFTPRoot.GetPath(), perm='elradfmwMT')

		self.handler = NotifyHandler
		self.handler.txtOutput= self.txtOutput
		self.handler.authorizer = authorizer
		
		

		self.handler.banner = "[Pobhelp] Pyftpdlib based ftpd ready."

		address = ('0.0.0.0', self.entryPort.GetValue())
		self.server = FTPServer(address, self.handler)

		self.server.max_cons = 256
		self.server.max_cons_per_ip = 5

		
		self.server.serve_forever()
	
	
	def startServer(self,evt):
		self.btStart.Enable(False)
		self.btStop.Enable(True)
		self.txtOutput.WriteText(' *** ('+getDatetime()+') Server Started ***')
		self.txtOutput.Newline()
		thFtpd = threading.Thread(target=self.thdFTPD)
		thFtpd.daemon = True
		thFtpd.start()
	
	def stopServer(self,evt):
		self.server.close_all()
		self.btStart.Enable(True)
		self.btStop.Enable(False)
		self.txtOutput.WriteText(' *** ('+getDatetime()+') Server Stopped by user ***')
		self.txtOutput.Newline()
		
	



