import os

def dir():
	path = os.getcwd() 
	#dirname = os.path.abspath(os.path.join(path, os.pardir)) 
	dirname = os.getcwd()
	return dirname
