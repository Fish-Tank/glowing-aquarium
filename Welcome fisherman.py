import pandas as pd
account_data = pd.read_csv("accounts.txt", delimiter=" ")
fish_data = pd.read_csv("fish.txt", delimiter=" ")

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

current_user = {
    "name": None,
    "password": None,
}

print('Welcome to the Fishing-Tournament App... ')


def save_user_data(username, email, password):
    accounts_file = open("accounts.txt", "a")
    accounts_file.write(f"{username} {email} {password} \n")
    accounts_file.close()
    print("Account created sucessfully!")

def save_fish_data(type, length, lake, user_name):
    fish_file = open("fish.txt", "a")
    fish_file.write(f"{type} {length} {lake} {user_name} \n")
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
    '''
    function checking if your string is a pure digit, int
    return : bool
    '''
    if check_input.isdigit():
        return True
    return False



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


        elif user_input == 'achievements':
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
            fish_data = fish_data[['type', 'length', 'lake', 'username']]
            print(fish_data.sort_values('length', ascending=False).reset_index(drop=True))