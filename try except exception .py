print("enter the first number")
num1=input()
print("enter the second number")
num2=input()
try:
    print("the sum of two number is",int(num1)+int(num2))
except Exception as e:
    print(e)
    print("this is very important line")