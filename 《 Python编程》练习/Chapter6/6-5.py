river_country = {
    'mekong': 'china',
    'nile': 'egypt',
    'missie': 'america',
    }
for river, country in river_country.items():
    print("The " + river.title() + "runs through " + river.title())

for river in river_country.keys():
    print(river)

for country in river_country.values():
    print(country)
