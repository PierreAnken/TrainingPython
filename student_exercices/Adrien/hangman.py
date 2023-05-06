import requests


def get_quotes(url):
    # Make a GET request and get response data
    response = requests.get(url)

    # parse json and get the quote list back
    data = response.json()
    return data


if __name__ == '__main__':
    # Get all quotes from api
    api_url = 'https://type.fit/api/quotes'
    all_quotes = get_quotes(api_url)
    print(all_quotes)


#

