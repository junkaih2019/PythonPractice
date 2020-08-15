fav = {
    'wang': {
        'num1': 5,
        'num2': 4,
        'num3': 2,
    },
    'li': {
        'num1': 6,
        'num2': 4,
        'num3': 2,
    },
    'liu': {
        'num1': 7,
        'num2': 4,
        'num3': 2,
    },
}
for name,nums in fav.items():
    print("\n" + name + "'s lucky numbers are:")
    for num in nums.values():
        print(num)
