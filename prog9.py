

import math
def calculate_volume(diameter, height):
    # the formula for volume of cone V = πr^2h/3
    radius = diameter/2
    volume = math.pi * radius ** 2 * (height / 3)
    print("Mr Survivor: the volume of a cone with a diameter of {} and height of {} is {} herfs ^3".format(diameter, height, volume))

def calculate_surfacearea(diameter, height):
     #The formula for surface area A = πr(r + sqr(h^2 + r^2))
     #The base area A = πr^2

     radius = diameter/2
     base_area = math.pi * radius ** 2
     surface_area = math.pi * radius * (radius + math.sqrt(height ** 2 + radius ** 2))
     surface_area_side = surface_area - base_area
     print("The surface area = {} herfs ^2 including the base.".format(surface_area))
     print("The surface area of just the sides = {} herfs ^2 ".format(surface_area_side))


def main():
    #prompt the user to enter non negative diameter and height
    diameter = float(input("Input base Diameter (herfs): "))
    #check that the diameter is non negative
    while diameter < 0:
        diameter = float(input("Input base Diameter (herfs): "))

    #check that the height is non negative
    height = float(input("Input height (herfs): "))
    while height < 0 :
        height = float(input("Input height (herfs): "))

    #call function to calculate volume and area respectively and passing diameter and height to them
    calculate_volume(diameter, height)
    calculate_surfacearea(diameter, height)

main()
