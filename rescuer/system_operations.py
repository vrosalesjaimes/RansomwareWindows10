import ctypes

def restore_wallpaper(image_path):
    """
    Restore the system wallpaper to the specified image.

    Args:
        image_path (Path): The path to the image file.
    """
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(image_path), 3)
