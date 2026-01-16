#!/usr/bin/env python3
import sys
import os

from time import sleep
import traceback

from modules.APOD_api import APOD_api
from modules._setup_program import setup_program
from modules.errors_handling import ERROR_REPORT, error_report
from modules.files import dowload_file_from_url
from modules.interface import inform
from modules.program import (get_path, last_img_as_wallpaper, load_api_key,
                             make_name_from_url, new_apod_needed,
                             save_user_data, update_history)

@error_report()
def run_program():
    # Setup in case of first run
    setup_program()

    inform('Checking API key...')
    api_key = load_api_key()

    # If no API key, get one
    if not api_key:
        api_key = get_api_key()
    
    # Getting info about current img out there
    inform('Getting info about current server img...')
    apod = APOD_api(api_key)
    apod_data = apod.get_apod()

    # Check if data type is image
    if apod_data.get('media_type') != 'image':
        inform("Today we have not an image, probably it's a video.\n"
                   "Can't use it, so try the next day!",
                   clear_term=True)
        input()
        return

    # Check if the img is new,
    # compearing dates of last apod and just loaded one
    if not new_apod_needed(apod_data['date']):
        inform('There is no new img yet!',
                   sleep_time=2,
                   clear_term=True
        )
        return
    
    # Download image
    url = apod_data['hdurl']
    inform('Downloading new img...')
    dowload_file_from_url(
        url=url, 
        save_path=get_path('images_store')+f'/{make_name_from_url(url)}'
    )

    # Add apod data to history
    update_history( apod_data['date'], apod_data)

    # Set wallpaper
    inform('Setting wallpaper...')
    last_img_as_wallpaper()

    inform('Done!',
               sleep_time=1,
               clear_term=True
    )


def get_api_key():
    while True:
        api_key = input('Enter your API key: ')
        if APOD_api(api_key).test_connection():
            save_user_data(api_key)
            return api_key
        else:
            print('Invalid API key. Please try again.')
            sleep(2)


if __name__ == '__main__':
    try:
        run_program()
    except Exception as error:
        inform('/!\\ Error occured.',
               clear_term=True)
        
        if ERROR_REPORT['message']:
            inform(f'\n{ERROR_REPORT['message']}')
        
        inform(('\nReport file path: '
                f'{ERROR_REPORT["report path"]}\n\n'
                'Press enter to close program.'))
        
        input()