import requests

def fetch_repos(username):
    
    URL = f'https://api.github.com/users/{username}/repos'
    req = requests.get(URL)

    data_array = req.json()
    
    return data_array
        