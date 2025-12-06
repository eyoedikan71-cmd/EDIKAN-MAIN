my_first_variable = 1  
my_first_variable =2 

print(type(my_first_variable))
print(my_first_variable)


my_first_variable = "Now, I'm a string." 

print(my_first_variable)

def add_two_numbers(number_one, number_two):
  total = number_one + number_two
  print(total)  

add_two_numbers(3, 4)


def add_two_numbers(number_one, number_two):
        return number_one + number_two
add_two_numbers(3, 4)
sum_with_return = add_two_numbers(5, 6)
print(sum_with_return)


def add_two_numbers(number_one, number_two):
  result = number_one + number_two
# add_two_numbers(5, 7)
print(add_two_numbers(5, 7))

import math

tech=math.pow(2,4) 
print(tech)


placeholders = ["spam", "ham", "eggs", "green_spam", "green_ham", "green_eggs"]

while placeholders:
  print(placeholders.pop(0))

word_list = ["bird", "chicken", "barrel", "bongo"]

for word in word_list:
  if word.startswith("b"):
    print(f"{word.title()} starts with a B.")
  else:
    print(f"{word.title()} doesn't start with a B.")

for number in range(1, 7):
  if number % 2 == 0:
    print(f"{number} is even.")
  else:
    print(f"{number} is odd.")

for number in range(3, 15, 2):
  if number % 2 == 0:
    print(f"{number} is even.")
  else:
    print(f"{number} is odd.")

for index, word in enumerate(word_list):
  if word.startswith("b"):
    print(f"{word.title()} (at index {index}) starts with a B.")
  else:
    print(f"{word.title()} (at index {index}) doesn't start with a B.")

word_lt = ["cat", "chicken", "barrel", "apple", "spinach"]
category_list = ["mammal", "bird", "thing", "fruit", "vegetable"]

for index, word in enumerate(word_lt):
  print(f"\n{word.title()} is in category: {category_list[index]}.")


word_thing = ["bird", "chicken", "barrel", "bongo", "sliver", "apple", "bear"]

# This will skip *bird*, at index 0
for index, word in enumerate(word_thing):
    if index == 0:
        continue
    if word.startswith("b"):
        print(f"{word.title()} (at index {index}) starts with a b.")
print("\n")

word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple"]
for index, word in enumerate(word_list):
  if word.startswith("b"):
    print(f"{word.title()} (at index {index}) starts with a B.")
  elif word == "sliver":
    break
  else:
    print(f"{word.title()} doesn't start with a B.")
print("loop broken.")


# student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
# # round_scores(student_scores)
# # [40, 39, 95, 80, 25, 31, 70, 55, 40, 90]
# count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40])
# # 5
# above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75)
# # [90,75,83,96]

# """Where the highest score is 100, and failing is <= 40.
#        "F" <= 40
#  41 <= "D" <= 55
#  56 <= "C" <= 70
#  71 <= "B" <= 85
#  86 <= "A" <= 100
# """

# letter_grades(highest=100)
# [41, 56, 71, 86]


# """Where the highest score is 88, and failing is <= 40.
#        "F" <= 40
#  41 <= "D" <= 52
#  53 <= "C" <= 64
#  65 <= "B" <= 76
#  77 <= "A" <= 88
# """

# letter_grades(highest=88)
# [41, 53, 65, 77]

# student_scores = [100, 99, 90, 84, 66, 53, 47]
# student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
# student_ranking(student_scores, student_names)

# # ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66', '6. Bern: 53', '7. Fred: 47']

# perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]])
# ["Alex", 100]

# perfect_score(student_info=[["Charles", 90], ["Tony", 80]])
# []

import requests

# url = 'https://w3schools.com/python/demopage.htm'

# url = 'https://www.w3schools.com/python/demopae.htm'
# https://www.google.com/search
# params = {'q':''}
# response = requests.get(url, params=params)
# #response code

# if response.status_code == 200:
#     print("Page successfully reetrieved")
#     print(response.text)
# else:
#     print(response.status_code)


# url = "https://api.github.com/users/eyoedikan71-cmd/events"
# r = requests.get(url=url)
# print(r.status_code)

# # print(r.text)
# print(r.json())


# Task:
# <user> created a github repo <repo_name> found at <repo_url>
# 1. ask user for input
# 2. format username to template url -- "https://api.github.com/users/<username>/events"
#3. make request to formattted url
#4. get json response
#3. check if event is createeevent, print a formmatted message


# user_name = input("input your user name: ")
# print(user_name)
# url = (f"https://api.github.com/users/{user_name}/events")

# Task:
# <user> created a github repo <repo_name> found at <repo_url>
# 1. ask user for input
# 2. format username to template url -- "https://api.github.com/users/<username>/events"
#3. make request to formattted url
#4. get json response
#3. check if event is createeevent, print a formmatted message

user_name = input("input your user name: ")
print(user_name)
url = f"https://api.github.com/users/{user_name}/events"
response = requests.get(url=url)
print(response.status_code)
json_response = response.json()
for event in json_response:
    if event['type'] == 'CreateEvent':
        repo_name = event['repo']['name']
        repo_url = event['repo']['url']
        message = f"{user_name} created a github repo {repo_name} found at {repo_url}"
        print(message)
  

