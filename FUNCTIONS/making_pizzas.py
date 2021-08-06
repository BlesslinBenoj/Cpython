#1

import pizza

pizza.make_pizza(16,'pepperoni')

pizza.make_pizza(12,'mushrooms','cheese','green peppers')

#2

from pizza import make_pizza

make_pizza(19,'cheese','sause')


#3

from pizza import make_pizza as mp

mp(20,'cheese')


#4

import pizza as p

p.make_pizza(19,'mushrooms','cheese')


#5

from pizza import *

make_pizza(21,'cheese','mushrooms')































