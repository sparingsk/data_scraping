import requests
from bs4 import BeautifulSoup
import time
import shutil

from helpers.data import get_info_key, get_remaining_sports, exists_image, replace_chars
from helpers.save_file import save_file

URL = 'https://sportoviska.sk'

def get_sport_urls():
  response = requests.get(URL)

  print(response.status_code)

  soup = BeautifulSoup(response.text, features="html.parser")
  sports_list = soup.find(id='jr_treeView16')

  url_data = []

  for e in sports_list:
    a = e.find('a')
    if a != -1:
      data = {
        'name': a.text,
        'url': a['href']
      }
      url_data.append(data)

  return url_data

def get_sport_venues(url):

  print('Calling url {}'.format(url))

  response = requests.get(url)

  soup = BeautifulSoup(response.text, features='html.parser')

  number_of_venues_tag = soup.find('td', {
    'class': 'jr_pagenav_results'
  })

  number_of_venues = number_of_venues_tag.text.split(' ')[len(number_of_venues_tag.text.split(' ')) - 1]
  number_of_calls = int(number_of_venues)//50 + 1

  venues = []

  for i in range(1, number_of_calls + 1):
    response = requests.get(url, params={
      'limit': 50,
      'page': i
    })

    soup = BeautifulSoup(response.text, features='html.parser')

    list_tag = soup.find(id='gm_listingColumn')
    venues_tags = list_tag.findAll('div', {
      'class': 'contentTitle'
    })

    for tag in venues_tags:
      a = tag.find('a')
      venue = {
        'name': a.text,
        'url': URL + a['href']
      }

      venues.append(venue)

  return venues

def get_venue_information(url):

  print('Calling url {}'.format(url))

  info = {
    'description': None,
    'category': None,
    'activities': None,
    'opening_hours': None,
    'price_list': None,
    'address': None,
    'phone': None,
    'email': None,
    'web': None,
    'GPS': None,
  }

  response = requests.get(url)

  if response.status_code != 200:
    print('STATUS: {}'.format(response.status_code))

  soup = BeautifulSoup(response.text, features="html.parser")

  # description
  description = soup.find('div', {
    'class': 'contentFulltext'
  })
  info['description'] = str(description)
  # info['description'] = description.text

  # information from tables
  tables = soup.findAll('table', {
    'class': 'fieldGroupTable'
  })

  print(len(tables))

  for table in tables:
    for tr in table.findAll('tr'):
      label = tr.find('td', {
        'class': 'fieldLabel'
      })
      if not label or not label.text:
        continue
      key = get_info_key(label.text)

      value = tr.find('td', {
        'class': 'fieldValue'
      })

      info[key] = str(value)
      # info[key] = value.text

  return info

def get_main_image(url, sport):

  print('Calling url {}'.format(url))

  response = requests.get(url)
  soup = BeautifulSoup(response.text, features="html.parser")

  header = soup.find('meta', {
    'property': 'og:title'
  })
  name = header['content']
  name = replace_chars(name)

  image_div = soup.find('div', {
    'class': 'itemMainImage'
  })
  if not image_div:
    print('No picture, aborting')
    return
  a = image_div.find('a')

  image_url = a['href']

  image_response = requests.get(image_url, stream=True)

  image_name = 'data/images/' + sport + '/' + name + '.jpg'
  with open(image_name, 'wb') as f:
    image_response.raw.decode_content = True
    shutil.copyfileobj(image_response.raw, f)

# u = 'https://sportoviska.sk/aerobik-fitness/banskobystricky/fit-studio-hit-banska-bystrica'

# get_main_image(u, 'Tenis')

url_data = get_sport_urls()

url_data = url_data[16:17]

# url_data = get_remaining_sports(url_data, 'data/images', True)

print(len(url_data))
print(url_data)

# images
for u in url_data:
  venues = get_sport_venues(u['url'])
  for i, v in enumerate(venues):
    if not exists_image(u['name'], v['name']):
      print('No.', i, v['name'])
      get_main_image(v['url'], u['name'])
      time.sleep(1)

# venue info
# for u in url_data[:16]:
#   venues = get_sport_venues(u['url'])
#   for i, v in enumerate(venues):
#     print('No.', i, v['name'])
#     info = get_venue_information(v['url'])
#     v['info'] = info
#     time.sleep(1)
#   u['venues'] = venues

#   path = 'data/separate/' + u['name'] + '.json'
#   save_file(path, u)

# save_file('data/data.json', url_data)