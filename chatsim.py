class User:
    def __init__(self,name):
        self.name = name

class Chat:
    def __init__(self):
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, content, sender, receiver):
        msg: Message = Message(content, sender, receiver)
        self.messages.append(msg)

    def show_message(self):
        for msg in self.messages:
            print(f"{msg.sender.name} to {msg.receiver.name}: {msg.content}")

class Message:
    def __init__(self,content,sender,receiver):
        self.content = content
        self.sender = sender
        self.receiver = receiver

    
def main():
    chat = Chat()
    user1 = User("Alice")
    user2 = User("Bob")
    chat.add_user(user1)
    chat.add_user(user2)
    chat.send_message("Hello, Bob!", user1, user2)
    chat.show_message()

if __name__ == "__main__":
    main()