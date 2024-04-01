import arcpy
arcpy.env.workspace = "N:\PythonPro\Ex10\Data"
arcpy.CheckOutExtension("Spatial")
outraster = arcpy.sa.Slope("elevation")
desc = arcpy.da.Describe(outraster)
print(desc["datasetType"])
print(desc["permanent"])

##if arcpy.CheckExtension("Spatial") == "Available":           
##    print("Spatial extension available.")
##else:
##    print("Not available.")
