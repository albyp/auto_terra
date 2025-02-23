import time
import pyautogui as pg

DEBUG_DELAY = 0.2

def pause() -> None:
    """Pause for debugging purposes."""
    time.sleep(DEBUG_DELAY)


def move_rel_top_right(window, offset: tuple[int, int]) -> None:
    # pg.moveTo(window.topright[0] + offset[0] - 9, window.topright[1] + offset[1] - 8) # bullshit mod for extra monitors
    pg.moveTo(window.topright[0] + offset[0], window.topright[1] + offset[1])


def move_click_pause(window, offset: tuple[int, int]) -> None:
    """
    Moves the mouse to position defined by offset (relative to top right),
    Clicks the mouse and then pauses.
    
    Args:
        window (object) : A `pygetwindow` Window object representing the DJI Terra application
        offset (tuple[int, int]) : The x, y offset to move relative from window top right.

    Returns:
        None
    """
    move_rel_top_right(window, offset)
    pg.click()
    pause()