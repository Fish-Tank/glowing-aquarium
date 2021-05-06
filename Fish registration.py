command = [
    "exit > exit the program and submit the fish",
    "help > show all the commands",
    "fish > enter a fish",
]

current_user = {
    "name": None,
    "password": None,
}


def save_fish_data(type, length, lake):
    fish_file = open("fish.txt", "a")
    fish_file.write(f"{type} {length} {lake} \n")
    fish_file.close()
    print("Catch submitted sucessfully!")



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
    elif user_input == "fish":
        type = input("Enter fish type :>> ")
        length = input("Enter fish lenght :>> ")
        lake = input("Enter lake :>> ")
        # save data
        save_fish_data(type, length, lake)

    else:
        print("I don't understand.\
        Please enter a valid command or type 'help'.")