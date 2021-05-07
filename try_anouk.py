import pandas as pd
accounts = pd.read_csv("accounts.txt", delimiter = " ")
print(accounts)
print(accounts.columns)