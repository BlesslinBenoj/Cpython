def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)
result=factorial(5)
print(result)