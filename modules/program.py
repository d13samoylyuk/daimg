import os

from PIL import ImageFont
from dotenv import load_dotenv
from modules.basic import define_id
from modules.files import (add_csv_line, check_file_exists,
                          create_env_file, read_csv_file, read_json_file)
from modules.system import img_as_desktop_wallpaper
from modules.times import compare_time, str_to_time, time_now


def get_path(file):
    return read_json_file('data/rule_paths.json')[file]



def load_api_key():
    # Check if .env file exists
    if not check_file_exists(get_path('env')):
        return None
    
    load_dotenv(dotenv_path=get_path('env'))
    return os.getenv('API_KEY')
    

def save_user_data(key: str):
    template =f'API_KEY={key}'
    create_env_file(get_path('env'), template)


def last_record():
    history = read_csv_file(get_path('history'))
    if not history:
        return None
    last_line = history[-1]

    return last_line


def last_apod_date():
    last_line = last_record()
    if not last_line:
        return None
    
    return str_to_time(last_line['date'])


def new_apod_needed(new_apod_date):
    last_apod = last_apod_date()
    if not last_apod:
        return True

    return compare_time(last_apod, str_to_time(new_apod_date))


def make_id():
    last_line = last_record()
    id_num = 1
    if last_line:
        id_num += int(last_line['id'])
    
    return define_id(id_num, prefix='', max_id_lenth=0)


def update_history(apod_date, apod_data):
    data_line = [make_id(),                              # id
                 make_name_from_url(apod_data['hdurl']), # file_name
                 apod_date,                              # date
                 apod_data['explanation']                # description
                 ]
    add_csv_line(get_path('history'), data_line)


def make_name_from_url(url, get_suffix=True):
    if get_suffix:
        suffix = make_id()
        splited = url.split('/')[-1].split('.')
        return f'{splited[0]}_{suffix}.{splited[1]}'
    
    return url.split('/')[-1]


def last_img_as_wallpaper():
    img_name = last_record()['file_name']
    last_img_path = get_path('images_store') + f'/{img_name}'

    return img_as_desktop_wallpaper(last_img_path)


def load_font(font_path: str = 'font_default',
              font_size: int = 20):
    try:
        if font_path == 'font_default':
            font_path = get_path(font_path)
        return ImageFont.truetype(font=font_path,
                                  size=font_size)
    except IOError:
        print("Font file not found, using default font.")
        return ImageFont.load_default(size=font_size)