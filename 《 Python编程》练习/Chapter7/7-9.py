sandwich_orders = ['tuna', 'pastrami', 'chicken','pastrami', 'ham','pastrami',]
print("Pastrami sode out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    print(sandwich + ' sandwich')
