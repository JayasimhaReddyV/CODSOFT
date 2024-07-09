#Task 1: Create a command-line Based To-do-list using Python

#importing datetime Module
import datetime

#creating a list to store the set of tasks
tasks = []

#function to add a task to the tasks list
def add():
    Task_name = input("Enter the Task: ")
    Due_Date_input = input("Enter the Due Date in YYYY-MM-DD Format: ")
    Due_Time_input = input("Enter the Due Time in 24 hours HH:MM Format: ")
    try:
        #strptime - string format to date and time
        Due_Date = datetime.datetime.strptime(Due_Date_input, "%Y-%m-%d").date()
        Due_Time = datetime.datetime.strptime(Due_Time_input, "%H:%M").time()
        Due_DateTime = datetime.datetime.combine(Due_Date, Due_Time)
    except ValueError:
        print("Invalid Date or Time Format, Please use the correct Format")
        return
    tasks.append({"Name":Task_name, "Due_DateTime": Due_DateTime, "Status": "Pending"})
    print("The Task has been added sucessfully!")

#function to view the list of tasks
def view():
    if not tasks:
        print("There are No Tasks available!")
        return
    print("="*100)
    for i, task in enumerate(tasks):
        print("Task Number:",i+1,",","Task:",task['Name'],",","Due Date and Time:",task['Due_DateTime'],",","Status:",task['Status'])
    print("="*100)

#function to update tasks and their status
def update():
    view()
    try:
        task_number = int(input("Enter the Task Number to Update: ")) - 1
        if task_number < 0 and task_number >= len(tasks):
            print("Invalid Task Number!")
            return
        task = tasks[task_number]
        New_Task_name = input("Enter the New Task Name (leave the field blank to keep the name as it was Before): ")
        if New_Task_name:
            task["Name"] =  New_Task_name
        New_Task_Date_input = input("Enter the New Task Due Date (leave the field blank to keep the Due Date as it was before): ")
        New_Task_Time_input = input("Enter the New Task Due Time (leave the field blank to keep the Due Time as it was before): ")
        if New_Task_Date_input and New_Task_Time_input:
            try:
                New_Task_Date = datetime.datetime.strptime(New_Task_Date_input, "%Y-%m-%d").date()
                New_Task_Time = datetime.datetime.strptime(New_Task_Time_input, "%H:%M").time()
                task['Due_DateTime'] = datetime.datetime.combine(New_Task_Date, New_Task_Time)
            except ValueError:
                print("Invalid date or time format!")
                return
        New_Status = input("Enter the new status (Completed/Pending), Leave Blank to keep the status as before: ")
        if New_Status in ['Pending', 'Completed']:
            task['Status'] = New_Status
        print("Task updated successfully!")
    except ValueError:
        print("Please enter a valid number!")

#Main function loop to run the To-do-list program
def main():
    while True:
        print("\nTo-Do-List Application: ")
        print("Select any one operation: ")
        print("1. Add a Task\n2. Update a Task\n3. View Tasks\n4. Exit")
        choice = (input("Enter your choice: "))
        if choice == '1':
            add()
        elif choice == '2':
            update()
        elif choice == '3':
            view()
        elif choice == '4':
            print("Bye! Exiting the To-do-List")
            break
        else:
            print("Invalid Choice! Please try Again!!")

if __name__ == "__main__":
    main()