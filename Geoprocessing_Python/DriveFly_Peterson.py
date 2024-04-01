#Anna Peterson
#GEOG 6180
#October 24, 2022

from math import *
from numpy import *

## PART 1

#Step 1
# Initialize array of points from Numpy
p = array([[356.647, 4237.752],
     [364.415, 4357.138],
     [384.706, 4314.043],
     [430.910, 4620.996],
     [626.337, 4270.335],
     [645.836, 4192.594],
     [419.447, 4564.488],
     [459.050, 4085.449],
     [443.795, 4455.096],
     [425.430, 4511.381],
     [270.880, 4108.552],
     [624.174, 4479.259]])


# Function to fill a matrix with Euclidean distances
def EuclidDistMatrix(p):
    n = len(p)

    z = zeros((n,n))    # numpy function to create matix of zeros

    for i in range(n):
        for j in range(n):
            if i != j:
                xc = pow(p[i, 0] - p[j, 0], 2)    # (x0 - x1) ^ 2
                yc = pow(p[i, 1] - p[j, 1], 2)    # (y0 - y1) ^ 2
                z[i,j] = round(sqrt(xc + yc), 1)

    return z

# Call the functions to fill the matrices d and m
F = EuclidDistMatrix(p)


# Print out the results
print("Euclidean Distance")
print(F)

#Step 2
# Initialize a distance matrix with 99's in the unknown cells
# Diagonal is always zeros
d = array([[  0, 999,  90, 999, 379, 999, 999, 303, 999, 999, 168, 999],
              [999,   0,  62, 999, 999, 999, 999, 999, 149, 999, 291, 999],
              [ 90,  62,   0, 999, 339, 999, 999, 999, 162, 999, 999, 999],
              [999, 999, 999,   0, 999, 999,  72, 999, 999, 999, 999, 999],
              [379, 999, 339, 999,   0,  87, 999, 999, 307, 999, 999, 366],
              [999, 999, 999, 999,  87,   0, 999, 352, 999, 999, 999, 999],
              [999, 999, 999,  72, 999, 999,   0, 999, 999,  62, 999, 999],
              [303, 999, 999, 999, 999, 352, 999,   0, 999, 999, 248, 999],
              [999, 149, 162, 999, 307, 999, 999, 999,   0,  73, 999, 247],
              [999, 999, 999, 999, 999, 999,  62, 999,  73,   0, 999, 278],
              [168, 291, 999, 999, 999, 999, 999, 248, 999, 999,   0, 999],
              [999, 999, 999, 999, 366, 999, 999, 999, 247, 278, 999,   0]])

# Function to run Floyd's algorithm
def Floyd():
    n = len(d)
    print(n)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i,j] = min(d[i, j], d[i, k] + d[k, j])

Floyd()

print("Floyd result")
print(d)

#Step 3
#For whatever reason python was thinking too much about the zeros so I used 
#seterr to get around this
seterr(divide = 'ignore', invalid = 'ignore')

#ratio of D:F
rat = d/F
print("The ratio of D:F is:")
print(rat)

#Difference of D - F
diff = d - F
print("The difference between D - F is:") 
print(diff)

#Step 4
n = array([["Beaver",    356647, 4237752, 38.276389, -112.638889],
     ["Delta",     364415, 4357138, 39.353056, -112.573611],
     ["Fillmore",  384706, 4314043, 38.967778, -112.330833],
     ["Logan",     430910, 4620996, 41.737778, -111.830833],
     ["Moab",      626337, 4270335, 38.572500, -109.549722],
     ["Monticello",645836, 4192594, 37.869167, -109.341944],
     ["Ogden",     419447, 4564488, 41.227778, -111.961111],
     ["Page AZ",   459050, 4085449, 36.914167, -111.459722],
     ["Provo",     443795, 4455096, 40.244422, -111.660803],
     ["Salt Lake", 425430, 4511381, 40.750000, -111.883333],
     ["St.George", 270880, 4108552, 37.095278, -113.578056],
     ["Vernal",    624174, 4479259, 40.454722, -109.535556]])

temp = []
# Step 4 is finished at the bottom

# PART 2
d_time = d/112
print d_time
f_time = F/804
print f_time

for i in range(12):
    for j in range(12):
        temp.append((rat[i,j],i,j,diff[i,j],d[i,j],F[i,j],d_time[i,j],f_time[i,j]))

temp.sort()
temp.reverse()

for pair in temp:
    ratio = round(pair[0], 4)
    city1 = n[pair[1]][0]
    city2 = n[pair[2]][0]
    diff = round(pair[3],1)
    duh = round(pair[4],2)
    Fun = round(pair[5],2)
    drive = round(pair[6],2)
    fly = round(pair[7],4)
    print(city1, city2, duh, Fun, ratio, diff, drive, fly)




