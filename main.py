print("===== STUDENT PRODUCTIVITY MANAGER =====")

tasks = []

name = input("Enter your name: ")
goal = input("What is your main study goal today? ")

for i in range(3):
    task = input("Enter a task: ")
    tasks.append(task)

priority = input("What is the task priority? (High/Medium/Low): ")

completed = input("Did you complete this task? (yes/no): ")

study_time = float(input("How many hours will you study today? "))
remaining_time = 5 - study_time


def show_tasks():
    print()
    print("===== YOUR TASKS =====")

    for task in tasks:
        print(task)


print()
print("Hello,", name)
print("Today's goal:", goal)

show_tasks()

print()
print("===== STUDY DETAILS =====")
print("Priority:", priority)
print("Study Time:", study_time, "hours")
print("Remaining Time:", remaining_time, "hours")

if remaining_time <= 0:
    print("You have completed your study time for today!")
else:
    print("You have", remaining_time, "hours left to study today!")


if completed.lower() == "yes":
    print("Great job, " + name + "! You completed your task for today.")
else:
    print("Don't worry, " + name + "! You can try again tomorrow.")


with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

print()
print("Tasks saved successfully!")
print("===== END OF PROGRAM =====")