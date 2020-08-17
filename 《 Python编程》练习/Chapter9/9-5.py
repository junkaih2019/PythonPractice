class User():
    def __init__(self,first_name,last_name,age):
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


aUser = User("wang", "xiaoming", 10)
aUser.incerment_login_attempts()
aUser.incerment_login_attempts()
aUser.incerment_login_attempts()
aUser.incerment_login_attempts()
aUser.incerment_login_attempts()
print("login_attempts: " + str(aUser.login_attempts))
aUser.reset_login_attempts()
print("login_attempts: " +str(aUser.login_attempts))
