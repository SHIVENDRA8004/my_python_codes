def areaofcylinder(d,h):
    print(f"The Diameter of Cylinder is {d}")
    print(f"The Height of Cylinder is {h}")
    pi=3.141
    area=pi*d*(h+(d/2))
    print(f"The Area of Cylinder is {area}")
d=int(input("Enter The Diameter Of Cylinder:"))
h=int(input("Enter The Height Of Cylinder:"))
areaofcylinder(d,h)