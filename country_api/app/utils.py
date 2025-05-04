import requests

def fetch_country_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    data = fetch_country_data()
    print(data[0])