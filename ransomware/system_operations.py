import ctypes
import os
from pathlib import Path

def set_wallpaper(image_path):
    """
    Set the system wallpaper to the specified image.

    Args:
        image_path (Path): The path to the image file.
    """
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(image_path), 3)

def get_system32_path():
    """
    Get the path to the System32 directory.

    Returns:
        str: The path to the System32 directory.
    """
    windows_dir = os.environ.get('SystemRoot')
    return os.path.join(windows_dir, 'System32')
