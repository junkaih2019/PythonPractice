cities = {
    'beijin': {
        'country': 'china',
        'population': '1000',
        'fact': 'a',
    },

    'shanghai': {
        'country': 'china',
        'population': '2000',
        'fact': 'b',
    },

    'taiyuan': {
        'country': 'china',
        'population': '3000',
        'fact': 'c',
    },
}
for city_name, city_info in cities.items():
    print("\ncity: " + city_name)
    print("\tcountry: " + city_info['country'])
    print("\tpopulation: " + city_info['population'])
    print("\tfact: " + city_info['fact'])