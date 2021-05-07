with open ("accounts.txt", "r") as accounts:
    a_lines = accounts.readlines()
    print(a_lines)

user_names = []
email = []
a_password = []
for l in a_lines:
    as_list = l.split(" ")
    user_names.append(as_list[0])
    email.append(as_list[1])
    a_password.append(as_list[2])

print(user_names)
print(email)
print(a_password)


with open("fish.txt", "r") as fish:
    f_lines = fish.readlines()
    print(f_lines)


fish_type = []
length = []
lake = []
f_password = []
for l in f_lines:
    as_list = l.split(" ")
    fish_type.append(as_list[0])
    length.append(as_list[1])
    lake.append(as_list[2])
    f_password.append(as_list[3])

print(fish_type)
print(length)
print(lake)
print(f_password)

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





