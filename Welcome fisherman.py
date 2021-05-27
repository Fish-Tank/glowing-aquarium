#import of pandas
import pandas as pd

#creation of txt files
account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)

#naming columns of txt files
account_data.columns = ['username', 'email', 'password']
fish_data.columns = ['type', 'length', 'lake', 'username']

#commands for the user in the program
commands = [
    "exit > exit the program",
    "help > show all the commands",
    "create account > create a new user to stay informed about the tournament",
    "login > to login to your account",
    "logout > to logout your account",
    "fish > enter a fish",
    "profile > show all my profile details ",
    "achievements > show me my caught fish",
    "leaderboard > check current tournament standings",
    "results > show me the biggest 5 catches",
    "lakes > show me catches from lakes",
    "average > Show me the average of the length of the caught fish from the lakes",
    "count > Show me the amount of fish caught from lakes\n"
]

#commands to display catches from the lakes with all information
show_catches_from_lakes = [
    "Type on of the lakes\n",
    "bodensee > show me catches from Bodensee",
    "murtensee > show me catches from Murtensee",
    "bielersee > show me catches from Bielersee",
    "neuburgersee > show me catches from Neuburgersee",
    "vierwaldstättersee > show me catches from Vierwaldstättersee\n",
]

#commands to display the catches from the lakes with average length
average_of_lake = [
    "Type one of the lakes to see the average size of a cought fish\n",
    "median of all > show me average from all lakes",
    "median of bodensee > show me average from Bodensee",
    "median of murtensee > show me average from Murtensee",
    "median of bielersee > show me average from Bielersee",
    "median of neuburgersee > show me average from Neuburgersee",
    "median of vierwaldstättersee > show me average from Vierwaldstättersee\n",
]

#commands to display the amount of fish caught
count_fish = [
    "Type one of the lakes to see the amount of caught fish\n",
    "count all > show me all fish caught",
    "count bodensee > show me all fish caught in Bodensee",
    "count murtensee > show me all fish caught in Murtensee",
    "count bielersee > show me all fish caught in Bielersee",
    "count neuburgersee > show me all fish caught in Neuburgersee",
    "count vierwaldstättersee > show me all fish caught in vierwaldstättersee\n",
]

current_user = {
    "name": None,
    "password": None,
}

#start into the program with an introduction message
print('Welcome to the Fishing-Tournament Program \nSelect a command below and start today\'s fishing tournament :)\nGood luck!\n')
for i in range(len(commands)):
    print(commands[i])

#defintion for txt file for the creation of an account
def save_user_data(username, email, password):
    accounts_file = open("accounts.txt", "a")
    accounts_file.write(f"{username} {email} {password}\n")
    accounts_file.close()
    print("Account created sucessfully!")

#defintion for txt file for entering a catch
def save_fish_data(type, length, lake, user_name):
    fish_file = open("fish.txt", "a")
    fish_file.write(f"{type} {length} {lake} {user_name}\n")
    fish_file.close()
    print("Catch submitted sucessfully!")

#definition to check in the file if user and password exist
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

#definition for login
def log_in():
    user_name = input("Enter your user name:>> ")
    password = input("Enter your user password:>> ")
    #read data
    if user_exist(user_name, password):
        current_user["name"] = user_name
        current_user["password"] = password
        print("You logged in sucessfully. Welcome %s" % user_name)
    else:
        print("Account does not exist or you entered user name or password wrong!")

#defintion for logout
def log_out():
    current_user["name"] = None
    print("You logged out.")

#defintion if input is a digit
def is_digit(check_input):
    if check_input.isdigit():
        return True
    return False

#defintion for checking the leaderboard
def check_leaderboards():
    print('0) Perch')
    print('1) Pike')
    print('2) Catfish')
    while True:
        type = int(input('For which species would you like to see the leaderboard? '))

        if type == 0:
            print('Perch!')
            print(fish_data.loc[fish_data['type'] == 0].sort_values('length', ascending=False).reset_index(drop=True))
            break
        elif type == 1:
            print('Pike')
            print(fish_data.loc[fish_data['type'] == 1].sort_values('length', ascending=False).reset_index(drop=True))
            break
        elif type == 2:
            print('Catfish')
            print(fish_data.loc[fish_data['type'] == 2].sort_values('length', ascending=False).reset_index(drop=True))
            break
        else:
            print('That\'s not an option!')

#definition for showing results
def show_me_results():
    results = input("Enter show me the results:>> ")
    print("Here the results")

#list of possible fishes
fishtype_list = ['perch' , 'pike' , 'catfish']

#interface to the user with all functions for him/her
while True:
        #input to enter a command or display the menu when the user is not logged in
        if current_user["name"] == None:
            user_input = input("Enter a command or type help :>> ").lower()
        else:
            #input to enter a command or display the menu when the user is not logged in
            user_input = input("(Welcome: %s) Enter a command or type help :>> " % current_user["name"]).lower()
        #if user enters exit, program will close
        if user_input == "exit":
            break
        #if user enters help, the menu will be displayed
        elif user_input == 'help':
            for i in range(len(commands)):
                print(commands[i])
        #if user want to create an account
        elif user_input == "create account":
            #input for entering user name
            while True:
                user_name = input("Enter user name :>> ")
                new_account_data = account_data[['username']]
                row = new_account_data.to_csv(header=None, index=False).strip('\n').split('\n')
                #if successful this step will be closed
                if user_name not in row:
                    break
                #if users already exists, user has to enter a new name
                else:
                    print(f"{user_name} is already taken, please choose another one!")
            #username has to be longer than for digits
            if len(user_name) < 4:
                print("this user name is too short. Enter a valid user name")
                user_name = input("Enter user name :>> ")
            #user has to enter his mail address
            email = input("Enter a valid email :>> ")
            #to check if email address has an @
            if "@" not in email:
                print("The email you entered is not valid. Please enter email again")
                email = input("Enter a valid email :>> ")
            #user has to set password and confirm it
            password1 = input("Enter password :>> ")
            password2 = input("Confirm password :>> ")
            #to check if the password is longer than four digits, and if so, if it is correct
            if password2 != password1 or len(password1) < 4:
                print(
                    "password does not match or it's too small. Please enter password again")
                password1 = input("Enter password :>> ")
                password2 = input("Confirm password :>> ")
            #save data of the user (username, email and password)
            save_user_data(user_name, email, password1)

        #if user wants to log in
        elif user_input == "login":

            log_in()

            current_user = { "name": None, "password": None }
        #if user want to enter a fish into the program
        elif user_input == "fish":

            while True:
                #display menu with the possible fish species:
                print(f'Fish species in this tournament: ')
                for index, item in enumerate(fishtype_list):
                    print(f'{index} : {item}')
                print(f'type \'exit\' to exit the program\n')
                break
            #set user input to nothing to force entry into while loop
            type = ''

            while type != 'exit':
                type = input('select the species you caught from the list above: ')

                #make sure the user types an actual integer if the input is not q (to quit)
                while type != 'exit' and not is_digit(type):
                    print(f'please try again, integer is required as input')
                    type = input('select the species you caught form the list above:')

                #if the user does not want to exit, it will print the choice
                if type != 'exit':
                    try:
                        print(f'You chose {fishtype_list[int(type)]}')
                        break
                    except IndexError:
                        print("Invalid entry!")
            #entering the length of the fish
            while True:
                length = input("Please enter fish length in cm:>> ")
                #if the fish is longer than 250 cm, the user cannot enter the fish and additionally check if the length is a digit
                try:
                    length = float(length)
                    if length < 250:
                        break
                    elif length > 250:
                        print("That would be bigger than any fish that swims in the Swiss lakes ;) Try again!")
                except ValueError:
                    print("This is not a number! Is it so hard to enter a number? ")
            #user must enter the lake where he caught the fish
            lake = input("Enter lake :>> ")
            user_name = input("Enter the username who caught the fish: ")
            #save data
            save_fish_data(type, length, lake, user_name)
        #user can check all his caught fish
        elif user_input == 'achievements':
            account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
            fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)

            account_data.columns = ['username', 'email', 'password']
            fish_data.columns = ['type', 'length', 'lake', 'username']
            #user has to enter his name and program checks if user exists. If successful, the catches will be displayed
            while True:
                user_name = input("Enter your name to search: \nor type exit to return to the start :>> ")
                new_account_data = account_data[['username']]
                row = new_account_data.to_csv(header=None, index=False).strip('\n').split('\n')
                if user_name in row:
                    personal_catches = (fish_data.loc[fish_data['username'] == user_name])
                    print(personal_catches)
                    break
                elif user_name == "exit":
                    break
                #if user doesn't exist
                else:
                    print("This this username doesn't exist!")
        #user can enter his name and sees his profile
        elif user_input == 'profile':
            account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
            fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)

            account_data.columns = ['username', 'email', 'password']
            fish_data.columns = ['type', 'length', 'lake', 'username']
            #user has to enter his name and if successful, the information will be displayed
            while True:
                user_name = input("Enter your name to search: ")
                new_account_data = account_data[['username']]
                row = new_account_data.to_csv(header=None, index=False).strip('\n').split('\n')
                if user_name in row:
                    personal_catches = (account_data.loc[account_data['username'] == user_name])
                    print(personal_catches)
                    break
                #if user doesn't exist
                else:
                    print("This this username doesn't exist!")
        #user can check the leaderboard
        elif user_input == 'leaderboard':

            check_leaderboards()
        #user can check the five highest catches
        elif user_input == "results":
            results_of_all = fish_data.loc[fish_data['lake'].str.contains('see')]
            dtry = pd.to_numeric(results_of_all['length'])
            biggest = dtry.sort_values(ascending=False)
            Show_results_all = biggest.head(6)
            print(type(Show_results_all))
            print(Show_results_all)
        #if the user enters "lakes", a new menu will be displayed
        elif user_input == 'lakes':
            for i in range(len(show_catches_from_lakes)):
                print(show_catches_from_lakes[i])
        #if the user enters "bodensee",he can see the five highest catches there
        elif user_input == "bodensee":
            catches_bodensee = fish_data.loc[fish_data['lake'].str.contains('Boden')]
            show_bodensee = catches_bodensee.head(5)
            print(show_bodensee)
        #if the user enters "murtensee",he can see the five highest catches there
        elif user_input == "murtensee":
            catches_murtensee = fish_data.loc[fish_data['lake'].str.contains('Murten')]
            show_murtensee = catches_murtensee.head(5)
            print(show_murtensee)
        #if the user enters "bielersee",he can see the five highest catches there
        elif user_input == "bielersee":
            catches_Bielersee = fish_data.loc[fish_data['lake'].str.contains('Bie')]
            show_Bielersee = catches_Bielersee.head(5)
            print(show_Bielersee)
        #if the user enters "neuburgersee", he can see the five highest catches there
        elif user_input == "neuburgersee":
            catches_Neuburgersee = fish_data.loc[fish_data['lake'].str.contains('Neuburgersee')]
            show_Neuburgersee = catches_Neuburgersee.head(5)
            print(show_Neuburgersee)
        #if the user enters "vierwaldstättersee",he can see the five highest catches there
        elif user_input == "vierwaldstättersee":
            catches_Vierwaldstättersee = fish_data.loc[fish_data['lake'].str.contains('Boden')]
            show_Vierwaldstättersee = catches_Vierwaldstättersee.head(5)
            print(show_Vierwaldstättersee)
        #if the user enters "average", a new menu will be displayed
        elif user_input == 'average':
            for i in range(len(average_of_lake)):
                print(average_of_lake[i])
        #if the user enters "median of all",he can see the average of the length from all catches
        elif user_input == "median of all":
            median_of_all = fish_data.loc[fish_data['lake'].str.contains('see')]
            dtry = pd.to_numeric(median_of_all['length'])
            average = dtry.mean()
            print(type(average))
            print(average)
            Show_median_all = median_of_all.head(2)
        #if the user enters "median of bodensee", from there he can see the average length from all catches
        elif user_input == "median of bodensee":
            median_of_bodensee = fish_data.loc[fish_data['lake'].str.contains('Bodensee')]
            dtry = pd.to_numeric(median_of_bodensee['length'])
            average = dtry.mean()
            print(type(average))
            print(average)
            Show_median_bodensee = median_of_bodensee.head(2)
        #if the user enters "median of murtensee", from there he can see the average length from all catches
        elif user_input == "median of murtensee":
            median_of_murtensee = fish_data.loc[fish_data['lake'].str.contains('Murten')]
            dtry = pd.to_numeric(median_of_murtensee['length'])
            average = dtry.mean()
            print(type(average))
            print(average)
            Show_median_murtensee = median_of_murtensee.head(2)
        #if the user enters "median of Lake bielersee", from there he can see the average length from all catches
        elif user_input == "median of bielersee":
            median_of_bielersee = fish_data.loc[fish_data['lake'].str.contains('Bieler')]
            dtry = pd.to_numeric(median_of_bielersee['length'])
            average = dtry.mean()
            print(type(average))
            print(average)
            Show_median_bielersee = median_of_bielersee.head(2)
        #if the user enters "median of neuenburgersee", from there he can see the average length from all catches
        elif user_input == "median of neuenburgersee":
            median_of_neuenburgersee = fish_data.loc[fish_data['lake'].str.contains('Neuenburgersee')]
            dtry = pd.to_numeric(median_of_neuenburgersee['length'])
            average = dtry.mean()
            print(type(average))
            print(average)
            Show_median_neuenburgersee = median_of_neuenburgersee.head(2)
        #if the user enters "median of vierwaldstättersee", from there he can see the average length from all catches
        elif user_input == "median of vierwaldstättersee":
            median_of_vierwaldstättersee = fish_data.loc[fish_data['lake'].str.contains('Vierwaldstättersee')]
            dtry = pd.to_numeric(median_of_vierwaldstättersee['length'])
            average = dtry.mean()
            print(type(average))
            print(average)
            Show_median_vierwaldstättersee = median_of_vierwaldstättersee.head(2)
        #if user enters "count", a new menu will be displayed
        elif user_input == 'count':
            for i in range(len(count_fish)):
                print(count_fish[i])
        #if the user enters "count all", the number of all fish caught will be displayed
        elif user_input == 'count all':
            count = fish_data[['type']].value_counts()
            print(count)
        #if the user enters "count bodensee", the number of all fish caught from there will be displayed
        elif user_input == 'count bodensee':
            count_of_bodensee = fish_data.loc[fish_data['lake'].str.contains('Bodensee')]
            dtry = pd.to_numeric(count_of_bodensee['type'])
            count = dtry.value_counts()
            print(type(count))
            print(count)
            Show_count_of_bodensee = count_of_bodensee.head(2)
        #if the user enters "count murtensee", the number of all fish caught from there will be displayed
        elif user_input == 'count murtensee':
            count_of_murtensee = fish_data.loc[fish_data['lake'].str.contains('Murtensee')]
            dtry = pd.to_numeric(count_of_murtensee['type'])
            count = dtry.value_counts()
            print(type(count))
            print(count)
            Show_count_of_murtensee = count_of_murtensee.head(2)
        #if the user enters "count bielersee", the number of all fish caught from there will be displayed
        elif user_input == 'count bielersee':
            count_of_bielersee = fish_data.loc[fish_data['lake'].str.contains('Bielersee')]
            dtry = pd.to_numeric(count_of_bielersee['type'])
            count = dtry.value_counts()
            print(type(count))
            print(count)
            Show_count_of_bielersee = count_of_bielersee.head(2)
        #if the user enters "count neuenburgersee", the number of all fish caught from there will be displayed
        elif user_input == 'count neuenburgersee':
            count_of_neuenburgersee = fish_data.loc[fish_data['lake'].str.contains('Neuenburgersee')]
            dtry = pd.to_numeric(count_of_neuenburgersee['type'])
            count = dtry.value_counts()
            print(type(count))
            print(count)
            Show_count_of_neuenburgersee = count_of_neuenburgersee.head(2)
        #if the user enters "count vierwaldstättersee", the number of all fish caught from there will be displayed
        elif user_input == 'count vierwaldstättersee':
            count_of_vierwaldstättersee = fish_data.loc[fish_data['lake'].str.contains('Vierwaldstättersee')]
            dtry = pd.to_numeric(count_of_vierwaldstättersee['type'])
            count = dtry.value_counts()
            print(type(count))
            print(count)
            Show_count_of_vierwaldstättersee = count_of_vierwaldstättersee.head(2)
        #if input "help" is not valid, an error message will be shown
        else:
            print("I don't understand.\
            Please enter a valid command or type 'help'.")
