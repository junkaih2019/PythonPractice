pizzas = ['apple', 'banana', 'pine']
friend_pizzas = pizzas[:]
pizzas.append('tang')
friend_pizzas.append('sugar')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My fiend's pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
