# =====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%d-%m-%Y"

# Function 1: reg_user is called when the user selects 'r' to register a user.

def reg_user(menu_choice):

    if menu_choice == "r":  # Setting if statement for menu_choice.

        new_user = input("Please enter a new username: ")

        # Checking if the username already exists in the usernames_list.
        while new_user in usernames_list:
            print("The username you entered is already listed.")
            new_user = input("Please enter a new username: ")

        # If the new username is not already listed, it is added to usernames_list.
        if new_user not in usernames_list:
            usernames_list.append(new_user)
            user_details["Usernames"] = usernames_list

        new_password = input("Please enter a new password: ")
        pass_confirm = input("Please confirm your new password: ")

        # If the new and confirmed password values do not match, an appropriate error message is displayed.
        # The user is then prompted to enter their new password and confirm it until they match.
        while new_password != pass_confirm:
            print("Your confirmed password does not match the original password.")
            new_password = input("Please enter your new password: ")
            pass_confirm = input("Please confirm your new password: ")

            # If the new and confirmed password values match, a successful message is displayed.
        if new_password == pass_confirm:
            print("Your password is valid.")
            passwords_list.append(new_password)
            user_details["Passwords"] = passwords_list

            # user.txt file opened to write to.
            with open('user.txt', 'r+') as user_file:

                # Using for statement to print username and passwords on separate lines.
                # The number of lines is equal to the number of items in usernames_list.
                for i in range(len(usernames_list)):
                    # Writing from the appropriate dictionary keys, in the correct format.
                    user_file.write(user_details["Usernames"][i] + ";" + user_details["Passwords"][i] + '\n')

        # Message returned at the end of function.
        return ("Your new username and password have been successfully added.")


# Function 2: add_task is called when a user selects 'a' to add a new task.
def add_task(menu_choice):
    if menu_choice == "a":

        # Getting user input on the username of the person the task is assigned to.
        task_username = input("Please enter the username of the person you wish to assign the task to: ")

        while True:
            if task_username not in usernames_list:
                print("User does not exist. Please enter a valid username")
                task_username = input("Please enter the username of the person you wish to assign the task to: ")
            else:
                break

        # Getting user input on the title of the task being added.
        task_title = input("Please enter the title of the task: ")

        # Getting information regarding the description of the added task.
        task_description = input("Please enter a description of the task: ")

        # Getting due date of task as DD-MM-YYYY format
        while True:
            try:
                task_due_date = input("Due date of task (DD-MM-YYYY): ")
                date_split = task_due_date.split("-")
                task_due_date = date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
                due_date_time = task_due_date.strftime(DATETIME_STRING_FORMAT)
                break

            # Exceptions handling 
            except ValueError: 
                print("\nInvalid datetime format. Please use the format specified.")
            
            except IndexError:
                print("\nInvalid datetime. Please try again.")

                
        # Using the previously imported datetime module today() function to calculate the current date.
        current_date = date.today()

        # Changing the date object to a string in the correct date format.
        assigned_date = current_date.strftime('%d-%m-%Y')

        # task_completed is automatically set to "No" when adding a new task.
        task_completed = "No"

        # Casting all the user input info into a list, to add to the tasks_dict.
        task_list = [task_username, task_title, task_description, assigned_date, due_date_time, task_completed]
        tasks_dict[f"{count}"] = task_list

        # Opening the tasks.txt file to enter the new task information.
        with open('tasks.txt', 'a') as task_file:

            # Printing the list values for each key in tasks_dict to a new line.
            for key in tasks_dict:
                # Casting to a string enabling the info to be written to the file.
                task_string = str(tasks_dict[key])  
                bad_chars = ["[", "]", "\'" ]

                # Taking out characters pertaining to previous list/dictionary format.
                for i in bad_chars:  
                    task_string = task_string.replace(i,"")

            # Writing the correct format of each string line to the file.
            task_file.writelines(task_string + "\n")  # Writing the correct format of each string line to the file.

        # Message returned at the end of the function.
        return ("Your new task has been added successfully.")


# Function 3: view_all is called when a user selects 'va' to view all tasks listed in tasks.txt.
def view_all(menu_choice):
    if menu_choice == "va":
        
        # Printing all tasks
        for key in tasks_dict:
            print(f"""________________________________________________
Task {key}:\t\t\t {str(tasks_dict[key][1])}
Assigned to:\t\t  {str(tasks_dict[key][0])}
Date assigned:\t\t {str(tasks_dict[key][3])}
Due Date:\t\t {str(tasks_dict[key][4])}
Task Completed?\t\t {str(tasks_dict[key][5])}
Task Description:
 {(tasks_dict[key][2])}
________________________________________________""")

        while True:
            try:
                #Select a task introducing a task number
                task_no = int(input("Please enter task number: "))

                #Printing the task selected
                print(f"""________________________________________________
Task {task_no}:\t\t\t {str(tasks_dict[f"{task_no}"][1])}
Assigned to:\t\t {str(tasks_dict[f"{task_no}"][0])}
Date assigned:\t\t {str(tasks_dict[f"{task_no}"][3])}
Due Date:\t\t {str(tasks_dict[f"{task_no}"][4])}
Task Completed?\t\t {str(tasks_dict[f"{task_no}"][5])}
Task Description:
{(tasks_dict[f"{task_no}"][2])}
________________________________________________""")
                return ("End of Tasks.")

            # Exceptions handling 
            except KeyError:
                print ("\nThe task number introduced does not exist. Please try again.")

            except ValueError:
                print("\nPlease introduce a valid number.")


# Function 4: view_mine is called when a user selects 'vm' to view all tasks assigned to them.
def view_mine(menu_choice, username):

    if menu_choice == "vm":
        for key in tasks_dict:

            # If the task is assigned to the user, it is displayed.
            if username in (tasks_dict[key][0]):  
                print(f"""________________________________________________
Task {key}:\t\t\t {str(tasks_dict[key][1])}
Assigned to:\t\t  {str(tasks_dict[key][0])}
Date assigned:\t\t {str(tasks_dict[key][3])}
Due Date:\t\t {str(tasks_dict[key][4])}
Task Completed?\t\t {str(tasks_dict[key][5])}
Task Description:
{str(tasks_dict[key][2])}
________________________________________________""")

        # The user can now choose to either edit a task by number or return to the main menu.
        task_selection = input("\nPlease select a task by number to edit (e.g. 1, 2,3). \nIf no task displayed, type -1 to return to the main menu. ")
            
        while True:
            try:
                # If they select '-1', they return to main menu.
                if task_selection == "-1":  
                    return (menu)

                elif username in tasks_dict[f"{task_selection}"][0]:
                    # If they enter a task number, they can choose to mark as complete or edit.
                    option = input("Would you like to mark the task as complete or edit the task? (e.g. M OR E) ").lower()

                    if option == "m":
                        # If they choose to mark, and the task is already marked as completed, print the message
                        if " Yes" not in tasks_dict[f"{task_selection}"][5]:
                            tasks_dict[f"{task_selection}"][5] = " Yes"
                            return ("Your task has been successfully marked as completed. \nChoose 'vm' from menu below to select another task to mark.")    
                        
                        # If they choose to mark, the item linked to that task for completion is changed to 'Yes' in tasks_dict.
                        else:  
                            return("This task has already been marked as completed.")

                    # If they choose to edit, the task must be incomplete, i.e. appropriate item in dictionary list equal to 'No'.
                    elif option == "e" and (" No" in tasks_dict[f"{task_selection}"][5]):

                        # They are given the option to edit username or due date.
                        edit_choice = input("Would you like to edit the task username or due date? (Type 'U' or 'D') ").lower()

                        # If they choose to edit the username, they are prompted to enter a new username for the task.
                        if edit_choice == "u": 
                            name_edit = input("Please enter a new username for the task: ")
                            
                            while True:

                                if username == name_edit:
                                    print("The username introduced has already this task. Try another username.")
                                    name_edit = input("Please enter a new username for the task: ")
                                    continue
                                
                                elif name_edit not in usernames_list:
                                    print ("The username does not exist. Please try again. ")
                                    name_edit = input("Please enter a new username for the task: ")
                                    continue

                                else:
                                    # The new name is assigned in the dictionary.
                                    tasks_dict[f"{task_selection}"][0] = name_edit

                                    return("The task username has been updated successfully.")
                        
                        # If they choose to edit the due date, they are prompted to enter a new date.
                        elif edit_choice == "d": 

                            while True:
                                try:
                                    due_date_changed = input("Enter a new due date (DD-MM-YYYY): ")
                                    date_changed_split = due_date_changed.split("-")
                                    due_date_changed = date(int(date_changed_split[2]), int(date_changed_split[1]), int(date_changed_split[0]))
                                    due_date_time_changed = due_date_changed.strftime(DATETIME_STRING_FORMAT)
                                    tasks_dict[f"{task_selection}"][4] = due_date_time_changed
                                    return ("The due date has been updated successfully.") 
                            

                                # Exceptions handling 
                                except ValueError:
                                    print("Invalid datetime format. Please use the format specified")

                                except IndexError:
                                    print("\nInvalid datetime. Please try again.")
                            
                    elif option == "e" and (" Yes" in tasks_dict[f"{task_selection}"][5]):
                        return ("You can only edit tasks that are not already completed. \nChoose 'vm' from the menu below to select another task to edit.")
                    
                # If the task selected belongs to another user
                else: 
                    print ("\nYou can not access this task. Please try again.")
                    task_selection = input("\nPlease enter a task number (e.g. 1, 2,3). If no task displayed, type -1 to return to the main menu. ")
                break

            # If they select a task does not exist
            except KeyError: 
                print ("\nThe task selected does not exist. Please try again.")
                task_selection = input("\nPlease select a a task by number to edit (e.g. 1, 2,3). If no task displayed, type -1 to return to the main menu. ")

# Function 5: over_due_check
# if the current date is greater than the due date, then the task is over due.
def over_due_check(due_date):
    over_due = False  # Setting Boolean variable for the task as over_due.

    # First, the variable is split into a list.
    date_split = due_date.split("-")
    due_date = datetime(int(date_split[2]), int(date_split[1]), int(date_split[0]))
    
    # Getting the current date using the datetime module and formatting it into the same format at the due date initially was.
    date_now = datetime.now()

    # If the current date is less than the set due date, over_due is changed to 'True'.
    if date_now > due_date:  
        over_due = True
        return (over_due)  # over_due value is returned.

    else:  # If the set due date is greater than or equals to the current date, over_due remains 'False'.
        return (over_due)  # over_due value is returned.


# Function 6: Generating text files 'task_overview.txt' and 'user_overview.txt'.
def generate_reports():
    task_overview = ""
    user_overview = ""

    # Total number of tasks is equal to the key count of tasks_dict.
    tasks_total = len(tasks_dict)

    # Adding a string with the total tasks number to the tas_overview string.
    task_overview = task_overview + f"The total number of tasks generated and tracked by task_manager.py is {str(tasks_total)}."
    
    # Setting variables for integers concerning completed tasks, uncompleted tasks and overdue tasks respectively.
    tasks_completed = 0
    tasks_uncompleted = 0
    overdue_tasks = 0
   
    for key in tasks_dict: 
        # Checking for which tasks are completed by finding the 'Yes' string in each key of tasks_dict.
        if tasks_dict[key][5]==" Yes": 
            tasks_completed += 1  # If the task is completed, i.e. 'Yes' string item is present, variable tasks_completed is increased by 1.

        # Checking for which tasks are completed by finding the 'No' string in each key of tasks_dict.
        elif tasks_dict[key][5] == " No":  
            tasks_uncompleted += 1  # If the task is uncompleted, i.e. 'No' string item is present, variable tasks_uncompleted is increased by 1.

            # If the over_due_check function returns 'True', a task is overdue and uncompleted.
            if over_due_check(tasks_dict[key][4]):  
                overdue_tasks += 1  # overdue_tasks is increased by 1 to count the uncompleted, overdue tasks.

    # All of the numbers calculated above are now built into sentences in the task_overview string.
    # Percentages are also calculated within the f-strings added, with the results being rounded to 2 decimal places and cast into strings into sentences.
    task_overview = task_overview + f"\nThe total number of completed tasks is {str(tasks_completed)}." + f"\nThe total number of uncompleted tasks is {str(tasks_uncompleted)}."
    task_overview = task_overview + f"\nThe total number of uncompleted and overdue tasks is {str(overdue_tasks)}."
    task_overview = task_overview + f"\nThe percentage of uncompleted tasks is {str(round((tasks_uncompleted / tasks_total) * 100, 2))}%."
    task_overview = task_overview + f"\nThe percentage of tasks that are overdue {str(round((overdue_tasks / tasks_total) * 100, 2))}%."

    # Generating a 'task_overview' file.
    # The task_overview string is then written to the file in an easy to read format.
    with open('task_overview.txt', 'w+') as file:
        file.write(task_overview)

    # Setting variables to store information regarding total users, tasks completed for a user, tasks uncompleted for the user,
    #tasks uncompleted and over-due for the user respectively.
    total_users = len(usernames_list)
    
    for i in range(len(usernames_list)):
        tasks_total_user = 0
        tasks_completed_user = 0
        tasks_uncompleted_user = 0
        overdue_tasks_user = 0

        for key in tasks_dict:

            if tasks_dict[key][0] == usernames_list[i]:  # Counting the number of tasks assigned to the user by identifying the first list item.
                tasks_total_user += 1  # Integer tasks_total_user is increased by 1 if the task is for the user.

                if tasks_dict[key][5] == " Yes":  # Checking if the task for the user is completed.
                    tasks_completed_user += 1  # Integer tasks_completed_user is increased by 1 if the task is completed.

                elif tasks_dict[key][5] == " No":  # Checking if the task for the user is uncompleted.
                    tasks_uncompleted_user += 1  # Integer tasks_uncompleted_user is increased by 1 if the task is uncompleted.
        
                    if over_due_check(tasks_dict[key][4]):  # Checking if the task is uncompleted and overdue.
                        overdue_tasks_user += 1  # If overdue, integer overdue_tasks_user is increased by 1.

    # Writing all the info calculated above into sentence strings which are built into the user_overview string variable.
    
        user_overview = user_overview + f"Username: {usernames_list[i]}"
        user_overview = user_overview + f"\nThe total number of users registered with task_manager.py is {str(total_users)}."
        user_overview = user_overview + f"\nThe total number of tasks generated and tracked by task_manager.py is {str(tasks_total)}."
        user_overview = user_overview + f"\nThe total number of tasks assigned to {usernames_list[i]} is {str(tasks_total_user)}."
        user_overview = user_overview + f"\nThe percentage of the total number of tasks assigned to {usernames_list[i]} is {str(round((tasks_total_user / tasks_total) * 100, 2))}%."
        user_overview = user_overview + f"\nThe percentage of tasks assigned to {usernames_list[i]} that have been completed is {str(round((tasks_completed_user / tasks_total) * 100, 2))}%."
        user_overview = user_overview + f"\nThe percentage of tasks still to be completed by {usernames_list[i]} is {str(round((tasks_uncompleted_user / tasks_total) * 100, 2))}%."
        user_overview = user_overview + f"\nThe percentage of uncompleted and overdue tasks assigned to {usernames_list[i]} is {str(round((overdue_tasks_user / tasks_total) * 100, 2))}%."
        user_overview = user_overview + f"\n_____________________________________________________\n"

    # Now generating a 'user' file.
    # The user_overview string is then written to the file in an easy to read format.
    with open('user_overview.txt', 'w+') as file:
        file.write(user_overview)

    return ("Your reports have been generated successfully.")


# Writing the main program.

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r+') as user_file:
    user_data = user_file.read().split("\n")

# The user_details dictionary will be built with lists from 'usernames_list' and 'passwords_list' as values.
user_details = {}
usernames_list = []
passwords_list = []

# Adding the info in the user.txt file into the set list.
with open('user.txt', 'r+') as user_data:
    for line in user_data:
        newline = line.rstrip('\n')  # Stripping newline characters from the line.
        split_line = newline.split(";")  # Splitting the line into a list.

        usernames_list.append(split_line[0])  # Assigning items from the list into corresponding list.
        passwords_list.append(split_line[1])

        user_details["Usernames"] = usernames_list  # Lists are now stored as values assigned to keys in user_details dictionary.
        user_details["Passwords"] = passwords_list

    # Writing the program for the task manager.
# Getting input from the user on their login details.
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Creating a while loop to run indefinitely whilst login details are incorrect.
while (username not in usernames_list) or (password not in passwords_list):

    # If username is correct and password is correct, the following message is displayed.
    if (username not in usernames_list) and (password in passwords_list):
        print("Your username is not listed.")
        username = input("Please re-enter your username: ")
        password = input("Please re-enter your password: ")

    # If password is incorrect and username is correct, the following message is displayed.
    elif (password not in passwords_list) and (username in usernames_list):
        print("Your password is incorrect.")
        username = input("Please re-enter your username: ")
        password = input("Please re-enter your password: ")

    # If both the username and password are incorrect, the following message is displayed.
    elif (username not in usernames_list) and (password not in passwords_list):
        print("Your username and password are incorrect.")
        username = input("Please re-enter your username: ")
        password = input("Please re-enter your password: ")

# If both username and password are correct, the successful login message is displayed.
if (username in usernames_list) and (password in passwords_list):
    print("You are successfully logged in.")

# Creating the tasks_dict dictionary
tasks_dict = {}

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open('tasks.txt', 'r+') as task_file:
    data = task_file.readlines()

    # Enumerating the tasks
    for count, task_line in enumerate(data, 1):
        new_task_line = task_line.rstrip("\n")
        split_task_line = new_task_line.split(",")
        tasks_dict[f"{count}"] = split_task_line 

# If task_overview.txt is not exists, it will be created.
if not os.path.exists("task_overview.txt"):
    with open("task_overview.txt", "w") as file:
        pass

# If user_overview.txt is not exists, it will be created.
if not os.path.exists("user_overview.txt"):
    with open("user_overview.txt", "w") as file:
        pass

# Displaying the menu once the user is logged in.
while True:
    if username == "admin":  # The admin user views a specific menu with extra options (gr and ds).
        menu = input("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
""").lower()

    else:  # All other users can only view the basic menu.

        menu = input("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
""").lower()
        
    # Choosing 'r' from the menu causes the reg_user function to be called.
    if menu == "r":
        print(reg_user(menu))

    # Choosing 'a' from the menu causes the add_task function to be called.
    elif menu == "a":
        print(add_task(menu))

    # Choosing 'va' from the menu causes the view_all function to be called.
    elif menu == "va":
        print(view_all(menu))

    # Choosing 'vm' from the menu causes the view_mine function to be called.
    elif menu == "vm":
        print(view_mine(menu, username))

        with open ("tasks.txt", "w+") as file:
            for key in tasks_dict:
                # Casting to a string enabling the info to be written to the file.
                tasks_string = str(tasks_dict[key])
                bad_chars = ["[", "]", "\'" ]

                for i in bad_chars: 
                    # Taking out characters pertaining to previous list/dictionary format.
                    tasks_string = tasks_string.replace(i,"")
                tasks_string = tasks_string.replace("  "," ")
                
                # Writing in the tasks.txt file
                file.writelines(tasks_string +"\n")   

    # Choosing 'gr' from the menu causes text files user_overview and task_overview to be generated.
    elif menu == "gr":
        print(generate_reports())

    # Calling function generate files in case they do no exist yet.
    elif menu == 'ds':
        print(generate_reports())
        print("""\n____________________________________________________
The task overview report is as follows:
____________________________________________________\n""")

        # Opening the task_overview file to get info from it.
        with open('task_overview.txt', 'r+') as file:
            for line in file:
                # Printing/displaying each line in the file.
                print(line)  
        print("""\n_____________________________________________________
The user overview report is as follows:
_____________________________________________________\n""")

        # Opening user_overview file.
        with open('user_overview.txt', 'r+') as file:
            for line in file:
                # Displaying each line of the file.
                print(line)  

        print("""\n______________________________________________________
End of Statistics Reports
______________________________________________________\n""")

    # If the user selects 'e' they can log out of the program.
    elif menu == "e":
        print("You are successfully logged out.")
        break