##import arcpy
##arcpy.env.workspace = "N:\PythonPro\Ex10\Data"
##raster = "landcover.tif"
##desc = arcpy.da.Describe(raster)
##print("Raster base name: " + desc["baseName"])
##print("Raster data type: " + desc["dataType"])
##print("Raster file extension: " + desc["extension"])
##print("Raster spatial reference: " + desc["spatialReference"].name)
##print("Raster format: " + desc["format"])
##print("Raster compression: " + desc["compressionType"])
##print("Raster number of bands: " + str(desc["bandCount"]))

##import arcpy
##arcpy.env.workspace = "N:\PythonPro\Ex10\Data" 
##raster = "tm.img"
##desc = arcpy.da.Describe(raster)
##x = desc["meanCellHeight"]
##y = desc["meanCellWidth"]
##spatialref = desc["spatialReference"]
##units = spatialref.linearUnitName
##print("The raster resolution is {0} by {1} {2}.".format(x, y, units))
##

import arcpy
arcpy.env.workspace = "N:\PythonPro\Ex10\Data" 
raster = "tm.img"
desc = arcpy.da.Describe(raster)
for rband in desc["children"]:
 bandname = rband["baseName"]
 x = rband["meanCellHeight"]
 y = rband["meanCellWidth"]
 spatialref = desc["spatialReference"]
 units = spatialref.angularUnitName
 print("The resolution of {0} is {1:.7f} by {2:.7f} {3}."
 .format(bandname, x, y, units))
##if spatialref.type == "Geographic"
