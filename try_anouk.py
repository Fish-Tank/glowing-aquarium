import pandas as pd
account_data = pd.read_csv("accounts.txt", delimiter=" ")
fish_data = pd.read_csv("fish.txt", delimiter=" ")

commands = [
    "profile > show all my profile details ",
    "achievements > show me my cought fish",
    "rating list > enter a fish",
]

current_user = {
    "name": None,
    "password": None,
}

while True:
        if current_user["name"] == None:
            user_input = input("What do you wanna do :>> ").lower()
        else:
            user_input = input("(Welcome: %s) Enter a command or type help :>> " % current_user["name"]).lower()

        if user_input == "exit":
            break

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