commands = [
            "exit > exit the program",
            "help > show all the commands",
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
        user_input = input(
            "(Welcome: %s) Enter a command or type help :>> " % current_user["name"]).lower()

    if user_input == "exit":
        break
    elif user_input == 'help':
        for i in range(len(commands)):
            print(commands[i])
    elif user_input == 'profile':
        found_password = a_password[2]
        if found_password in f_password:
            print(a_lines[2])
        else:
            print("Error")
    #elif user_input == 'achievements':

#while True:
    #f_lines
#accounts.close()
#fish.close()





