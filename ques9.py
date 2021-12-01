def volumnofcylinder(d,h):
    print(f"The Diameter of Cylinder is {d}")
    print(f"The Height of Cylinder is {h}")
    pi=3.141
    volumn=(pi*(d*d)*h)/4
    print(f"The Volumn of Cylinder is {volumn}")
d=int(input("Enter The Diameter Of Cylinder:"))
h=int(input("Enter The Height Of Cylinder:"))
volumnofcylinder(d,h)