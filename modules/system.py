import ctypes
import os
from pathlib import Path
import platform
import subprocess

import tkinter

from modules.basic import two_number_ratio


MACHINE_PLATFORM = {
    "OS": platform.system()
}


def img_as_desktop_wallpaper(img_path):
    platform = MACHINE_PLATFORM['OS']

    if platform == 'Windows':
        abs_path = os.path.abspath(img_path)
        _windows_wp_setup(abs_path)

    elif platform == 'Linux':
        _linux_wp_setup(img_path=img_path)


def _windows_wp_setup(abs_path):
    
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    success =  ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        abs_path,
        SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
    
    if not success:
        error_code = ctypes.windll.kernel32.GetLastError()
        raise RuntimeError(error_code)


def _linux_wp_setup(img_path):
    '''
    ! GNOME desktop environment ! \\
    other desktop environments are not supported yet
    '''

    uri = Path(img_path).resolve().as_uri()
    
    subprocess.run([
        "gsettings",
        "set",
        "org.gnome.desktop.background",
        "picture-uri", 
        uri])
    
    subprocess.run([
        "gsettings",
        "set",
        "org.gnome.desktop.background",
        "picture-uri-dark", 
        uri])


def clear_terminal():
    if MACHINE_PLATFORM['OS'] == 'Linux':
        os.system('clear')
    elif MACHINE_PLATFORM['OS'] == 'Windows':
        os.system('cls')


def get_screen_info() -> tuple[int, int, tuple[int, int]]:
    '''returns screen width, height and aspect ratio as a tuple'''

    root = tkinter.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    return {
        'width': screen_width,
        'height': screen_height,
        'ratio': two_number_ratio(screen_width, screen_height)
    }