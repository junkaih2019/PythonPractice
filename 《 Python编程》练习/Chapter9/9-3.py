class User():
    def __init__(self,first_name,last_name,age):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("I'm " + self.first_name + " " + self.last_name + ".")
        print("My age is " + str(self.age))

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name + ".")


wang = User("wang", "xiaoming", 12)
lu = User("lu", "linlin", 13)
wang.describe_user()
wang.greet_user()
lu.describe_user()
lu.greet_user()
