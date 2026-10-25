from practice.database import users
from hashlib import sha256



print("=============================")
print("WELCOME TO THE CLASSROOM APP")
print("=============================")

username = input("Please enter your username: ")
user_password = sha256(input("Please enter your user password: ").encode())

# print(user_password.hexdigest())

def user_auth(user_name,password):

    for user in users:

        if user["user_name"] == user_name and user["password"] == password.hexdigest():

            print(f"\nHi {user["user_name"]} you logged in successfully")
            
            print(f"\nYour grade is {user["grade"]}")
            break
            
        else:
            print("Incorrect Username or Password")
            break
    

user_auth(username,user_password)