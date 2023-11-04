

# Camera to pole  83 in 6.9 ft
# Camera to plate  144 in 12 ft
# Camera to fence  304 in  25.3 ft
# Camera 120 degrees 3,036 sq ft

species = 'kitty cat'

region_area_sqft = 500000 # roughly 3 block radius
camera_fov_degrees = 120
distance_limit_feet = 25.3 # from my camera to the fence
area_surveyed_sqft = camera_fov_degrees * distance_limit_feet

# population_estimate = (seen / probably_seen) / (survey_area / region_area)
# where survey_area = cam_fov * limit_dist
# and probably_seen = detection function goes here

# sightings = 3
# percentage_of_sightings = 0.5



sightings_distances = [2, 1, 2, 3, 1, 3, 2, 4, 1, 2, 1, 5]
number_of_sightings = len(sightings_distances)
max_distance = sorted(sightings_distances)[-1]
mapped_distances = {}
covered = 0
unknown = 0

for distance in sightings_distances:
    unknown += max_distance - distance
    covered += distance
    if distance in mapped_distances:
        mapped_distances[distance] = mapped_distances.get(distance) + 1
    else:
        mapped_distances[distance] = 1












md = []
for x in mapped_distances:
    md.append(x)

ratio = covered / unknown

print(covered)
print(unknown)
print(ratio)

percentage_of_sightings = ratio

for x in md:
    s = mapped_distances.get(x)
    v = ''
    for i in range(s):
        v += 'sss'
    print(v)

print(mapped_distances)


estimated_population_size = (number_of_sightings / percentage_of_sightings) / (area_surveyed_sqft / region_area_sqft)

specimen_per_sqft = estimated_population_size / region_area_sqft

print(f'\n there are approximately ~{round(estimated_population_size)} {species}s in the area\n thats {round(specimen_per_sqft, 4)} {species}s per square foot')
