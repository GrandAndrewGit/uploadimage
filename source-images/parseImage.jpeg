import requests
from bs4 import BeautifulSoup
import json
import os
import time


# GET and save page one time
# url = 'https://okna.ua/ua/'

# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
# }

# req = requests.get(url, headers=headers)
# src = req.text

# with open('pages/okna-index.html', 'w') as file:
#     file.write(src)

# ------------------------------


# SAVE starting urls to json file
# with open('pages/okna-index.html') as file:
#     src = file.read()

# soup = BeautifulSoup(src, 'lxml')

# article_list = []

# all_news = soup.find('div', class_='news__articles').find_all('a')

# for i in all_news:
#     if i.find(class_='preview__title'):
#         news_dict = {}
#         news_dict['url'] = i.get("href")
#         news_dict['title'] = i.find(class_='preview__title').text.replace('\n', '').strip()
#         article_list.append(news_dict)

# with open('data/articles.json', 'w') as json_file:
#     json.dump(article_list, json_file, indent=4, ensure_ascii=False)

#-----------------------------------

with open('data/articles.json', 'r') as file:
    data = json.load(file)

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

# GET images
# img_counter = 1
# for i in data:
#     inner_url = i['url']
#     req = requests.get(inner_url, headers=headers)
#     src = req.text
#     soup = BeautifulSoup(src, 'lxml')

#     cover = soup.find('picture').find('img')
#     cover_url = cover['src']

#     cover_response = requests.get(cover_url, headers=headers)
#     cover_response_content = cover_response.content

#     os.makedirs(f'media/{img_counter}', exist_ok=True)

#     with open(f'media/{img_counter}/{img_counter}.jpg', 'wb') as file:
#         file.write(cover_response_content)
#     img_counter += 1


# THE WHOLE code for parsing url and images
def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
                return data
            except:
                return {}
    except FileNotFoundError:
        return {}
    
# existing_data = read_json_file('data/articles-details.json')
# for key, values in existing_data.items():
#     print(values['url'])

counter = 1
for i in data:
    existing_data = read_json_file('data/articles-details.json')

    try:
        inner_url = i['url']
        req = requests.get(inner_url, headers=headers)
        src = req.text

        soup = BeautifulSoup(src, 'lxml')
        page_h1 = soup.find('h1').text
        date = soup.find('time', class_='date').get('datetime')
        cover = soup.find('picture').find('img')
        cover_url = cover['src']
        cover_response = requests.get(cover_url, headers=headers)
        cover_response_content = cover_response.content

        os.makedirs(f'media/{counter}', exist_ok=True)
        with open(f'media/{counter}/{counter}.jpg', 'wb') as file:
            file.write(cover_response_content)

        article = {}
        article['url'] = inner_url
        article['title'] = page_h1
        article['date'] = date
        article['img_folder'] = counter

        number = 'n' + str(counter)
        existing_data[number] = article

        with open('data/articles-details.json', 'w') as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)
    except:
        inner_url = i['url']
        article = {}
        article['url'] = inner_url
        article['error'] = 'SOME ERROR'

        number = 'n' + str(counter)
        existing_data[number] = article

        with open('data/articles-details.json', 'w') as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)

    counter += 1

    print(f'Request number {counter}')
    time.sleep(1)

