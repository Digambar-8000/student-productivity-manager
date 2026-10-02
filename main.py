print("===== STUDENT PRODUCTIVITY MANAGER =====")

tasks = []

name = input("Enter your name: ")
goal = input("What is your main study goal today? ")

def show_tasks():
    print()
    print("===== YOUR TASKS =====")

    for task in tasks:
        print(task)

for i in range(3):
    task = input("Enter a Task:")
    tasks.append(task)

show_tasks()

print("Total Tasks:", len(tasks))

priority = input("What is the task priority? (High/Medium/Low): ")
completed = input("Did you complete this task? (yes/no): ")

study_time = float(input("How many hours will you study today? "))
remaining_time = 5 - study_time

print()
print("Hello,", name)
print("Today's goal:", goal)
print()

print("Priority:", priority)
print("Study Time:", study_time, "hours")
print("Remaining Time:", remaining_time, "hours")

if remaining_time <= 0:
    print("You have Completed your study time for today!")
else:
    print("you have", remaining_time, "hours left to study today!")

if completed.lower() == "yes":
    print("Great Job! " + name + "! You completed your task for today.")
else:
    print("Dont worry!" + name + "! You can try again tomorrow.")

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

    