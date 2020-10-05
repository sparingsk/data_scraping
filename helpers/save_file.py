import json

def save_file(path, data):
  with open(path, 'w', encoding='utf8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
  print('Data saved successfully to {}'.format(path))