# #step 1 - open file
#
# #step 2 - use loop numbers from 0 to 10; use example discussed in slide
# for M in range (11):
#     print (M, end=(""))
#
# #step 3 - write another loop to print numbers from 1 to 10
# for b in range(1,10):
#     print (b, end=(""))
#
# #step 4 - write another loop to print numbers from 1 to 10 but increments should be +2 rather than default +1
# for c in range (1, 10, 2):
#     print("c=", c)
#
# #step 5,6, 7 - now you will ask user to enter radius of the circle; using the input function
# import math
# radius=int(input("Enter the radius of a circle:"))
# math.pi
# Area=math.pi*radius**2
# print("Area=", Area)

#step 8, 9, 10 - enter length of rectangle - width of rectangle and calculate area of rectangle
length=int(input("Enter the length of a rectangle:"))
width=int(input("Enter the width of a rectangle:"))
Area_R=length*width
print(Area_R)

#step11 - modify step 7 and 10 to check the input parameters are greater than 0
if Area_R>0:
    print("Area_R=", Area_R)
else:
    print("you cannot compute area of the requested polygon")

