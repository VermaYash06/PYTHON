#1q)we have to take input no. from user as integer'''
#for starting 10 units price is 50
#next 20 20rs
#for rest 10rs
#calculate total price

x=int(input("enter unit"))

if (x<=10):
    print("price is : ",10*50)

elif (x<=30):
    print("price is : ",(x-10)*(20)+(10*50))

else:
    print("price is : ",(10*50)+(20*20)+(x-30)*(10))