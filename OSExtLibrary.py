#**************************************************************************************************
#
# [Filename]: OSExtLibrary.py
# [Purpose ]: Additional keyword for Robot Framework.
#
# History:
#**************************************************************************************************
# VER  NAME      DATE        COMMENT
#**************************************************************************************************
# R00  Evan Chang 2013/05/29  Initial version.

#==================================================================================================
#
# Import Section: add all import here
#
#==================================================================================================
import os


class OSExtLibrary:
	def __init__(self):
		self.original_dir = os.getcwd()

	def change_directory(self, path):
		print "current directory : %s" % os.getcwd()
		os.chdir(path)
		print "change directory to  %s" % os.getcwd()		