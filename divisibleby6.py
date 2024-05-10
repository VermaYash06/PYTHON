#Q3 Take two number from the user and check whether both the number are divisble by 6
#( divisibility rule say it should be divided by 2 and 3)

x=int(input("1st no : "))
y=int(input("2st no : "))

if(x%6==0 and y%6==0):
    print("both no. are divisible by 6")

else:
    print("both no. aren't divisible by 6")