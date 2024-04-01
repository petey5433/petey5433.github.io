import arcpy
from sys import argv

#to run outside my own computer, you will want to change the following parameters

Init = "N:\6180_Final\6180_Final.gdb\MapUnitPolys"
Haz = "N:\6180_Final\6180_Final.gdb\Hazard"
Area = "N:\6180_Final\6180_Final.gdb\Area"

# Takes in raw input to determine which filter to utilize by user selection
def GeoHaz():
    print("Geologic hazards are dangerous!")
    print("Do you want to search for a hazard zone?")
    answer = input("Type Volcano (V), Earthquake (E), or Landslide (L) then hit 'Enter'.").lower()
    # Volcano
    if answer == "Volcano" or answer == "V":
        #building the filter (change the where clause .csv)
        def VolcanoHazardFilter(MapUnitPolys = Init, Hazard = Haz):

            Unit = "Tacoma Geologic Unit"

            # Selecting units
            arcpy.analysis.Select(in_features = Unit,
                                  out_feature_class = Hazard,
                                  where_clause = "tacoma_units.csv.LITHOLOGY IN ('basalt flows and flow breccias, Crescent Formation', 'lahars', 'volcaniclastic deposits or rocks')")
        VolcanoHazardFilter()
    #Landslide
    elif answer == "Landslide" or answer == "L":
        # landslide filter, it runs the same as the volcano hazard, but with different units
        def SlideHazardFilter(MapUnitPolys = Init, SlideHazard = Haz):

            Unit = "Tacoma Geologic Unit"

            # Selecting units
            arcpy.analysis.Select(in_features = Unit,
                                  out_feature_class = SlideHazard,
                                  where_clause = "tacoma_units.csv.LITHOLOGY IN ('mass-wasting deposits, mostly landslides')")
        SlideHazardFilter()
    #Earthquake
    elif answer == "Earthquake" or answer == "E":  
        #building the eqarthquake filter 
        def QuakeHazardFilter(MapUnitPolys = Init, Hazard = Haz):

            Unit = "Tacoma Geologic Unit"

            # Selecting units
            arcpy.analysis.Select(in_features = Unit,
                                  out_feature_class = Hazard,
                                  where_clause = "tacoma_units.csv.LITHOLOGY IN ('serpintine', 'shocked quartz')")
        QuakeHazardFilter()
    else:
        print ("Please try again.")
        
GeoHaz()


# dissolve polygons into one shape then multiple shape area by 10% (change hazard name to whichever hazard you are working with)
def Area(Hazard = Haz, Area="N:\6180_Final\6180_Final.gdb\Area"):  

    # Dissolve polygons through arcpy
    arcpy.management.Dissolve(in_features = Hazard,
                              out_feature_class = Area,
                              dissolve_field = ["DescriptionOfMapUnits_GeneralLithology"],
                              statistics_fields = [], multi_part="MULTI_PART",
                              unsplit_lines = "DISSOLVE_LINES", concatenation_separator = "")

Area()   
# We want to know the entirety of the area so we can assume how big to create our buffer    
# empty list
l = []

# set workspace through arcpy
arcpy.env.workspace = r"N:\6180_Final\6180_Final.gdb"

# define margin of error here
ME = .1 #for 10% error

# using arcpy's search cursor for selecting and returning rows, we specifically want area
rows = arcpy.SearchCursor("Area")

# for loop that goes through all the values of shape_area and appends to our empty list, l
for row in rows:
    tot = row.getValue("Shape_area")
    l.append(tot)
    
# sums all the items in the list to get the total area
a = sum(l)

# multiply our sum by the margin of error to get how much border to add to our buffer
a = a * ME 

#Creating the hazard zone (change hazard name to whichever hazard you are working with)
def HazardZone(Hazard = Haz, Hazard_zone = "N:\6180_Final\6180_Final.gdb\Hazard_zone"): 

    # Buffer and make sure to have dissolve on ALL to make sure it creates one polygon rather than several
    arcpy.analysis.Buffer(in_features = Hazard,
                          out_feature_class = Hazard_zone,
                          buffer_distance_or_field = a + "International Feet",
                          line_side="FULL", line_end_type="ROUND",
                          dissolve_option = "ALL", dissolve_field = [],
                          method="PLANAR")

HazardZone()

# clipping public schools to hazard zone
# arcpy.analysis.Clip(in_features = Washington_State_Public_Schools, clip_features = Hazard, out_feature_class = Danger2Schools)
