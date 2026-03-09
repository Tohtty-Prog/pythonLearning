import os
import json

def check_file():
    if not os.path.exists("userdata.json"):
        with open("userdata.json", 'w') as f:
            json.dump({"users": []}, f, indent=4)

def register(user,password):
    with open("userdata.json", 'r') as f:
        data = json.load(f)

        new_data = {
            "username": user,
            "password": password
        }

        data["users"].append(new_data)
    
    with open("userdata.json", 'w') as f:
        json.dump(data,f,indent=4)

def login(user,password):
    with open("userdata.json", 'r') as f:
        data = json.load(f)
    
    if not data["users"]:
        print("No users")
        return
    
    for saved_users in data["users"]:
        if saved_users["username"] == user and saved_users["password"] == password:
            print("You logged in")
            return
    print("Username or password was incorrect")



def show_users():
    with open("userdata.json", 'r') as f:
        data = json.load(f)

    if not data["users"]:
        print("no users")
        return
    
    for i, user in enumerate(data["users"], start=1):
        print(f"{i}. {user['username']}")


def main():
    check_file()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Show users")
        print("4. Exit")

        choice = input("Choice: ")
        if choice == '1':
            user = input("Type username: ")
            password = input("Type password: ")

            register(user,password)
        elif choice == '2':
            user = input("type username: ")
            password = input("type password: ")
            login(user,password)
        elif choice == '3':
            show_users()
        elif choice == '4':
            print("Bye")
            break
        else:
            print("unknown choice")



if __name__ == "__main__":
    main()