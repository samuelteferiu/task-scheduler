import datetime

tasks = []

def due_date():
    while True:
        try:
            date_str = input("Enter due date and Time (YYYY-MM-DD HH:MM:SS): ")
            due_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            return due_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")

def priority():
    while True:
        try:
            priority = int(input("Enter priority number (1(low)-5(high)): "))
            if 1 <= priority <= 5:
                return priority
            else:
                print("Invalid priority. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date_value = due_date()
    priority_level = priority()
    task = {
        'title': title,
        'description': description,
        'due_date': due_date_value,
        'priority': priority_level,
        'completed': False
    }
    tasks.append(task)
    print("Task added successfully!")

def display_upcoming_tasks():
    print("Upcoming tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "completed" if task["completed"] else "pending"
        print(f"{index}. [{status}] Task: {task['title']}, Due Date: {task['due_date']}, Priority: {task['priority']}")

def mark_task_as_completed():
    display_upcoming_tasks()
    task_index = int(input("Enter the task number to mark as completed or reschedule: ")) - 1
    if 0 <= task_index < len(tasks):
        choice = input("Do you want to reschedule the task? (Y/N): ")
        if choice.upper() == 'Y':
            new_due_date = input("Enter the new due date and time (YYYY-MM-DD HH:MM:SS): ")
            tasks[task_index]['due_date'] = new_due_date
            print(f"Task '{tasks[task_index]['title']}' is rescheduled to {new_due_date}")
        elif choice.upper() == 'N':
            tasks[task_index]['completed'] = True
            print(f"Task '{tasks[task_index]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

def check_reminders():
    current_time = datetime.datetime.now()
    upcoming_tasks = []
    for task in tasks:
        due_date = task['due_date']
        if not task['completed'] and (due_date - current_time) <= datetime.timedelta(days=1):
            upcoming_tasks.append(task)
    if upcoming_tasks:
        print("\nReminder: You have the following tasks due within the next 24 hours:")
        for index, task in enumerate(upcoming_tasks, start=1):
            print(f"{index}. Task: {task['title']}, Due Date: {task['due_date']}, Priority: {task['priority']}")
    else:
        print("\nNo upcoming tasks within the next 24 hours.")

def main():
    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. Display Upcoming Tasks")
        print("3. Mark Task as Completed or Reschedule")
        print("4. Check Reminders")
        print("5. Quit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            display_upcoming_tasks()
        elif choice == '3':
            mark_task_as_completed()
        elif choice == '4':
            check_reminders()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()