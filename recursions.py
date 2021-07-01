import sys
sys.setrecursionlimit(2000)
i=0
def wishme():
    global i
    i=i+1
    print("good morning",i)
    wishme()
wishme()