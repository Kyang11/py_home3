



import math

def house_area():
    length=float(input("Enther the length: "))
    width=float(input("Enther the Width: "))
    total_area= length*width
    print(f"The total area is: {total_area} ")
    return house_area
print(house_area())

def circumference():
    diameter1 = float(input("Enther the diameter: "))
    pi=math.pi
    total_circumference= diameter1*pi
    print(f"The total circumference is: {total_circumference} ")
    return circumference
print(circumference())
   



