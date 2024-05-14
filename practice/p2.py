fileobj=open("p1.py","r+")
with open("p1.txt","r") as fileobj:
    for line in fileonj.readlines():
        print(line.strip())