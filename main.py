#!/usr/bin/python
import sys, alsaaudio, xdg.IconTheme
from PySide.QtCore import *
from PySide.QtGui import *

class App:
	def __init__(self):
		self.app = QApplication(sys.argv)
		
		# TODO change icon according to volume
		self.lowIcon = QIcon(xdg.IconTheme.getIconPath("audio-volume-low"))
		self.medIcon = QIcon(xdg.IconTheme.getIconPath("audio-volume-high"))
		self.highIcon = QIcon(xdg.IconTheme.getIconPath("audio-volume-medium"))
		self.muteIcon = QIcon(xdg.IconTheme.getIconPath("audio-volume-muted"))
		
		self.menu = QMenu()
		volPlusAction = self.menu.addAction("Volume +")
		volMinusAction = self.menu.addAction("Volume -")
		volMuteAction = self.menu.addAction("Mute")
		
		volPlusAction.triggered.connect(self.volume_plus)
		volMinusAction.triggered.connect(self.volume_minus)
		volMuteAction.triggered.connect(self.volume_mute)
		
		self.tray = QSystemTrayIcon()
		self.tray.setContextMenu(self.menu)
		self.tray.show()
		
		self.update_icon()
		
	def run(self):
		self.app.exec_()
		sys.exit()

	def set_volume(self, value):
		if value >= 0 and value <= 100:
			mixer = alsaaudio.Mixer()
			mixer.setvolume(value)
	
	def get_volume(self):
		mixer = alsaaudio.Mixer()
		return mixer.getvolume()[0]
	
	def volume_plus(self):
		self.set_volume(self.get_volume() + 10)
		self.update_icon()
	
	def volume_minus(self):
		self.set_volume(self.get_volume() - 10)
		self.update_icon()
	
	def volume_mute(self):
		mixer = alsaaudio.Mixer()
		
		if mixer.getmute()[0]:
			mixer.setmute(0)
		else:
			mixer.setmute(1)
		
		self.update_icon()
	
	# Updates the icon according to the volume level
	def update_icon(self):
		mixer = alsaaudio.Mixer()
		
		if mixer.getmute()[0]: self.tray.setIcon(self.muteIcon)
		else:
			if self.get_volume() < 33: self.tray.setIcon(self.lowIcon)
			elif self.get_volume() < 66: self.tray.setIcon(self.medIcon)
			else: self.tray.setIcon(self.highIcon)

if __name__ == "__main__":
	app = App()
	app.run()