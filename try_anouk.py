import pandas as pd
account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)

account_data.columns = ['username', 'email', 'password']
fish_data.columns = ['type', 'length', 'lake', 'username']
<<<<<<< Updated upstream

fishtype_list = ['perch' , 'pike' , 'catfish']

while True:
    # menu:
    print(f'Fish species in this tournament: ')
    for index, item in enumerate(fishtype_list):
        print(f'{index} : {item}')
    print(f'type \'exit\' to exit the program\n')
    break

while True:
    type = input("Type number: ")
    try:
        if type == 1 or 2 or 3:
            type = int(type)
            print(fish_data.loc[fish_data['type'] == type].sort_values('length', ascending=False).reset_index(drop=True))
            break
    except:
        print("Error")



#type = int(input("Type number: "))
#print(fish_data.loc[fish_data['type']==type].sort_values('length', ascending=False).reset_index(drop=True))

=======

fishtype_list = ['perch' , 'pike' , 'catfish']

type = 2


type = input('select the species you caught form the list above: ')
int_type = int(type)
if type == 0:
    print(fish_data.loc[(fish_data['0'] == type)].sort_values('length', ascending=False).reset_index(drop=True))
elif type == 1:
    print(fish_data.loc[(fish_data['1'] == type)].sort_values('length', ascending=False).reset_index(drop=True))
>>>>>>> Stashed changes
