from PIL import Image

from modules.basic import fit_num_pairs
from modules.files import read_csv_file
from modules.program import get_path
from modules.system import get_screen_info


Debug = True
def DebugPrint(*args, **kwargs):
    if Debug:
        print(*args, **kwargs)


def setup_image(img_id: int):

    image_info = read_csv_file(get_path('history'))[img_id-1]

    img_path = (get_path('images_store'), image_info['file_name'])

    img = Image.open('/'.join(img_path))



    # Loading info about current screen
    screen = get_screen_info()

    DebugPrint('screen info:', screen)



    # Create black scene with the size of the screen
    scene = Image.new('RGB', (screen['height'], screen['width']), (10, 10, 10))


    # Calculate new image size to fully fit the screen,
    #  which means that the biggest sides of an image must
    #  be the same size as the biggest sides of the screen
    new_img_size = fit_num_pairs((screen['width'], screen['height']),
                                 (img.width, img.height))

    DebugPrint('img scale', img.width, img.height)
    DebugPrint('img new scale', new_img_size)
    


    # Apply new size to the image
    img = img.resize(new_img_size)



    # Calculate position to center the image on the scene
    x = 0#(screen['width'] - new_img_size[0]) #// 2
    y = (screen['height'] - new_img_size[1]) // 2

    scene.paste(img, (x, y))

    scene.save('_test/scene1.jpg')