# with open('lesson10files/weekdays.txt') as week_file:
#     weekdays = [day.strip() for day in week_file.readlines()]
    
# print(weekdays)

# username = input("Enter your username: ")

# with open('user_info.txt', 'w') as file_object:
#     file_object.write(username)

# with open('user_info.txt') as file_object:
#     username = file_object.read()

# print(f"Welcome back, {username}!") 

# import json

# cj = {}
# cj['first_name'] = 'John'
# cj['last_name'] = 'Doe'
# cj['cars'] = [{
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'color': 'red'},
#     {'brand': 'BMW',
#     'model': 'X5',
#     'color': 'blue'}]
# cj['has_a_dog'] = True
# cj['money_in_pocket'] = 5000

# with open('cj.json', 'w') as file_object:
#     json.dump(cj, file_object)


# import json

# with open('cj.json') as file_object:
#     cj = json.load(file_object)

# for key, value in cj.items():
#     print(f"{key}: {value}")







with open('myfile.txt', 'w', encoding='utf-8') as f:
   f.write("Hello file world!")

with open('myfile.txt', 'r') as f:
    text_file = f.read()
    print(text_file)
    