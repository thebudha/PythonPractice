# To do list application


def print_menu():
    print("\nTodo List Menu:")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")


def get_choice():
    while True:
        choice = input("Enter your choice (1-4): ")
        valid_choices = ("1", "2", "3", "4")
        if choice not in valid_choices:
            print("Invalid choice!")
            continue
        return choice


def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return

    print('\nCurrent tasks:')
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    while True:
        task = input("Enter a new task: ").strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print("Task cannot be empty!")


def remove_task(tasks):
    display_tasks(tasks)

    while True:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("Task removed.")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid task number!")


def main():
    tasks = []

    while True:
        print_menu()
        choice = get_choice()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
