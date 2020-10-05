import os

b = os.path.getsize('data/images/Tenis/Kurty Lazany.jpg')

base_path = 'data/images'

def analyze_sizes():
  image_dirs = os.listdir(base_path)
  count = 0

  number_of_images = 0
  for dir in image_dirs:
    images = os.listdir(os.path.join(base_path, dir))
    number_of_images += len(images)
    for image in images:
      size = os.path.getsize(os.path.join(base_path, dir, image))
      if size/1024 > 256:
        print(size/1024, image)
        count += 1

  print(number_of_images)

  return count

c = analyze_sizes()

print(c)