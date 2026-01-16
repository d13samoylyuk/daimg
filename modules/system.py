import ctypes
import os
from pathlib import Path
import platform
import subprocess

from test import screen_info


MACHINE_PLATFORM = {
    "OS": platform.system(),
    "display": screen_info()
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