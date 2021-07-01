import time
initial=time.time()
k=0
while k<45:
    print("i am a good boy")
    k=k+1
print("time for execution of while loop:",time.time()-initial)
initial2=time.time()
for i in range(45):
    print("i am a good boy")
print("time for execution  of for loop:",time.time()-initial2)