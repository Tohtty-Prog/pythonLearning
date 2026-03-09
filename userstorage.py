import json
import os


def main():
    if not os.path.exists("users.json"):
        with open("users.json", 'w') as f:
            json.dump({"users": []}, f, indent=4)
    else:
        pass


    while True:
        print("\n1. Add user")
        print("2. Show users")
        print("3. Exit")
        choice = input("choice: ")

        if choice == '1':
            username = input("give username: ")
            age = input("give age: ")
            with open("users.json", 'r') as f:
                data = json.load(f)
                new_user = {
                    "username":  username,
                    "age": age
                }
                data["users"].append(new_user)

            with open("users.json", "w") as f:
                json.dump(data,f, indent=4)
        elif choice == '2':
            with open("users.json", 'r') as f:
                data = json.load(f)
            if not data["users"]:
                print("No users found")
                continue

            for i,user in enumerate(data["users"], start=1):
                print(f"{i}. {user['username']} ({user['age']})")
        elif choice == '3':
            print("Good bye")
            break
        else:
            print("Unknown choice")

if __name__ == "__main__":
    main()