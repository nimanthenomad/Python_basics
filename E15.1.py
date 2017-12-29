import math
def distance_between_points(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance
print distance_between_points(10,12,4,5)
