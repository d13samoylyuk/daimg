from PIL import Image

from debug import DebugPrint
from modules.basic import aspect_fit
from modules.files import read_csv_file
from modules.program import get_path, last_record
from modules.system import get_font_size, get_screen_info
from modules.text_to_image import text_field_and_wrap, text_to_field


FONT_SIZE = get_font_size()
wallpapers_folder = get_path("wallpapers_store")
WALLPAPERS_FOLDER = wallpapers_folder


class Padding:
    '''
    Proportion to the screen
    '''
    text = 0.25


def setup_image(img_id: int = None,
                save_path = WALLPAPERS_FOLDER,
                wp_file_name = None):
    global FONT_SIZE
    font_size_al = FONT_SIZE

    if not img_id:
        img_id = int(last_record()['id'])

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
    new_img_size = aspect_fit((screen['width'], screen['height']),
                                 (img.width, img.height))

    DebugPrint('img scale', img.width, img.height)
    DebugPrint('img new scale', new_img_size)
    


    # Calculate space for the image description,
    # if there is any
    screen_area = screen['width'] * screen['height']
    image_area = new_img_size[0] * new_img_size[1]
    left_over_area = screen_area - image_area

    is_text_on_right = screen['height'] == new_img_size[1]

    # Determine the size of a field that left
    # after the image which then would be used
    # as the Text Field - (Width, Height)

    text_field_size = (0, 0)
    if is_text_on_right:
        text_field_size = (screen['width'] - new_img_size[0], 
                      screen['height'])
    else:
        text_field_size = (screen['width'], 
                      screen['height'] - new_img_size[1])
        
    DebugPrint('text field size', text_field_size,
               '\n  is text on the right side', is_text_on_right)
    

    # Get the text image
    description = image_info['description']
    text_size = (
        text_field_size[0] - round(text_field_size[0] * Padding.text),
        text_field_size[1] - round(text_field_size[1] * Padding.text))

    
    for step in range(11):
        text_box_size, wrapped_text = text_field_and_wrap(
            scene_width=text_size[0],
            text=description,
            font_size=font_size_al)

        if text_box_size[1] > text_size[1]:
            font_size_al -= 1
            print(step+1)
            if step == 10:
                font_size_al = None
                break
        else:
            break

    DebugPrint(f'Suggest font size: {FONT_SIZE}, used: {font_size_al}')

    if font_size_al:
        text_image = text_to_field(
            text=wrapped_text,
            fields_size=text_box_size,
            font_size=font_size_al)

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

        # Calculate the position of the text on the wallpaer scene
        if is_text_on_right:
            x_text_field = new_img_size[0]
            y_text_field = 0
        else:
            x_text_field = 0
            y_text_field = new_img_size[1]


    # Apply padding to the image size
    pass


    # Apply new size to the image
    img = img.resize(new_img_size)


    # Calculate the position to center the image on the scene
    # If image is vertical
    x = 0
    y = 0

    # Puzzle the wallpaper
    scene.paste(img, (x, y))

    if font_size_al:
        scene.paste(text_field_img,
                    (x_text_field, y_text_field))

    if not wp_file_name:
        wp_file_name = f'{img_id}_{image_info['file_name']}'
    scene.save(f"{save_path}/{wp_file_name}")