#Q2:take 3 number as input from a user as 3 side of a triangle
#and check whether it will create a triagle or not

x=int(input("1side : "))
y=int(input("2side : "))
z=int(input("3side : "))

if (x+y)>z and (y+z)>x and (x+z)>y:
    print("x ,y and z can make a triangle")

else:
    print("x , y and z can't make a triangle")