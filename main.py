print("===== STUDENT PRODUCTIVITY MANAGER =====")

tasks = []
daily_target = 5


def add_task():
    print()
    print("===== ADD TASK =====")

    task_name = input("Enter task: ")

    while task_name.strip() == "":
        print("Task cannot be empty.")
        task_name = input("Enter task: ")

    priority = input("Enter priority (High/Medium/Low): ").capitalize()

    while priority not in ["High", "Medium", "Low"]:
        print("Please enter High, Medium, or Low.")
        priority = input("Enter priority (High/Medium/Low): ").capitalize()

    tasks.append({
        "task": task_name,
        "priority": priority
    })

    print("Task added successfully!")


def show_tasks():
    print()
    print("===== YOUR TASKS =====")

    if len(tasks) == 0:
        print("No tasks added yet.")
        return

    for i, task in enumerate(tasks, start=1):
        print(i, ".", task["task"])
        print("Priority:", task["priority"])
        print()


def edit_task():
    print()
    print("===== EDIT TASK =====")

    if len(tasks) == 0:
        print("No tasks available to edit.")
        return

    show_tasks()

    try:
        task_number = int(input("Enter task number to edit: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        task = tasks[task_number - 1]

        new_name = input("Enter new task name: ")

        if new_name.strip() != "":
            task["task"] = new_name

        new_priority = input(
            "Enter new priority (High/Medium/Low): "
        ).capitalize()

        while new_priority not in ["High", "Medium", "Low"]:
            print("Please enter High, Medium, or Low.")
            new_priority = input(
                "Enter new priority (High/Medium/Low): "
            ).capitalize()

        task["priority"] = new_priority

        print("Task updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    print()
    print("===== DELETE TASK =====")

    if len(tasks) == 0:
        print("No tasks available to delete.")
        return

    show_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        deleted_task = tasks.pop(task_number - 1)

        print("Deleted:", deleted_task["task"])

    except ValueError:
        print("Please enter a valid number.")


def search_task():
    print()
    print("===== SEARCH TASK =====")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    search = input("Enter task name to search: ").lower()

    found = False

    for i, task in enumerate(tasks, start=1):
        if search in task["task"].lower():
            print()
            print(i, ".", task["task"])
            print("Priority:", task["priority"])
            found = True

    if not found:
        print("No matching task found.")


def show_summary(study_time):
    print()
    print("===== PRODUCTIVITY SUMMARY =====")

    print("Total Tasks:", len(tasks))
    print("Study Time:", study_time, "hours")
    print("Daily Target:", daily_target, "hours")

    remaining_time = daily_target - study_time

    if remaining_time <= 0:
        print("Study target completed!")
    else:
        print("Remaining Study Time:", remaining_time, "hours")


def save_tasks():
    with open("tasks.txt", "w") as file:

        for task in tasks:
            file.write(
                task["task"]
                + " | Priority: "
                + task["priority"]
                + "\n"
            )

    print("Tasks saved successfully!")


print()

name = input("Enter your name: ")
goal = input("What is your main study goal today? ")

study_time = 0

while True:

    print()
    print("===== MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Update Study Time")
    print("7. View Productivity Summary")
    print("8. Save Tasks")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_task()

    elif choice == "2":

        show_tasks()

    elif choice == "3":

        edit_task()

    elif choice == "4":

        delete_task()

    elif choice == "5":

        search_task()

    elif choice == "6":

        try:
            study_time = float(
                input("How many hours did you study today? ")
            )

            if study_time < 0:
                print("Study time cannot be negative.")
                study_time = 0
            else:
                print("Study time updated!")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "7":

        show_summary(study_time)

    elif choice == "8":

        save_tasks()

    elif choice == "9":

        print()
        print("Saving your tasks...")
        save_tasks()

        print("Goodbye,", name + "!")
        print("Keep working toward:", goal)
        break

    else:

        print("Invalid choice. Please select 1-9.")