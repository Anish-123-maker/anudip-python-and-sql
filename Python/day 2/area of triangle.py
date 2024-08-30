b=int(input("Enter the base of the triangle: "))
h=int(input("Enter hight of the triangle: "))
def Area(b,h):
    area=0.5*b*h
    return area

area=Area(b,h)
print(f"The area of the triangle is: {area}")
