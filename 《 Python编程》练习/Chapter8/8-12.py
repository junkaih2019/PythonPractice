def sandwich_order(*ingredients):
    print("Your sandwich will be made of the following ingredients:")
    for ingredient in ingredients:
        print(ingredient)


sandwich_order('a', 'a', 'a')
sandwich_order('a', 'v', 'c')
sandwich_order('a', 's', 'w')