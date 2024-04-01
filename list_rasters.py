import arcpy
arcpy.env.workspace = "N:\PythonPro\Ex10\Data"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
 print(raster)
