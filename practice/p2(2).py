fileobj=open("p1.py","r+")
with open("p1.txt","r") as fileobj:
    for line in fileobj.readlines():
        print(line.strip())




import csv
filer=open("p2.txt")
p=csv.reader(filer)
for i in p:
    print(i)
    id,name,salary