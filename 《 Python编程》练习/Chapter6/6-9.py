favorite_places = {
    'wang': {
        'place1': 'beijin',
        'place2': 'shanghai',
        'place3': 'tianjin',
    },

    'tang': {
        'place1': 'beihai',
        'place2': 'tangshan',
        'place3': 'yulin',
    }
}
for name, places in favorite_places.items():
    print(name + "'s favorite places are:")
    for place in places.values():
        print(place)
