import pandas as pd
user_name = input('name: ')

account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
account_data.columns = ['username', 'email', 'password']
while True:
    new_account_data = account_data[['username']]
    row = new_account_data.to_csv(header=None, index=False).strip('\n').split('\n')
    if user_name in row:
        user_name_exists = (account_data.loc[account_data['username'] == user_name])
        print(f"{user_input} is already taken, please choose !")
        break


        elif user_input == "create account":
            user_name = input("Enter user name :>> ")
            while True:
                new_account_data = account_data[['username']]
                row = new_account_data.to_csv(header=None, index=False).strip('\n').split('\n')
                if user_name in row:
                    user_name_exists = (account_data.loc[account_data['username'] == user_name])
                    print(f"{user_input} is already taken, please choose !")
                    break
