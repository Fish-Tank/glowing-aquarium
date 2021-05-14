"results > show me the biggest 5 catchtes",
    "data > show me other information \n",


elif user_input == "results":
lake_data = open("fish.txt", "r")
row = []
for row in lake_data:
    sum()

print("Content of data: ")
print("So far so good")

account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None)
fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)

account_data.columns = ['username', 'email', 'password']
fish_data.columns = ['type', 'length', 'lake', 'username']

while True:
    lakes = input("Enter the lake: ")
    new_fish_data = fish_data[['lake']]
    row = new_fish_data.to_csv(header=None, index=False).strip('\n').split('\n')
    if lakes in row:
        lake_catches = (fish_data.loc[fish_data['lakes'] == lakes])
        print(lake_catches)
        break
# cols = list(fish_data.columns.values)
# fish_data = fish_data[cols[1]]
# biggest = fish_data.head(5)
# print(biggest)
# biggest.sort_values('length', ascending=False))
# fish_data['Total'] = fish_data.iloc[:, 1:1].sum(axis=1) -> sollte summe aus länge geben

# fish_data = fish_data.drop(columns=['lake']) -> sollte lake entfernen

# print(fish_data['Total'] = fish_data['length']) -> funktioniert nicht! sollte eigentlich für 5 grösste fische geben
# (fish_data.head(5))

# print(fish_data.sort_values(['length', 'lake'], ascending=True)) -> beide werte werden aussortiert

# print(fish_data.sort_values('length', ascending=False))

# print(fish_data.describe()) -> statistik von liste

# print(fish_data.loc[fish_data['lake'] == "Bodensee"]) -> gibt alle Fische vom Bodensee her

# (fish_data.head(3)) oberste drei aus der ganzen liste

# print(fish_data.columns) gibt kolumnen her

# print(fish_data[['type', 'length']]) gibt art und länge her

# print(fish_data.iloc[1:10]) gibt die ersten 10 spalten her

# for index, row in fish_data.iterrows():

# print(index, row['lake']) gibt alle seen wieder

# account_data = pd.read_csv("accounts.txt", delimiter=" ", header=None) -> war teil für fisch suche
# fish_data = pd.read_csv("fish.txt", delimiter=" ", header=None)
# account_data.columns = ['username', 'email', 'password']
# fish_data.columns = ['type', 'length', 'lake', 'username']
# while True:
# lake1 = input("Enter a lake and see all the catches:>> ")
# new_fish_data = fish_data[['lake']]
# row = new_fish_data.to_csv(header=None, index=False).strip('\n').split('\n')
# if lake1 in row:
# lake_catches = (fish_data.loc[fish_data['lake']] == lake1)
# print(lake_catches)
# break