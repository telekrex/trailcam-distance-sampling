
# Area = pi * r^2
#
# r = sqr root of Area / pi


import math

Area = 100

r = math.sqrt(Area / math.pi)

angle = 120

sector = (angle / 360) * (math.pi * (r**2))


print(sector)