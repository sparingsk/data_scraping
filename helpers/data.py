import os

def get_info_key(key):
  keys = {
    'Kategória': 'category',
    'Aktivity a služby': 'activities',
    'Otváracie hodiny': 'opening_hours',
    'Cenník': 'price_list',
    'Adresa': 'address',
    'Telefón': 'phone',
    'E-mail': 'email',
    'Web': 'web',
    'GPS': 'GPS'
  }

  if not keys[key]:
    print('Error', key)

  return keys[key]

def get_remaining_sports(url_data):
  fetched_files = os.listdir('data/separate')
  fetched_sports = [filename.split('.')[0] for filename in fetched_files]

  return [data for data in url_data if data['name'] not in fetched_sports]

def get_remaining_sports(url_data, dir='data/separate', recursive=False):
  fetched_files = os.listdir(dir)
  fetched_sports = [filename.split('.')[0] for filename in fetched_files]

  if recursive:
    return [data for data in url_data if len(os.listdir(os.path.join(dir, data['name']))) == 0]

  return [data for data in url_data if data['name'] not in fetched_sports]

def exists_image(sport, venue):
  imagefiles = os.listdir(os.path.join('data/images', sport))
  venues = [filename.split('.')[0] for filename in imagefiles]

  if venue in venues:
    return True

  return False

def replace_chars(s, chars=['*', '/']):
  for char in chars:
    s = s.replace(char, '')
  return s