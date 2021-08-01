number = input("Enter a number,and i'll tell you if it is even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"\nThe given number {number} is even.")
else:
    print(f"\nThe given number {number} is odd.")
