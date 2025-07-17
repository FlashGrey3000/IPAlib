import os

def display_on_linux(img_path: str):            # I am using this because I have some trouble due to wayland. You can just use cv2.imshow() if you would prefer
    """Display a file on linux systems
    """
    os.system(f"xdg-open {img_path}")