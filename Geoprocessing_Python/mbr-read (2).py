from numpy import *

# This is the code to read in a point set textfile (*.txt)
# The first line of the textfile is the number of points, followed by each point as follows:
# 2
# 3,2
# 1,5

# Define a class called Point that has two elements
class Point:	
    x = 0
    y = 0

# Declare an array called points with room for N points (e.g. 10)
points = [Point() for i in range(10)]

# Function to read points from a textfile named "name"; returns the number of points
def readFile(name):
    myFile = open(r"N:\points.txt")
    numpoints = int(myFile.readline())
    print(numpoints)
    for i in range(numpoints):
        points[i].x, points[i].y = [int(x) for x in myFile.readline().split()]
        print(points[i].x, points[i].y)
    myFile.close()
    return numpoints

# This will be the logic to define the MBR but right now it just prints the points
def MBR(n):
    print("MBR")
    minx = 999
    miny = 999
    maxx = 0
    maxy = 0
    for i in range(n):
        if (points[i].x < minx):
           minx = points[i].x
        if (points[i].y < miny):
            miny = points[i].y
        if (points[i].x > maxx):
            maxx = points[i].x
        if (points[i].y > maxy):
            maxy = points[i].y
    print (minx, miny, maxx, maxy)
       

# The main function that reads in a point textfile and calculates the MBR
def main():
    n = readFile("N:\points.txt")
    MBR(n)

# Call the main function
main()



