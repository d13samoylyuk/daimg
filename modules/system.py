import ctypes
import os
from pathlib import Path
import platform
import subprocess


MACHINE_PLATFORM = {
    "OS": platform.system()
}


def img_as_desktop_wallpaper(img_path):
    platform_function = {
        'Linux': _linux_wp_setup,
        'Darwin': _macos_wb_setup,
        'Windows': _windows_wp_setup
    }

    platform = MACHINE_PLATFORM['OS']

    platform_function[platform](img_path)


def _windows_wp_setup(img_path):

    abs_path = os.path.abspath(img_path)
    
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


def _macos_wb_setup(img_path):
    '''
    Sets the desktop wallpaper on macOS using AppleScript
    '''
    full_path = os.path.abspath(img_path)

    script = f'''
    tell application "Finder"
        set desktop picture to POSIX file "{full_path}"
    end tell
    '''
    subprocess.run(["osascript", "-e", script], check=True)


def clear_terminal():
    if MACHINE_PLATFORM['OS'] in ['Linux', 'Darwin']:
        os.system('clear')
    elif MACHINE_PLATFORM['OS'] == 'Windows':
        os.system('cls')