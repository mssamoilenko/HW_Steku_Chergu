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

#task2
class StringStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, string):
        if not self.is_full():
            self.stack.append(string)
            print(f"Рядок '{string}' додано в стек.")
        else:
            print("Стек переповнений!")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Стек порожній!")

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) >= self.size

    def clear(self):
        self.stack.clear()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

class StringQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def enqueue(self, string):
        if not self.is_full():
            self.queue.append(string)
            print(f"Рядок '{string}' додано в чергу.")
        else:
            print("Черга переповнена!")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Черга порожня!")

    def count(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.size

    def clear(self):
        self.queue.clear()

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

def main():
    structure_type = input("Виберіть структуру даних (1 - Стек, 2 - Черга): ")

    if structure_type == '1':
        structure_size = int(input("Введіть максимальний розмір стека: "))
        string_stack = StringStack(structure_size)
        current_structure = string_stack
        current_structure_name = "стек"
    elif structure_type == '2':
        structure_size = int(input("Введіть максимальний розмір черги: "))
        string_queue = StringQueue(structure_size)
        current_structure = string_queue
        current_structure_name = "черга"
    else:
        print("Невірний вибір.")
        return

    while True:
        print(f"\nМеню для роботи з {current_structure_name}:")
        print("1. Додати рядок в структуру")
        print("2. Витягнути рядок з структури")
        print("3. Підрахувати кількість рядків у структурі")
        print("4. Перевірити чи порожня структура")
        print("5. Перевірити чи повна структура")
        print("6. Очищення структури")
        print("7. Подивитися верхній або перший рядок без витягування")
        print("8. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            string_value = input("Введіть рядок: ")
            if current_structure_name == "стек":
                current_structure.push(string_value)
            else:
                current_structure.enqueue(string_value)
        elif choice == '2':
            if current_structure_name == "стек":
                popped_value = current_structure.pop()
                if popped_value is not None:
                    print(f"Витягнуто рядок: {popped_value}")
            else:
                dequeued_value = current_structure.dequeue()
                if dequeued_value is not None:
                    print(f"Витягнуто рядок: {dequeued_value}")
        elif choice == '3':
            count = current_structure.count()
            print(f"Кількість рядків у структурі: {count}")
        elif choice == '4':
            empty_status = "порожня" if current_structure.is_empty() else "не порожня"
            print(f"Структура {empty_status}.")
        elif choice == '5':
            full_status = "повна" if current_structure.is_full() else "не повна"
            print(f"Структура {full_status}.")
        elif choice == '6':
            current_structure.clear()
            print("Структура очищена.")
        elif choice == '7':
            if current_structure_name == "стек":
                top_value = current_structure.peek()
            else:
                top_value = current_structure.peek()

            if top_value is not None:
                print(f"Верхній або перший рядок у структурі: {top_value}")
        elif choice == '8':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

main()