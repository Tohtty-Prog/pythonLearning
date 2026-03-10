import requests

BASE_URL = "http://127.0.0.1:8000"

def get_messages():
    response = requests.get(f"{BASE_URL}/messages")
    if response.status_code == 200:
        messages = response.json()
        print("Viestit: ")
        for message in messages:
            print(f"{message['id']}: {message['username']} -> {message['text']}")
    else:
        print(f"virhe viestien saannissa", response.status_code, response.text)

def send_message():
    username = input("Whats ur username: ")
    text = input("Viesti,jonka lähetät: ")

    data = {
        "username": username,
        "text": text
    }
    response = requests.post(f"{BASE_URL}/messages", json=data)

    if response.status_code == 200:
        print("Viesti lähetetty")
        print(response.json())
    else:
        print("Virhe viestin lähetyksessä: ", response.json())

def delete_message():
    message_id = input("Anna poistettavan viestin id: ")
    response = requests.delete(f"{BASE_URL}/messages/{message_id}")
    if response.status_code == 200:
        print("Viesti on poistettu", response.json())
    else:
        print("Virhe viestin poistossa: ", response.status_code, response.text)

def main():
    while True:
        print("\n1. Näytä kaikki viestit")
        print("2. Lähetä viesti")
        print("3. poista viesti")
        print("4. Lopeta")

        choice = input("choice: ")
        if choice == '1':
            get_messages()
        elif choice == '2':
            send_message()
        elif choice == '3':
            delete_message()
        elif choice == '4':
            print("Bye")
            break
        else:
            print("Unknown choice")


if __name__ == "__main__":
    main()