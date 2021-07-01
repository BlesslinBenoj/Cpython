a=1
b=2
c=sum((a,b))
#print(c)
def function1(a,b):
    average=(a+b)/2
    print(average)
    return average
#function1(7,9)

""" 

ACTUAL ARGUMENTS:
*position
*keyword
*Default
*variable length

"""

POSITION:
def biodata(name,age)
    print(name)
    print(age)
biodata("beno",19)


KEYWORD:
def biodata(age,name)
    print(name)
    print(age)
biodata(name="beno",age=19)

DEFAULT:
def biodata(name,age=19)
    print(name)
    print(age)
biodata("beno")


VARIABLE LENGTH:
def add(a,*b):
    for i in b:
        a=a+i
    print(a)
add(5,6,7,8,9,10)