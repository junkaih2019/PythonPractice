class User:
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("I'm " + self.first_name + " " + self.last_name + ".")
        print("My age is " + str(self.age))

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name + ".")

    def incerment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super(Admin, self).__init__(first_name, last_name, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin is able to do the following things:")
        for privilege in self.privileges:
            print(privilege)


aAdmin = Admin("wang", "xiao", 19)
aAdmin.show_privileges()
