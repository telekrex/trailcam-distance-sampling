



R = 500000 # Region area, in sq. ft
C = 120 # Camera FOV, in degrees
D = 25.3 # Distance from camera to limit, in ft
A = C * D # Area surveyed by camera, to D, in sq. ft

# In this example, my camera of 120 degrees field of view
# surveyed an area to a distance of 25.3 feet (the fence
# in my backyard). I am interested in an estimation of
# 500,000 square feet around me, roughly a 3 block raidus.

sd = [2, 1, 2, 3, 1, 3, 2, 4, 1, 2, 1, 5]
# list of sightings, each in feet
n = len(sd) # number of sightings, total
maxd = sorted(sd)[-1] # max distance of any sighting