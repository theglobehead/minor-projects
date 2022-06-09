import os
from typing import List


class TextMessage:
    def __init__(self, user: str, message: str) -> None:
        self.user = user
        self.message = message


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.messages: List[TextMessage] = []
        server.register_user(self)

    def get_message(self, message: TextMessage):
        self.messages.append(message)

    def send_message(self, message_text: str):
        message = TextMessage(user=self.name, message=message_text)
        server.dispatch_message(message=message)

    def display_messages(self):
        for message in self.messages:
            name = message.user
            if name == self.name:
                name = "You"
            print(f"{name}: {message.message}")


class Server:
    def __init__(self) -> None:
        self.users: List[User] = []

    def register_user(self, user: User):
        self.users.append(user)

    def dispatch_message(self, message: TextMessage):
        for user in self.users:
            user.get_message(message=message)

class App:
    def __init__(self) -> None:
        self.user: User = None
        self.running = True

    def switch_user(self, name: str) -> bool:
        for user in server.users:
            if user.name == name:
                self.user = user
                return True
        print("Could not find user!")
        return False

    def main_loop(self):
        if self.user == None:
            if self.switch_user(name=input("Enter your username: ")):
                print(f"Logged in as {self.user.name}")
            return
            
        print("press c to change user, s to send message, e to exit and d to display messages")
        command = input("type here: ")
        if command == "c":
            if self.switch_user(name=input("name: ")):
                os.system('cls' if os.name=='nt' else 'clear')
        elif command == "s":
            self.user.send_message(message_text=input("message_text: "))
        elif command == "e":
            self.running = False
        elif command == "d":
            os.system('cls' if os.name=='nt' else 'clear')
            self.user.display_messages()
        else:
            print("unknown command!")


if __name__ == "__main__":
    server = Server()
    app = App()

    user1 = User(name="user1")
    user2 = User(name="user2")
    user3 = User(name="user3")

    while app.running:
        app.main_loop()