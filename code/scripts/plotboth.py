﻿#!/usr/bin/python
from numpy import *
from pylab import *
from matplotlib import rc, rcParams

#rc('text',usetex=False)
#rc('font',**{'family':'serif','serif':['Computer Modern']})

# Read in data from an ASCII data table
dataSpline = genfromtxt(sys.argv[1])
dataOpenSim = genfromtxt(sys.argv[2])

for i in range(0,dataSpline.shape[1]):
  #'data' is a matrix containing the columns and rows from the file
  fromOpenSim   = dataOpenSim[:,i]  # Python indices are (row,col) as in linalg
  fromSpline = dataSpline[:,i]  # Creates arrays for first two columns

  # Create a plot of the data
  p1, = plot(fromOpenSim, 'b')
  p2, = plot(fromSpline, 'r')
  legend([p1, p2], ["from Spline (1st file)", "from OpenSim (2nd file)"])
  # Turn on a grid
  grid(True)

  # Draw the plot to the screen
  show()