def make_car(factor, series, **car_info):
    car = {}
    car['factor'] = factor
    car['series'] = series
    for key,value in car_info.items():
        car[key] = value
    return car


car = make_car('a','b',color = 'blue', tow_package = True)
print(car)
