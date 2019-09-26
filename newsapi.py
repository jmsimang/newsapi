import requests
import json
import sys
from datetime import datetime, timedelta


def retrieve_api_details() -> object:
    try:
        with open('config.txt', 'r', encoding='utf-8') as file:
            return file.readline()
    except IOError as ioe:
        print('ERROR! \n{}'.format(ioe))


def process_query(query) -> None:
    api_key = retrieve_api_details()
    previous_month = datetime.now() - timedelta(30)
    from_date = datetime.strftime(previous_month, '%Y-%m-%d')
    url = f'https://newsapi.org/v2/everything?q={query}&from={from_date}&sortBy=popularity&apikey={api_key}'
    output_file = f'newsapi_results_{query}.json'
    response = requests.get(url).json()
    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(response, output, sort_keys=False, indent=4, ensure_ascii=False)
    print(f'DONE! OUTPUT FILE WITH DATA SAVED AS {output_file}')


if __name__ == '__main__':
    try:
        if len(sys.argv) < 3:
            q = sys.argv[1].lower()
            process_query(q)
        else:
            queries = sys.argv[1:]
            for q in queries:
                process_query(q.lower())
    except IndexError as ie:
        print(f'ERROR! \n{ie}')
