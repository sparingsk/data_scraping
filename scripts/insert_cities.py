import json

from bs4 import BeautifulSoup

def save_file(path, data):
  with open(path, 'w', encoding='utf8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
  print('Data saved successfully to {}'.format(path))

data = None
with open('data/data.json', encoding='utf8') as f:
  data = json.load(f)

for sport in data:
  venues = []
  for venue in sport['venues']:
    soup = BeautifulSoup(venue['info']['address'], features="html.parser")

    a = soup.find('a')
    if a:
      venue['info']['city'] = a.text
    else:
      venue['info']['city'] = None

    venues.append(venue)
    
  sport['venues'] = venues

save_file('data/data_with_cities.json', data)