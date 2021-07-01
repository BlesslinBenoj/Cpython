i=1
while i<=5:
    print("blesslin benoj",end="")
    k=1
    while k<=4:
        print("subscribe",end="")
        k=k+1
    i=i+1
    print()
#Guess the number
    i = 15
    while True:
        x = int(input("guess the number:"))
        if x > 15:
            print("your guess is higher than the value")
            continue
        elif x < 15:
            print("your guess is lower than the value")
            continue
        else:
            print("correct number")
            break