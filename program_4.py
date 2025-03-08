# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
def distance_problem(x1, x2, y1, y2, z1, z2):
    dist1 = (x1, y1, y2)
    dist2 = (x2, y2, z2)
    distance = ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
    print ("First Coordinates: ", dist1)
    print("Second Coordinates:", dist2)
    print ("Distance:", distance)
def main():
   try:
       cor1 = int(input("X1 = "))
       cor2 = int(input("X2 = "))
       cor3 = int(input("Y1 = "))
       cor4 = int(input("Y2 = "))
       cor5 = int(input("Z1 = "))
       cor6 = int(input("Z2 = "))
       distance_problem(cor1, cor2, cor3, cor4, cor5, cor6)
   except:
       print ("Error: Try again")

main()