#Welcome to the fisherman program. In this program a user can upload this catches and can compare it with others

#Import Data. One is for the account and the second is for the fish

import pandas as pd
account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)

account_data.columns = ['username', 'email', 'password']
fish_data.columns = ['type', 'length', 'lake', 'username']

#Commands for the program.
commands = [
    "exit > exit the program",
    "help > show all the commands",
    "create account > to create a new user",
    "login > to login to your account",
    "logout > to logout your account",
    "fish > enter a fish",
    "profile > show all my profile details ",
    "achievements > show me my cought fish",
    "rating list > enter a fish",
]

#Current user
current_user = {
    "name": None,
    "password": None,
}

#Introduction mesage for the user
print('Welcome to the Fishing-Tournament App... ')

#Open a text file for appending text
# Create user with username, email and password. If sucessfully created, progam continues.
def save_user_data(username, email, password):
    accounts_file = open("accounts.txt", "a")
    accounts_file.write(f"{username} {email} {password}\n")
    accounts_file.close()
    print("Account created sucessfully!")

#Open a text file for appending text
#Enter data for your catch (type, length, user_name).
def save_fish_data(type, length, lake, user_name):
    fish_file = open("fish.txt", "a")
    fish_file.write(f"{type} {length} {lake} {user_name}\n")
    fish_file.close()
    print("Catch submitted sucessfully!")

#Open for text file for reading text
def user_exist(username, password):
    accounts_file = open("accounts.txt", "r")
    accounts_file_data = accounts_file.readlines()
    exist = False
    for i in range(len(accounts_file_data)):
        splited_data = accounts_file_data[i].split()
        if username == splited_data[0] and password == splited_data[2]:
            exist = True
            break
    accounts_file.close()
    return exist

#Built in function
# Program to make a simple
# login screen
import tkinter as tk
root = tk.Tk()
# setting the windows size
root.geometry("600x400")
# declaring string variable
# for storing name and password
name_var = tk.StringVar()
passw_var = tk.StringVar()
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    name = name_var.get()
    password = passw_var.get()
    print("The name is : " + name)
    print("The password is : " + password)
    name_var.set("")
    passw_var.set("")
# creating a label for
# name using widget Label
    name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
# creating a entry for input
# name using widget Entry
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
# creating a label for password
    passw_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))
# creating a entry for password
    passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
# creating a button using the widget
# Button that will call the submit function
    sub_btn = tk.Button(root, text='Submit', command=submit)
# placing the label and entry in
# the required position using grid
# method
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    passw_label.grid(row=1, column=0)
    passw_entry.grid(row=1, column=1)
    sub_btn.grid(row=2, column=1)
# performing an infinite loop
# for the window to display
    root.mainloop()

#To log in the program
def log_in():
    name = name_var.get()
    password = passw_var.get()
    print("The name is : " + name)
    print("The password is : " + password)
    name_var.set("")
    passw_var.set("")
    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
    # creating a label for password
    passw_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))
    # creating a entry for password
    passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn = tk.Button(root, text='Submit', command=submit)
    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    passw_label.grid(row=1, column=0)
    passw_entry.grid(row=1, column=1)
    sub_btn.grid(row=2, column=1)
    # performing an infinite loop
    # for the window to display
    root.mainloop()
    # read data
    if user_exist(user_name, password):
        current_user["name"] = name
        current_user["password"] = password
        print("You logged in sucessfully. Welcome %s" % name)
    else:
        print("Account does not exist or you entered user name or password wrong!")

#To log out from your account
def log_out():
    current_user["name"] = None
    print("You logged out.")

#Function checking if your string is a pure digit.
def is_digit(check_input):
    '''
    function checking if your string is a pure digit, int
    return : bool
    '''
    if check_input.isdigit():
        return True
    return False

#list of all possible fishes to catch
fishtype_list = ['perch' , 'pike' , 'catfish']

#Menu for creating and save user data
while True:
        if current_user["name"] == None:
            user_input = input("Enter a command or type help :>> ").lower()
        else:
            user_input = input("(Welcome: %s) Enter a command or type help :>> " % current_user["name"]).lower()

        if user_input == "exit":
            break
        elif user_input == 'help':
            for i in range(len(commands)):
                print(commands[i])
        elif user_input == "create account":
            user_name = input("Enter user name :>> ")
            if len(user_name) < 4:
                print("this user name is too short. Enter a valid user name")
                user_name = input("Enter user name :>> ")
            email = input("Enter a valid email :>> ")
            if "@" not in email:
                print("The email you entered is not valid. Please enter email again")
                email = input("Enter a valid email :>> ")
            password1 = input("Enter password :>> ")
            password2 = input("Confirm password :>> ")
            if password2 != password1 or len(password1) < 4:
                print(
                    "password does not match or it's too small. Please enter password again")
                password1 = input("Enter password :>> ")
                password2 = input("Confirm password :>> ")
            # save data
            save_user_data(user_name, email, password1)

#login for tournament
        elif user_input == "login":

            log_in()

            command = [

                "exit > exit the program and submit the fish",

                "help > show all the commands",

                "fish > enter a fish",

            ]

            current_user = {

                "name": None,

                "password": None,

            }
        elif user_input == "fish":

            while True:
                # menu:
                print(f'Fish species in this tournament: ')
                for index, item in enumerate(fishtype_list):
                    print(f'{index} : {item}')
                print(f'type \'exit\' to exit the program\n')
                break
            # set user input to nothing to force entry into the while loop
            type = ''
            while type != 'q':
                type = input('select the species you caught form the list above: ')

                # make sure the user types an actual integer if the input is not q (to quit)
                while type != 'q' and not is_digit(type):
                    print(f'please try again, integer is required as input')
                    type = input('select the species you caught form the list above:')

                # if the user does not want to quit, we will print the choice
                if type != 'q':
                    try:
                        print(f'You chose {fishtype_list[int(type)]}')
                        break
                    except IndexError:
                        print("Invalid entry!")

            while True:
                length = input("Please enter fish length in cm:>> ")
                try:
                    length = float(length)
                    if length < 250:
                        break
                except ValueError:
                    print("This is not a number! Is it so hard to enter a number? ")

            lake = input("Enter lake :>> ")
            user_name = input("Enter the username who caught the fish: ")
            # save data
            save_fish_data(type, length, lake, user_name)

#data output
        elif user_input == 'achievements':
            account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
            fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)

            account_data.columns = ['username', 'email', 'password']
            fish_data.columns = ['type', 'length', 'lake', 'username']
            while True:
                user_name = input("Enter your name to search: ")
                new_account_data = account_data[['username']]
                row = new_account_data.to_csv(header=None, index=False).strip('\n').split('\n')
                if user_name in row:
                    personal_catches = (fish_data.loc[fish_data['username'] == user_name])
                    print(personal_catches)
                    break
                else:
                    print("This this username doesn't exist!")

        elif user_input == 'profile':
            account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
            fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)

            account_data.columns = ['username', 'email', 'password']
            fish_data.columns = ['type', 'length', 'lake', 'username']

            while True:
                user_name = input("Enter your name to search: ")
                new_account_data = account_data[['username']]
                row = new_account_data.to_csv(header=None, index=False).strip('\n').split('\n')
                if user_name in row:
                    personal_catches = (account_data.loc[account_data['username'] == user_name])
                    print(personal_catches)
                    break
                else:
                    print("This this username doesn't exist!")


        elif user_input == 'rating list':
            while True:
                fish_data = pd.read_csv("fish.txt", delimiter=" ")
                print(fish_data.sort_values('length', ascending=False).reset_index(drop=True))
                break

        else:
            print("I don't understand.\
            Please enter a valid command or type 'help'.")