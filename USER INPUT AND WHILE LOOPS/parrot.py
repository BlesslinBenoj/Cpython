
#1

message = input("tell me something,and i will repeat it back to you:")
print(message)


#2

prompt = "tell me something,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

#3

prompt = "tell me something,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)











































































































