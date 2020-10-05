import os
import json
from unidecode import unidecode

images_list = os.listdir('data/images')

def save_file(path, data):
  with open(path, 'w', encoding='utf8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
  print('Data saved successfully to {}'.format(path))

data = None
with open('data/data_with_cities.json', encoding='utf8') as f:
  data = json.load(f)

for sport in data:
  venues = []
  for venue in sport['venues']:
    name = venue['name']
    image_name = unidecode(name) + '.jpg'
    if image_name in images_list:
      venue['info']['image'] = image_name
    venues.append(venue)
    
  sport['venues'] = venues

save_file('data/data_with_cities_and_images.json', data)