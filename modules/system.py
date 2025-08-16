import ctypes
import os


def img_as_desktop_wallpaper(img_path):
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


def clear_terminal():
    os.system('cls')