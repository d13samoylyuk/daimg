from PIL import Image

from modules.basic import (get_ratios_tendency, get_ratios_tendency,
                           two_number_ratio)
from modules.system import get_screen_info


Debug = True
def DebugPrint(*args, **kwargs):
    if Debug:
        print(*args, **kwargs)


img_path = '/home/daniel/Desktop/NASA_WP/images/CatsPaw_Webb_1822_12.jpg'
img = Image.open(img_path)



# Loading info about current screen
screen = get_screen_info()

DebugPrint('screen info:', screen)



# Create black scene with the size of the screen
scene = Image.new('RGB', (screen['width'], screen['height']), (0, 0, 0))



# getting ratios tendency to tell if the screen and image
# are the same orientation
ration_img = two_number_ratio(img.width, img.height)
ratios_tendency = get_ratios_tendency(ration_img, screen['ratio'])

DebugPrint('ratios tendency', ratios_tendency)




# Calculate new image size to fit screen height first
if ratios_tendency:
    # image is same orientation as screen or square - fit to screen width
    pass

new_img_width = int(screen['height'] * img.width / img.height)
new_img_height = screen['height']
new_img_size = (new_img_width, new_img_height)

DebugPrint('img scale', img.width, img.height)
DebugPrint('img new scale', new_img_width, new_img_height)



# Apply new size to the image
img = img.resize(new_img_size)



# Calculate position to center the image on the scene
x = 0#(screen['width'] - new_img_size[0]) #// 2
y = (screen['height'] - new_img_size[1]) // 2

scene.paste(img, (x, y))

scene.save('_test/scene1.jpg')