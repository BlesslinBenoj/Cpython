"""
#1

def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('pepperoni','cheese','mushroom')

#2

def make_pizza(*toppings):
    print("\nMaking a pizza with the following topping:")
    for topping in toppings:
        print(f" - {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','cheese')

"""
#3

def make_pizza(size,*toppings):
    print(f"Making a {size}- inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")





















