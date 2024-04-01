import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "N:\PythonPro\Ex06"
fieldlist = arcpy.ListFields("cities.shp")
for field in fieldlist:
 print(field.name + " " + field.type)
