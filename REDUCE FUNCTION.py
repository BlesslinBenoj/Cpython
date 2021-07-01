#METHOD 1:


list1=[1,2,3,4,5,]
num=0
for i in list1:
    num=num+i
print(num)


#METHOD 2:
#USING REDUCE FUNCTION:

from functools import reduce

listt1=[1,2,3,4,5,]
num=reduce(lambda x,y:x+y,list1)
print(num)