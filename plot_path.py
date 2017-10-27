#!/usr/bin/env python
from numpy import genfromtxt
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    my_data = genfromtxt('Multi-models/basic-sim/simulation-1/R_2-3-2017_12-26-47_PM/outputs.csv', dtype=None, delimiter=',', skip_header=1)
    my_path = genfromtxt('Models/steering_controller/route.csv', dtype=None, delimiter=',', skip_header=1)

    plt.plot(my_data[1:,7], my_data[1:,8],'--b',my_path[1:,0], my_path[1:,1],'xk')
    plt.show()
	
