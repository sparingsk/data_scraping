import os

def get_sport_names():
  filelist = os.listdir('data/separate')

  sports = [name.split('.')[0] for name in filelist]

  return sports

sports = get_sport_names()

for sport in sports:
  print(r"{ name: '" + sport + r"' },")