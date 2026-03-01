from PIL import Image

from modules.basic import fit_num_pairs
from modules.files import read_csv_file
from modules.program import get_path
from modules.system import get_screen_info
from modules.text_to_image import text_field_and_wrap, text_to_field


FONT_SIZE = 30


class Padding:
    '''
    Percentaged to the screen
    '''
    text = 0.25


Debug = True
def DebugPrint(*args, **kwargs):
    if Debug:
        print(*args, **kwargs)


def setup_image(img_id: int):
    # Loading info about current screen
    screen = get_screen_info()
    # Create black scene with the size of the screen
    scene = Image.new('RGB', (screen['width'], screen['height']),
                      (10, 10, 10))
    
    DebugPrint('screen info:', screen)


    image_info = read_csv_file(get_path('history'))[img_id-1]
    img_path = (get_path('images_store'), image_info['file_name'])
    img = Image.open('/'.join(img_path))
    # Calculate new image size to fully fit the screen
    new_img_size = fit_num_pairs((screen['width'], screen['height']),
                                 (img.width, img.height))

    DebugPrint('img scale', img.width, img.height)
    DebugPrint('img new scale', new_img_size)
    


    # Calculate space for the image description,
    # if there is any
    screen_area = screen['width'] * screen['height']
    image_area = new_img_size[0] * new_img_size[1]
    left_over_area = screen_area - image_area

    if screen['height'] == new_img_size[1]:
        text_field_size = (screen['width'] - new_img_size[0], 
                      screen['height'])
    else:
        text_field_size = (screen['width'], 
                      screen['height'] - new_img_size[1])
        
    DebugPrint('text field size', text_field_size)
    DebugPrint(
        '\n   screen area: ', screen_area,
        '\n    image area: ', image_area,
        '\nleft over area: ', left_over_area)
    

    # Get the text image
    description = image_info['description']
    text_size = (
        text_field_size[0] - round(text_field_size[0] * Padding.text),
        text_field_size[1] - round(text_field_size[1] * Padding.text))

    text_box_size, wrapped_text = text_field_and_wrap(
        scene_width=text_size[0],
        text=description,
        font_size=FONT_SIZE)

    text_image = text_to_field(
        text=wrapped_text,
        fields_size=text_box_size,
        font_size=FONT_SIZE)

    # Create a text field image and
    # paste the text image on it
    text_field_img = Image.new(
        'RGBA', text_field_size, (0, 0, 0, 0))
    
    x_text = round(
        (text_field_size[0] - text_box_size[0]) / 2)
    y_text = round(
        (text_field_size[1] - text_box_size[1]) / 2)
    text_field_img.paste(
        text_image, (x_text, y_text))


    # Apply padding to the image size
    pass


    # Apply new size to the image
    img = img.resize(new_img_size)


    # Calculate the position to center the image on the scene
    x = 0#(screen['width'] - new_img_size[0]) #// 2
    y = 0#(screen['height'] - new_img_size[1]) // 2


    # Calculate the position of the on the wallpaer scene
    x_text_field = new_img_size[0]
    y_text_field = 0

    # Puzzle the wallpaper
    scene.paste(img, (x, y))
    scene.paste(text_field_img,
                (x_text_field, y_text_field))

    scene.save('_test/scene1.jpg')