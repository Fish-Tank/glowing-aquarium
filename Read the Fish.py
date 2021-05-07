with open ("accounts.txt", "r") as accounts:
    lines = accounts.readlines()
    print(lines)

user_names = []
email = []
password = []
for l in lines:
    as_list = l.split(" ")
    user_names.append(as_list[0])
    email.append(as_list[1])
    password.append(as_list[2])

print(user_names)
print(email)
print(password)

accounts.close()

with open ("fish.txt", "r") as fish:
    lines = fish.readlines()
    print(lines)

fish_type = []
length = []
lake = []
password = []
for l in lines:
    as_list = l.split(" ")
    fish_type.append(as_list[0])
    length.append(as_list[1])
    lake.append(as_list[2])
    password.append(as_list[3])

print(fish_type)
print(length)
print(lake)
print(password)

fish.close()



