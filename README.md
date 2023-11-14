# Dist samp

Attempting to perform distance sampling studies using trail cam footage.

A few things just to be clear:
- I am not a scientist, just a curious programmer.
- This project has not been peer reviewed (yet?)
- I am sharing this in hopes that someone smarter can point out any mistakes I've made and help me improve this.
- If you intend to use my scripts for your own studies I highly recommend doing additional research and modifying the code as needed.
- The trail cam approach is best only for solitary, uniquely identifiable animals -- see below for my explanation on that.
- I am not familiar with all methods of population estimating, I was attracted to distance sampling from a statistics point of view, and stayed for the animals. I am interested in learning about other methods to possibly derive other scripts/software.

Most of my understanding of distance sampling comes from:
- This website https://distancesampling.org/whatisds.html
- This youtube video and its followup https://www.youtube.com/watch?v=2kc4cU-iG1U

I've tried to apply what I know into a Python script, but I am hoping to iron some things out later. I intend to try the course at https://workshops.distancesampling.org/online-course/ to further my understanding, but that'll have to be when I have time.

I understand that observations can be recorded from a single point if you measure the radial distance from the observer to the subject. I paired this with calculating the area that a camera can cover by multiplying the lens field of view by a measured distance to a specific point. I used a trail cam with a fixed FOV of 120 degrees and it's aimed at a fence which firmly limits the distance that can be measured. To eliminate bias of potentially inflating numbers, I decided I had to count individual animal specimens, not sightings, and so I chose cats to study since I knew I could tell them apart, and I knew there were a few around my area.

I briefly thought about including a computer vision aspect in this project to virtually 'tag' animals, and then you could scale to animals that are more difficult to distinguish, but I do not have the patience to work on that, and this was just for fun, so.. If someone out there would like to tackle that and somehow combine our projects that would be exciting, perhaps.

I humbly attempted to address the fact that distance sampling is sensitive to animal movement; it doesn't really take into account the fact that they travel over time. If you could 3D scan the full survey region in an instant, this could be a lot more valid, but I've worked in photogrammetry before and I'm not aware of any cost effective way to do this. It defeats the purpose anyway of my idea to use trail cams alone as the observer. I had the idea to subtract the estimate area of the animal (per sighting) from the region area, so that animals cannot theoretically occupy the same space, but if you try out the script yourself you will see that this doesn't really have a large impact on the results. Maybe if the region area is very, very small it does. But for now the biggest factor is the sightings themselves. As put above, I'm not a scientist, but I'd love to hear from someone (anyone) if my ideas have any momentum or not.