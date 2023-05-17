tasks = []

while True:
    command = input()
    if command == "End":
        break

    current_command = command.split("-")

    importance = int(current_command[0])
    note = current_command[1]
    tasks.append((importance, note))
sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)