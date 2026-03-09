import os

def create_check_file():
    if not os.path.exists("testi.txt"):
        f = open("testi.txt", 'x')
        f.close()

def write_data(content):
    with open("testi.txt", 'a') as f:
        f.write(f"{content}\n")

def read_data():
    with open("testi.txt", 'r') as f:
        for line in f:
            print(line)

def main():
    create_check_file()
    while True:
        print("Take note")
        choice = input("Do u want to write or read the notes(w/r): )")
        if choice == 'r':
            read_data()
        elif choice == 'w':
            content = input("Write the staff u want to store: ")
            write_data(content)
        elif choice == 'q':
            print("Bye")
            break
        else:
            print("Unknown choice")

if __name__ == "__main__":
    main()
