import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
user_name = input("input your user name: ")
logging.info({user_name})
url = f"https://api.github.com/users/{user_name}/events"
response = requests.get(url=url)
logging.info({response.status_code})
json_response = response.json()
# print(json_response)
for event in json_response:
    if event['type'] == 'CreateEvent':
        repo_name = event['repo']['name']
        repo_url = event['repo']['url']
        message = f"{user_name} created a github repo {repo_name} found at {repo_url}"
        # print(message)
        logging.info({message})
