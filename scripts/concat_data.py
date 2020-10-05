import os
import json

def save_file(path, data):
  with open(path, 'w', encoding='utf8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
  print('Data saved successfully to {}'.format(path))

filelist = os.listdir('data/separate')

def join_jsons():
  full_data = []
  for filename in filelist:
    with open('data/separate/' + filename, 'r', encoding='utf8') as f:
      data = json.load(f)
      full_data.append(data)
  save_file('data/data.json', full_data)

join_jsons()