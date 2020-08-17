class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("Cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is opening.")


my_restaurant = Restaurant("KFC","chiken")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

his_restaurant = Restaurant("KFC2","chiken2")
his_restaurant.describe_restaurant()
his_restaurant.open_restaurant()

her_restaurant = Restaurant("KFC3","chiken3")
her_restaurant.describe_restaurant()
her_restaurant.open_restaurant()
