import arcpy
import os
ws = "N:\PythonPro\Ex06"
fgdb = "Copy.gdb"
arcpy.CreateFileGDB_management(ws, fgdb)
arcpy.env.workspace = ws
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
 fcname = arcpy.da.Describe(fc)["baseName"]
 newfc = os.path.join(ws, fgdb, fcname)
 arcpy.CopyFeatures_management(fc, newfc)
