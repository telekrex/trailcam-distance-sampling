
R = 500000 # Region area, in sq. ft
C = 120 # Camera FOV, in degrees
D = 25.3 # Distance from camera to limit, in ft
A = C * D # Area surveyed by camera, to D, in sq. ft

V = 3 # Approx. area taken up by a single specimen, in sq. ft
# In this case, a cat. I'm being a bit lenient about size,
# because I know they extremely rarely would be close enough
# to each other to occupy the same space.

# In this example, my camera of 120 degrees field of view
# surveyed an area to a distance of 25.3 feet (the fence
# in my backyard). I am interested in an estimation of
# 500,000 square feet around me, roughly a 3 block raidus.

sd = [1, 3, 2, 8, 32, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 1] # list of sightings, each in feet
aR = R - (V * len(sd)) # region area minus total area taken up by sepcimens, in sq. ft
n = len(sd) # number of sightings, total
maxd = sorted(sd)[-1] # max sighting distance

mapped_distances = {}
covered = 0
unknown = 0

for distance in sd:
    unknown += maxd - distance
    covered += distance
    if distance in mapped_distances:
        mapped_distances[distance] = mapped_distances.get(distance) + 1
    else:
        mapped_distances[distance] = 1

ratio = covered / unknown
percentage_of_sightings = ratio
estimated_population_size = (n / percentage_of_sightings) / (A / aR)
specimen_per_sqft = estimated_population_size / aR

print(f'\n there are approximately ~{round(estimated_population_size)} kitties in the area')
print(f' thats {round(specimen_per_sqft, 4)} kitties per square foot')
