#Anna Peterson
#GEOG 6180
#November 7, 2022
#Assignment 8

#Just ignore all the random libraries. I was trying a few things
from numpy import *
from math import *
import os
import matplotlib.pyplot as plt
import pandas as pd


n = 300              # DEM is 300 by 300
d = zeros((n,n))     # DEM begins as a 2D array of 0's (float)

#Read DEM
def ReadDEM():
    
    DEM_file = open('UU_DEM.txt','r')

    # Read elevation values from textfile into a 2D array of floats
    i = 0
    for line in DEM_file:
        l = line.split()         # split the line into a list of strings
        for j in range(n):
            d[i,j] = float(l[j]) # convert string numbers like '1234.5' to float
        i = i + 1
    DEM_file.close()


# Main function
def main():
    ReadDEM()

    # Print out upper left 5x5 of the DEM to verify it was read.
    # Elevation z-values are in meters (full DEM is 300 by 300)

    print("DEM dimensions: ", len(d), "by", len(d[0]))  # rows by cols
    for i in range(5):
        for j in range(5):
            print(d[i][j])
        print

# Call the main function
main()

#Read in the data again and name it something else
x = loadtxt("UU_DEM.txt")
#STEP 2A: Print the average, min, max to get the greatest difference
print('Average:', average(x))
print('Max:', amax(x))
print('Min:', amin(x))
print('Greatest difference in elevation:', amax(x) - amin(x))

#STEP 2B: Create bins. I loaded the data again just to differentiate what I'm asking. It's
# not necessary, but it keeps my head straight.
q = loadtxt("UU_DEM.txt")
hist, bin_edges = histogram(q, bins = [1381.8, 1468.18, 1554.56, 1640.94, 1727.32, 1813.7])
print(hist)

#STEP 3
# DEM resolution
res = 10

rows = 300
cols = 300

# init slope and aspect to 0
s = 0.0
a = 0.0

aspect = []
slope = []
def SlopeAspect(i, j, d):

    #computer b and c for the slope/aspect equations
    b = float((d[i-1, j+1] + (2*d[i, j+1]) + d[i+1,j+1] - d[i-1,j-1] - (2*d[i, j-1]) - d[i+1,j-1])) / (8*res)
    c = float((d[i+1, j-1] + (2*d[i+1, j]) + d[i+1,j+1] - d[i-1,j-1] - (2*d[i-1, j]) - d[i-1,j+1])) / (8*res)


    # Compute slope in degrees
    s = degrees(atan(sqrt(pow(b, 2) + pow(c, 2))))
    slope.append(s)

    # Compute the aspect
    a = 57.29578 * atan2(c, -b)

    # Convert aspect to degrees
    if a < 0:
        a = 90.0 - a
    elif a > 90.0:
        a = 360.0 - a + 90.0
    else:
        a = 90.0 - a

    # Aspect is undefined (-1) if slope is zero
    if s == 0:
        a = -1

    aspect.append(a)

# Compute the slope for all cells not on the edge
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
       # print("Cell:", "(", i, ",", j, ")")
        SlopeAspect(i, j, d)

#STEP 4A:

print("Shallowest slope: ", math.floor(min(slope)))
print ("Steepest slope: ", max(slope))
print ("What cell the shallowest slope is located in:", slope.index(min(slope)))
print ("What cell the steepest slope is located in:", slope.index(max(slope)))

#STEP 4B:
hist, bin_edges = histogram(slope, bins = [0, 10, 20, 30, 47])
slope_percent = (hist/90000)*100
print("Slope: ", slope_percent)

#STEP 4C:
hist, bin_edges = histogram(aspect, bins = [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180,
                                202.5, 225, 247.5, 270, 292.5, 315, 337.5, 360])
aspect_percent = (hist/90000)*100
print("Aspect: ", aspect_percent)
