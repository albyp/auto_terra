import logging
import pyautogui as pg

# Import window functions
from funcs.window import get_terra_window, focus_terra
from funcs.inputs import new_lidar_mission, name_mission, input_mission_data
from funcs.base_settings import select_base_settings, change_coordinate_system, input_coordinates

# Set logging level
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Defaults for testing
from config import MISSION_NAME, MISSION_DATA_DIR, EPSG, BASE_COORDINATES
PROCESS_BASE = True

def get_initial_mouse_pos() -> tuple:
    """
    Get the initial mouse position before running script.

    Returns:
        pos (tuple) : Initial mouse position
    """
    logging.debug("Recording the intial mouse position.")
    pos = pg.position()
    return pos


def return_mouse_pos(inital_mouse_pos:tuple) -> None:
    """
    Return the mouse to the intial position.

    Args:
        initial_mouse_pos (tuple) : Tuple containing (X, Y) position for the mouse intial position.

    Returns:
        None    
    """
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
    name_mission(MISSION_NAME, window)

    # Import LiDAR data to project
    input_mission_data(MISSION_DATA_DIR, window)
    
    # Process base settings
    if PROCESS_BASE:
        logging.info("Executing process base functions...")
        select_base_settings(window)
        change_coordinate_system(EPSG, window)
        input_coordinates(BASE_COORDINATES, window)

    return_mouse_pos(initial_mouse_pos)
    return


# Run program
if __name__ == '__main__':
    main()