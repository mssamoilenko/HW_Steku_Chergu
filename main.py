#task1
class UserManagement:
    def __init__(self):
        self.users = {}
        self.deleted_users_stack = []
        self.password_change_queue = []

    def add_user(self, username, password):
        if username in self.users:
            print("Користувач вже існує.")
        else:
            self.users[username] = password
            print(f"Користувача {username} додано.")

    def remove_user(self, username):
        if username in self.users:
            self.deleted_users_stack.append((username, self.users.pop(username)))
            print(f"Користувача {username} видалено.")
        else:
            print("Користувача не знайдено.")

    def restore_user(self):
        if self.deleted_users_stack:
            username, password = self.deleted_users_stack.pop()
            self.users[username] = password
            print(f"Користувача {username} відновлено.")
        else:
            print("Немає користувачів для відновлення.")

    def user_exists(self, username):
        return username in self.users

    def change_username(self, old_username, new_username):
        if old_username in self.users:
            self.users[new_username] = self.users.pop(old_username)
            print(f"Логін змінено з {old_username} на {new_username}.")
        else:
            print("Користувача не знайдено.")

    def change_password(self, username, new_password):
        if username in self.users:
            self.password_change_queue.append((username, new_password))
            print(f"Пароль для {username} змінено, але чекає на обробку.")
        else:
            print("Користувача не знайдено.")

    def process_password_changes(self):
        if self.password_change_queue:
            username, new_password = self.password_change_queue.pop(0)
            self.users[username] = new_password
            print(f"Пароль для {username} оновлено.")
        else:
            print("Немає запитів на зміну пароля.")

def main():
    um = UserManagement()

    while True:
        print("\nМеню:")
        print("1. Додати нового користувача")
        print("2. Видалити існуючого користувача")
        print("3. Перевірити чи існує користувач")
        print("4. Змінити логін наявного користувача")
        print("5. Змінити пароль наявного користувача")
        print("6. Відновити видаленого користувача")
        print("7. Обробити запити на зміну пароля")
        print("8. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            username = input("Введіть логін: ")
            password = input("Введіть пароль: ")
            um.add_user(username, password)
        elif choice == '2':
            username = input("Введіть логін для видалення: ")
            um.remove_user(username)
        elif choice == '3':
            username = input("Введіть логін для перевірки: ")
            exists = um.user_exists(username)
            print(f"Користувач {'існує' if exists else 'не існує'}.")
        elif choice == '4':
            old_username = input("Введіть старий логін: ")
            new_username = input("Введіть новий логін: ")
            um.change_username(old_username, new_username)
        elif choice == '5':
            username = input("Введіть логін для зміни пароля: ")
            new_password = input("Введіть новий пароль: ")
            um.change_password(username, new_password)
        elif choice == '6':
            um.restore_user()
        elif choice == '7':
            um.process_password_changes()
        elif choice == '8':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

main()