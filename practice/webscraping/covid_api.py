import requests
import pandas as pd

if __name__ == '__main__':

    BASE_URL = 'https://covid-193.p.rapidapi.com/'
    api_key = '####'
    api_host = 'covid-193.p.rapidapi.com'

    response = requests.get(
        url=f'{BASE_URL}countries',
        headers={
            'X-RapidAPI-Host': api_host,
            'X-RapidAPI-Key': api_key
        }
    )
    countries = response.json()['response']
    print(countries)

    response = requests.get(
        url=f'{BASE_URL}statistics',
        headers={
            'X-RapidAPI-Host': api_host,
            'X-RapidAPI-Key': api_key
        }
    )
    statistics = response.json()['response']
    print(statistics)

    response = requests.get(
        url=f'{BASE_URL}history',
        headers={
            'X-RapidAPI-Host': api_host,
            'X-RapidAPI-Key': api_key
        },
        params={
            'country': 'All'
        }
    )
    history = response.json()['response']
    cases = [list(h['cases'].values()) + [h['country']] for h in history]
    df = pd.DataFrame.from_records(cases)
    print(df.iloc[0])
