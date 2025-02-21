import logging
import pyautogui as pg

# Import window functions
from funcs.window import get_terra_window, focus_terra
from funcs.inputs import new_lidar_mission
from funcs.selectors import select_panel_button

# Set logging level
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def get_initial_mouse_pos() -> tuple:
    """Get the initial mouse position before running script.
    Return (tuple) : Initial mouse position"""
    logging.debug("Recording the intial mouse position.")
    pos = pg.position()
    return pos

def return_mouse_pos(inital_mouse_pos) -> None:
    """Return the mouse to the intial position."""
    logging.debug("Returning mouse to the initial position.")
    pg.moveTo(inital_mouse_pos)
    return

def main() -> None:
    initial_mouse_pos = get_initial_mouse_pos()


    # Check for Terra and focus application
    window = get_terra_window()
    focus_terra(window)

    # Create new mission and set up for import
    new_lidar_mission(window)

    return_mouse_pos(initial_mouse_pos)
    pass

# Run program
if __name__ == '__main__':
    main()