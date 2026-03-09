class TodoList():
    def __init__(self):
        self.todos = []
    
    def add_todo(self,todo):
        self.todos.append(todo)

    def remove_todo(self,todo):
        if todo in self.todos:
            self.todos.remove(todo)
        else:
            print(f"{todo} not found in the todo list.")
    def display_todos(self):
        if not self.todos:
            print("No todos in the list.")
        else:
            print("Todo List:")
            for idx, todo in enumerate(self.todos, start=1):
                print(f"{idx}. {todo}")

def main():
    todo_list = TodoList()
    while True:
        print("\nTodo List Application")
        print("1. Add Todo")
        print("2. Remove Todo")
        print("3. Display Todos")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            todo = input("Enter a new todo: ")
            todo_list.add_todo(todo)
            print(f"'{todo}' added to the list.")
        elif choice == '2':
            todo = input("Enter the todo to remove: ")
            todo_list.remove_todo(todo)
        elif choice == '3':
            todo_list.display_todos()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()