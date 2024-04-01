import arcpy
from arcpy.sa import *
arcpy.env.workspace = "N:\PythonPro\Ex10\Data"
arcpy.CheckOutExtension("Spatial")
elevraster = arcpy.Raster("elevation")
slope = Slope(elevraster)
goodslope = slope < 20
goodelev = elevraster < 2500
goodfinal = goodslope & goodelev
goodfinal.save("final")

