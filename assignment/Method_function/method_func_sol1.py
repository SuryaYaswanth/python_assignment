def volume(r):
    pi=3.14
    res=(4/3)*pi*(r**3)
    return res

radius=int(input("Enter the radius:"))
print("The Volume of Sphere is:",volume(radius))
