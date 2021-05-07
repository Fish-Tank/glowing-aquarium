commands = [
            "exit > exit the program and submit the fish",
            "help > show all the commands",
            "fish > enter a fish"]

current_user = {
            "name": None,
            "password": None,}

def is_digit(check_input):
    '''
    function checking if your string is a pure digit, int
    return : bool
    '''
    if check_input.isdigit():
        return True
    return False

def save_fish_data(type, length, lake):
    fish_file = open("fish.txt", "a")
    fish_file.write(f"{type} {length} {lake} \n")
    fish_file.close()
    print("Catch submitted sucessfully!")

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
            # save data
            save_fish_data(type, length, lake)

        else:
            print("I don't understand.\
            Please enter a valid command or type 'help'.")