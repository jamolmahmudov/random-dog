import requests


def get_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()[0]['url']
    
    return response.status_code