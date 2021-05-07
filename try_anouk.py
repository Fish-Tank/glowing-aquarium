import pandas as pd
account_data = ad = pd.read_csv("accounts.txt", delimiter=" ")
#fish_data = fd = pd.read_csv("fish.txt", delimiter=" ")

#for index, row in accounts.iterrows():
#    print(index, row['username'])
print(ad.columns)
#print(fd.columns)

#fd.loc[fd["password"] == "hallo"]

