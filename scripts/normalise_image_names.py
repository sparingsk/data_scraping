import os
from unidecode import unidecode

def normalise_and_move():
  folder_list = os.listdir('data/images')

  for folder in folder_list:
    folder_path = 'data/images/' + folder
    image_list = os.listdir(folder_path)
    for image in image_list:
      normalised_name = unidecode(image)
      os.rename(os.path.join(folder_path, image), os.path.join('data/images', normalised_name))

  print('Success !')

normalise_and_move()