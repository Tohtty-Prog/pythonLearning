import os

class BetterTodo:
    def __init__(self, filename='todo.txt'):
        self.filename = filename
        self.tasks = []
        self.check_file()
        self.load_data()

    def check_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'x') as f:
                pass
    
    def load_data(self):
        with open(self.filename, 'r') as f:
            for line in f:
                self.tasks.append(line)

    def add_task(self,task):
        with open(self.filename, 'a') as f:
            f.write(task + '\n')
            self.tasks.append(task)

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            with open(self.filename, 'w') as f:
                for task in self.tasks:
                    f.write(task)
        else:
            print("Invalid task number.")

    def __str__(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task.strip()}")
        return ""

def main():
    todo = BetterTodo()
    #todo.add_task("Buy groceries")
   # todo.add_task("Call Alice")
    todo.remove_task(1)
    print(todo)    
if __name__ == "__main__":
    main()