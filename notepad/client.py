import requests

#BASE_URL = "http://127.0.0.1:8000"
BASE_URL = "http://131.163.89.76:8000"


def add_note():
    content = input("Write note: ")

    response = requests.post(f"{BASE_URL}/notes",json={"content": content})
    
    print(response.json())


def show_notes():
    response = requests.get(f"{BASE_URL}/notes")
    notes = response.json()

    if not notes:
        print("No notes found.")
        return

    for note in notes:
        print(f"{note['id']}. {note['content']}")


def main():
    while True:
        print("\n1. Add note")
        print("2. Show notes")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            print("Bye")
            break
        else:
            print("Unknown choice")


if __name__ == "__main__":
    main()