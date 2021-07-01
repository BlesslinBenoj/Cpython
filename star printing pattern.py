print("How many rows of stars do you want?")
rows=int(input())
print("enter 1 for straight pattern and 0 for reverse pattern")
pattern=int(input())
new=bool(pattern)

if new==True:
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print("*",end="")
        print()

elif new==False:
    for i in range(rows,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()