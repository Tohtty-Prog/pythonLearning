import requests
BASE_URL = "http://127.0.0.1:8000"

def get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    if response.status_code == 200:
        messages = response.json()
        print("Viestit: ")
        for message in messages:
            print(f"{message['id']}: Task:{message['description']}. Status:{message['completed']}")
    else:
        print(f"Jokin meni pieleen ", response.json(), response.status_code)

def make_task():
    task = input("Mikä tehtävä: ")
    data = {"description": task}

    response = requests.post(f"{BASE_URL}/tasks", json=data)
    if response.status_code == 200:
        print("Tehtävä lisätty")
        print(response.json())
    else:
        print("Lähetys epäonnistui: ", response.json(), response.status_code)

def find_task():
    task_id = input("Anna tehtävän id: ")

    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    if response.status_code == 200:
        message = response.json()
        print(f"{message['id']}: Task:{message['description']}. Status:{message['completed']}")
        print("Tehtävä löytyi")
    else:
        print("Tehtävää ei löytynyt. ", response.json(), response.status_code)

def delete_task():
    task_id = input("Anna tehtävän id: ")
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    if response.status_code == 200:
        print("Tehtävä poistettiin onnistuneesti")
    else:
        print("Tehtävää ei voitu poistaa tai ei löytynyt. ", response.json(), response.status_code)

def update_task():
    task_id = input("Anna tehtävän id: ")
    response = requests.patch(f"{BASE_URL}/tasks/{task_id}")

    if response.status_code == 200:
        print("Tehtävä on muutettu Tehdyksi")
    else:
        print("Tehtävää ei voitu päivittää tai ei löytynyt. ", response.json(), response.status_code)

def main():
    while True:
        print("\n1. Luo tehtävä")
        print("2. Näytä kaikki tehtävät")
        print("3. Näytä tehtävä")
        print("4. Poista tehtävä")
        print("5. Päivitä tehtävä")
        print("6. Exit")
        choice = input("Choice: ")

        if choice == '1':
            make_task()
        elif choice == '2':
            get_tasks()
        elif choice == '3':
            find_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            update_task()
        elif choice == '6':
            print("Bye")
            break
        else:
            print("Unknown choice")
if __name__ == "__main__":
    main()