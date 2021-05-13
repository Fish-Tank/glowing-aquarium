import pandas as pd
account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)

account_data.columns = ['username', 'email', 'password']
fish_data.columns = ['type', 'length', 'lake', 'username']

commands = [
    "exit > exit the program",
    "help > show all the commands",
    "create account > create a new user to stay informed about the tournament",
    "login > to login to your account",
    "logout > to logout your account",
    "fish > enter a fish",
    "profile > show all my profile details ",
    "achievements > show me my caught fish",
    "rating list > enter a fish \n",
]

current_user = {
    "name": None,
    "password": None,
}

print('Welcome to the Fishing-Tournament Program \nSelect a command below and start today\'s fishing tournament :)\nGood luck!\n')
for i in range(len(commands)):
    print(commands[i])

def save_user_data(username, email, password):
    accounts_file = open("accounts.txt", "a")
    accounts_file.write(f"{username} {email} {password}\n")
    accounts_file.close()
    print("Account created sucessfully!")

def save_fish_data(type, length, lake, user_name):
    fish_file = open("fish.txt", "a")
    fish_file.write(f"{type} {length} {lake} {user_name}\n")
    fish_file.close()
    print("Catch submitted sucessfully!")

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


def log_in():
    user_name = input("Enter your user name:>> ")
    password = input("Enter your user password:>> ")
    # read data
    if user_exist(user_name, password):
        current_user["name"] = user_name
        current_user["password"] = password
        print("You logged in sucessfully. Welcome %s" % user_name)
    else:
        print("Account does not exist or you entered user name or password wrong!")


def log_out():
    current_user["name"] = None
    print("You logged out.")

def is_digit(check_input):
    if check_input.isdigit():
        return True
    return False

def check_leaderboards():
    print('1) Perch')
    print('2) Pike')
    print('3) Catfish')
    while True:
        type = int(input('For which species would you like to see the leaderboard? '))

        if type == 1:
            print('Perch!')
            print(fish_data.loc[fish_data['type'] == 0].sort_values('length', ascending=False).reset_index(drop=True))
            break
        elif type == 2:
            print('Pike')
            print(fish_data.loc[fish_data['type'] == 1].sort_values('length', ascending=False).reset_index(drop=True))
            break
        elif type == 3:
            print('Catfish')
            print(fish_data.loc[fish_data['type'] == 2].sort_values('length', ascending=False).reset_index(drop=True))
            break
        else:
            print('That\'s not an option!')






fishtype_list = ['perch' , 'pike' , 'catfish']

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
            while True:
                user_name = input("Enter user name :>> ")
                new_account_data = account_data[['username']]
                row = new_account_data.to_csv(header=None, index=False).strip('\n').split('\n')
                if user_name not in row:
                    break
                else:
                    print(f"{user_name} is already taken, please choose !")
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


        elif user_input == "login":

            log_in()

            current_user = { "name": None, "password": None }

        elif user_input == "fish":

            while True:
                # menu:
                print(f'Fish species in this tournament: ')
                for index, item in enumerate(fishtype_list):
                    print(f'{index+1} : {item}')
                print(f'type \'exit\' to exit the program\n')
                break
            # set user input to nothing to force entry into the while loop
            type = ''

            while type != 'exit':
                type = input('select the species you caught from the list above: ')



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
                    elif length > 250:
                        print("That would be bigger than any fish that swims in the Swiss lakes ;) Try again!")
                except ValueError:
                    print("This is not a number! Is it so hard to enter a number? ")

            lake = input("Enter lake :>> ")
            user_name = input("Enter the username who caught the fish: ")
            # save data
            save_fish_data(type, length, lake, user_name)


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

            check_leaderboards()


        else:
            print("I don't understand.\
            Please enter a valid command or type 'help'.")