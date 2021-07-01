#METHOD 1

list=["macbook","macbook pro","iphone","oneplus","samsung","huawei"]
for i in list:
    print(i," and ",end="")
print(" others are very popular phones")

#METHOD 2


list=["macbook","macbook pro","iphone","oneplus","samsung","huawei"]

a=" and ".join(list)
print(a,"and others are very popular phones")