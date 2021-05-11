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

while True:
        if current_user["name"] == None:
            user_input = input("Enter a command or type help :>> ").lower()
        else:
            user_input = input("(Welcome: %s) Enter a command or type help :>> " % current_user["name"]).lower()

        if user_input == "exit":
            break
        elif user_input == 'profile':
            user_name = input("Enter your name to search: ")
            personal_catches = (account_data.loc[account_data['username'] == user_name])
            print(personal_catches)