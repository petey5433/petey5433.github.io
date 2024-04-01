import arcpy
arcpy.env.workspace = "N:\PythonPro\Ex06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
 fcdesc = arcpy.da.Describe(fc)
 dtype = fcdesc["dataType"]
 name = fcdesc["name"]
 stype = fcdesc["shapeType"]
 print(f"{dtype} {name} has shapetype {stype}")
