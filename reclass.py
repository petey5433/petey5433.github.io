import arcpy
from arcpy.sa import *
arcpy.env.workspace = "N:\PythonPro\Ex10\Data"
arcpy.CheckOutExtension("Spatial")
myremap = RemapValue([[41,1], [42,2], [43,3]])
outreclass = Reclassify("landcover.tif", "VALUE", myremap, "NODATA")
outreclass.save("lc_recl")
