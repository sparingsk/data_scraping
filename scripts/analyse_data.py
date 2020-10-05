import json

data = None
with open('data/data.json', encoding='utf8') as f:
  data = json.load(f)

def contains(list_of_dicts, obj):
  for d in list_of_dicts:
    if d['name'] == obj['name']:
      return True
  return False

def analyse(data):

  venues = []

  for sport in data:
    for venue in sport['venues']:
      if contains(venues, venue):
        for v in venues:
          if v['name'] == venue['name']:
            v['sports'].append(sport['name'])
            break
      else:
        venue['sports'] = [sport['name']]
        venues.append(venue)

  return venues

venues = analyse(data)

print(len(venues))

for v in venues:
  if len(v['sports']) > 1:
    print(v['name'], v['sports'])

