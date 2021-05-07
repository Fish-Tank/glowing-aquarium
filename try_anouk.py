import pandas as pd
account_data = pd.read_csv("accounts.txt", delimiter=" ")
fish_data = pd.read_csv("fish.txt", delimiter = " ")

password = "hallo"


personal_catches = (fish_data.loc[fish_data['password'] == password])
print(personal_catches)


#for index, row in accounts.iterrows():
#    print(index, row['username'])
#print(ad.columns)
#print(fish_data.columns)

#print(fish_data.loc[fish_data["password"] == "hallo"])
#print(fish_data.sort_values(["fish", "length"],ascending=[1,0]))