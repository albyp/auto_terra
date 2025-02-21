import pyautogui as pg
import logging
import time

def new_lidar_mission(window) -> None:
    """Create new mission from keyboard shortcut and mouse click"""
    logging.debug("Creating new mission using keyboard shortcut")
    pg.hotkey('ctrl', 'n')

    logging.debug("Calculating LiDAR button position")
    terra_center = (window.topleft[0] + (window.width / 2), window.topleft[1] + (window.height / 2))
    lidar_button = (terra_center[0] + 146, terra_center[1] + 36)

    logging.debug("Moving mouse to LiDAR button")
    pg.moveTo(lidar_button)
    time.sleep(0.1)
    logging.debug("Clicking LiDAR button")
    pg.click()
    time.sleep(0.1)
    return

def name_mission(mission:str) -> None:
    """Clear the default mission name and input the given parameter."""
    logging.debug("Clearing mission name")
    pg.hotket('ctrl', 'a')
    time.sleep(0.1)
    pg.press('backspace')
    logging.debug(f"Inputting mission name: '{mission}'.")
    pg.write(mission)
    return

def input_mission_data(data_dir:str) -> None:
    """Paste the input mission data directory for processing.
    Parameters
    data_dir (str) : Directory for LiDAR data
    """
    logging.debug("Inputting mission data to DJI Terra.")
    pg.write(data_dir)
    time.sleep(0.1)
    pg.press('enter')
    time.sleep(0.1)
    pg.press('enter')
    logging.info('Finishing inputting LiDAR data to DJI Terra')
    return
