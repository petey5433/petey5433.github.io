import arcpy

arcpy.env.workspace = "N:\PythonPro\Ex06"
fc = "cities.shp"
newfc = "cities_copy.shp"
if arcpy.Exists(fc):
 arcpy.CopyFeatures_management(fc, newfc)

