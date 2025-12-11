import argparse
parser = argparse.ArgumentParser(description="Simple argparse demo.")
parser.add_argument("name", type=str, default="students", help="Your name")

args = parser.parse_args()

name = args.name
print(name)

# parser = argparse.ArgumentParser()
# parser.add_argument("username", help="Your first name")

#  
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
import argparse
import requests


# user_name = input("input your user name: ")

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Input your user name")
# print(user_name)
args = parser.parse_args()
user_name = args.username
print(user_name)


url = f"https://api.github.com/users/{user_name}/events"
response = requests.get(url=url)
print(response.status_code)
json_response = response.json()
print(json_response)
print(type(json_response))
# for event in json_response:
if json_response == 'CreateEvent':
    repo_name = json_response['repo']['name']
    repo_url = json_response['repo']['url']
    message = f"{user_name} created a github repo {repo_name} found at {repo_url}"
    print(message)
else :
    print("No CreateEvent found.")
