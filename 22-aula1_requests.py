import requests
from bs4 import BeautifulSoup 


url = 'https://jsonplaceholder.typicode.com'
response = requests.get(url)
response.content.decode('utf-8')
raw_response = response.text
parsed_html = BeautifulSoup(raw_response, 'html.parser')


# print(parsed_html.title.text)

heading = parsed_html.select_one("body > div:nth-child(3) > section.container.mx-auto.max-w-4xl.mb-six > h2")

if heading is not None:
    pai_do_trem = heading.parent

    if pai_do_trem is not None:
        for p in pai_do_trem.select('p'):
            print(p.text)