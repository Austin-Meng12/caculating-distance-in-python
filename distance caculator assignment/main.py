import math


print("WELCOME TO DISTANCE CACULATOR")
#input variables/values
x1 = float(input("x1:"))
y1 = float(input("y1:"))
x2 = float(input("x2:"))
y2 = float(input("y2:"))

#process
distance = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**0.5
#output variables
print("distance between the points is  " + str(distance) )

