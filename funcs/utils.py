import time
import pyautogui as pg
import keyboard
from pynput import mouse
import logging
from funcs.state import stop_script
import os

DEBUG_DELAY = 0.2

script_path = os.path.dirname(__file__)

def return_mouse_pos(initial_pos:tuple) -> None:
    """
    Return the mouse to the initial position.

    Args:
        initial_mouse_pos (tuple) : Tuple containing (X, Y) position for the mouse initial position.

    Returns:
        None        
    """
    logging.debug("Returning mouse to the initial position.")
    pg.moveTo(initial_pos)


def pause() -> None:
    """Pause for debugging purposes."""
    time.sleep(DEBUG_DELAY)


def move_rel_top_right(window, offset: tuple[int, int]) -> None:
    """Move mouse relative to top right of window

    Args:
        window (object): A `pygetwindow` Window object representing the DJI Terra applcation
        offset (tuple[int, int]): The x, y offset to move relative from window top right.
    """
    pg.moveTo(window.topright[0] + offset[0], window.topright[1] + offset[1])


def move_click_pause(window, offset: tuple[int, int]) -> None:
    """
    Moves the mouse to position defined by offset (relative to top right),
    Clicks the mouse and then pauses.
    
    Args:
        window (object) : A `pygetwindow` Window object representing the DJI Terra application
        offset (tuple[int, int]) : The x, y offset to move relative from window top right - feeds into move_rel_top_right.

    Returns:
        None
    """
    move_rel_top_right(window, offset)
    pg.click()
    pause()


def check_interrupt() -> None:
    """Continuously checks for interruption (esc key or right-click)."""
    global stop_script
    while not stop_script:
        if stop_script or keyboard.is_pressed("esc"):
            logging.warning("Interrupt detected. Exiting script...")
            stop_script = True
        time.sleep(0.1) # Prevent excessive CPU usage for threaded task


def on_right_click(x, y, button, pressed):
        """Stops script execution on right-click."""
        global stop_script
        if button == mouse.Button.right and pressed:
            logging.warning("Right-click detected. Stopping script...")
            stop_script = True


def processing_confirm() -> bool:
    logging.info("Waiting for confirmation.")
    res = pg.confirm("Click OK to continue processing.", "Auto Terra script")
    if res == "OK":
        logging.info("Processing confirmed.")
        return True
    return False