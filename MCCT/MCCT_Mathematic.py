#1.print()


#2.sum()

num1 = 2
num2 = 3
print(f"sum= {sum([num1+num2])}")

#round 
num3 = 10.11122
print(round(num3))

#abs()--> Abosolute math
print(abs(-25))
#Here, abs() removes the negative sign and returns the distance from zero.

#Summary: abs(x) returns the positive value of x (or 0 if x is zero).

import  math

r = 10
area_circle = math.pi * r ** 2
print(area_circle)

d = 28
area = math.pi * (d/2) ** 2
print(f"area of circle = {float(area):.2f}")

user1 = float(input("enter your number"))
user2 = float(input("enter your number"))

print("Minimum = {min(user1,user2)}")
print("Maxmimum = {max(user1,user2)}")

print(f"Sum = {sum([user1+user2])}")
print(f"power = {math.pow(user1,user2)}")



