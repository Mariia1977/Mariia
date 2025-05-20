import json

# Файл, де будемо зберігати список справ
TODO_FILE = "todo_list.json"

# Функція для завантаження списку справ
def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Функція для збереження списку справ
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Основна функція
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Додати завдання")
        print("2. Показати список")
        print("3. Видалити завдання")
        print("4. Вийти")
        choice = input("Оберіть дію: ")

        if choice == "1":
            task = input("Введіть нове завдання: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Завдання додано!")

        elif choice == "2":
            if tasks:
                print("\nСписок завдань:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("📭 Список порожній!")

        elif choice == "3":
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    index = int(input("Введіть номер завдання для видалення: ")) - 1
                    if 0 <= index < len(tasks):
                        removed_task = tasks.pop(index)
                        save_tasks(tasks)
                        print(f"🗑️ Завдання '{removed_task}' видалено!")
                    else:
                        print("❌ Невірний номер!")
                except ValueError:
                    print("❌ Введіть число!")

        elif choice == "4":
            print("👋 До побачення!")
            break
        else:
            print("❌ Невірний вибір!")

if __name__ == "__main__":
    main()
