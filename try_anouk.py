import pandas as pd
account_data = pd.read_csv("accounts.txt", delimiter=" ")
fish_data = pd.read_csv("fish.txt", delimiter=" ")

input = ('')
print(account_data)

print(fish_data.sort_values('length', ascending=False).reset_index(drop=True))
