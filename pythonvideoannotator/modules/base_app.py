#! /usr/bin/python2
# -*- coding: utf-8 -*-
from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtGui, QtCore
from pyforms.Controls import ControlPlayer
from pyforms.Controls import ControlFile
from pyforms.Controls import ControlEventTimeline
from pyforms.Controls import ControlDockWidget


def Exit(): exit()

class VideoAnnotationEditor(BaseWidget):
	"""Application form"""

	def __init__(self):
		global conf;
		conf += 'pythonvideoannotator.resources'  # Resources can only be loaded after pyqt is running

		super(VideoAnnotationEditor, self).__init__('Video annotation editor')

		self._video 	= ControlFile('Video')
		self._player 	= ControlPlayer("Player")
		self._time 		= ControlEventTimeline('Time')
		self._dock 		= ControlDockWidget("Timeline", side='bottom')
		self._formset 	= ['_video', '_player']

		self._dock.value 				= self._time
		self._video.changed 			= self.video_changed_evt
		self._player.processFrame 		= self.process_frame
		self._player.onClick 			= self.onPlayerClick
		self._time.key_release_event 	= self.__time_key_release_event

		self.mainmenu.insert(0,
			{'File': [ {'Exit': Exit, 'icon': conf.ANNOTATOR_ICON_EXIT} ]}
		)

		
	def initForm(self):
		super(VideoAnnotationEditor, self).initForm()

		if conf.VIDEO_FILE_PATH: self._video.value = conf.VIDEO_FILE_PATH
		if conf.CHART_FILE_PATH: self._time.import_chart(*conf.CHART_FILE_PATH)

	######################################################################################
	#### EVENTS ##########################################################################
	######################################################################################

	def video_changed_evt(self):
		self._player.value 	= self._video.value
		self._time.max 		= self._player.max

	def __time_key_release_event(self, event):
		"""
		Control video playback using the space bar to Play/Pause
		"""
		if event.key() == QtCore.Qt.Key_Space:
			self._video.stop() if self._video.is_playing else self._video.play()
		

	def onPlayerClick(self, event, x, y):
		"""
		Code to select a blob with the mouse
		"""
		super(VideoAnnotationEditor, self).onPlayerClick(event, x, y)
		self._player.refresh()

	def process_frame(self, frame):
		"""
		Function called before render each frame
		"""
		return frame