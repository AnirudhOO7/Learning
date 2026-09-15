users = [
    {"name": "Sam", "age": 30, "active": True},
    {"name": "Alex", "age": 17, "active": False},
    {"name": "Jo", "age": 25, "active": True},
    {"name": "Pat", "age": 45, "active": True},
]

def active_names(users):
    names = []
    for user in users:
        if user["active"] == True:
            names.append(user["name"])

    return names

def average_age(users):
    sum = 0
    for user in users:
        sum+= user["age"]
    avg = sum/len(users)
    return avg

def find_by_name(users, name):
    for user in users:
        if user["name"] == name:
            return True
    return None

print(find_by_name(users, "Jo"))    
print(find_by_name(users, "Nobody")) 