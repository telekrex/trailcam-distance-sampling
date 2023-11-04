# Dist samp

Attempting to perform distance sampling studies using trail cam footage.

A few things just to be clear:
- I am not a scientist, just a curious programmer.
- This project has not been peer reviewed.
- I am sharing this part for fun, but part in hopes that someone smarter than me can point out any mistakes I've made and help me improve this.
- Perhaps it could be useful to people interested in ecology studies using their own trail cams.
- If you intend to use my scripts for your own studies I highly recommend doing additional research and modifying the code as needed.

Most of my understanding of distance sampling comes from https://distancesampling.org/whatisds.html which I've tried to apply in Python.

I understand that observations can be recorded from a single point if you measure the radial distance from the observer to the subject. I paired this with calculating the area that a camera can cover by multiplying the lens field of view by a measured distance to a specific point. I used a trail cam with a fixed FOV of 120 degrees and it's aimed at a fence which firmly limits the distance that can be measured. To eliminate bias of potentially inflating numbers, I decided I had to count individual animal specimens, not sightings, and so I chose cats to study since I knew I could tell them apart, and I knew there were a few around my area.

I briefly thought about including a computer vision aspect in this project to virtually 'tag' animals, and then you could scale to animals that are more difficult to distinguish, but I do not have the patience to work on that, and this was just for fun, so.. If someone out there would like to tackle that and somehow combine our projects that would be exciting, perhaps.


# distance-sampling
point based distance sampling formula

good for studying populations of:
- solitary, nocturnal animals
- visibly unique individuals



