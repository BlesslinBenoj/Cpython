age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 35:
    price = 40
elif age >= 35:
    price = 60
print(f"Your admission cost is ${price}.")