class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("Cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is opening.")

    def set_number_served(self,number):
        self.number_served = number

    def incerment_number_served(self,increase):
        self.number_served += increase


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['a', 'b', 'c']

    def show_ice_cream(self):
        for flavor in self.flavors:
            print("We have " + flavor + " flavor's ice cream.")

my_ice_cream = IceCreamStand("KFC", "ICE")
my_ice_cream.show_ice_cream()
