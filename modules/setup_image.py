from PIL import Image


img_path = '/home/daniel/Desktop/NASA_WP/images/CatsPaw_Webb_1822_12.jpg'

screen_info = 13

img = Image.open(img_path)
background = Image.new('RGB', (1920, 1080), (0, 0, 0))