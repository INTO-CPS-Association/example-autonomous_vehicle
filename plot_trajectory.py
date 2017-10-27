#!/usr/bin/env python
from numpy import genfromtxt
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

if __name__ == '__main__':

	directory = 'Multi-models/basic-sim/simulation-1'
	newestfolder = max([os.path.join(directory,d) for d in os.listdir(directory)], key=os.path.getmtime)
	outputfile = ''.join([newestfolder, '/outputs.csv'])
	time= datetime.fromtimestamp(os.path.getmtime(outputfile)).strftime('%Y-%m-%d %H:%M:%S')
	ts = str('%s at time %s' %(outputfile,time ))
	print(ts)
	my_data = genfromtxt(outputfile, dtype=None, delimiter=',', skip_header=0)
	my_path = genfromtxt('Models/steering_controller/route.csv', dtype=None, delimiter=',', skip_header=1)
	#my_GPSdata = genfromtxt('gps_rotated.csv', dtype=None, delimiter=',', skip_header=0)
	plt.plot(my_data[1:,7], my_data[1:,8],'r',label="Simulated Trajectory")
	plt.plot(my_path[1:,0], my_path[1:,1],'--b',label="Path")
	#plt.plot(my_GPSdata[1:,0], my_GPSdata[1:,1],'r',linewidth=1.0,label="Field Test")
	plt.axis('equal')
	plt.xlabel('x [m]')
	plt.ylabel('y [m]')	
	plt.legend(loc=1)	
	plt.grid('on')
	plt.show()