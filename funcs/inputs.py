import pyautogui as pg
import logging
import time

def new_lidar_mission(window) -> None:
    """Create new mission from keyboard shortcut and mouse click"""
    logging.debug("Creating new mission using keyboard shortcut")
    pg.hotkey('ctrl', 'n')
    pause()

    logging.debug("Calculating LiDAR button position")
    terra_center = (window.topleft[0] + (window.width / 2), window.topleft[1] + (window.height / 2))
    lidar_button = (terra_center[0] + 146, terra_center[1] + 36)

    logging.debug("Moving mouse to LiDAR button")
    pg.moveTo(lidar_button)
    pause()

    logging.debug("Clicking LiDAR button")
    pg.click()
    pause()
    return

def name_mission(mission:str, window) -> None:
    """Clear the default mission name and input the given parameter."""
    logging.debug("Clearing mission name")
    pg.hotkey('ctrl', 'a')
    pause()

    pg.press('backspace')
    pause()

    logging.debug(f"Inputting mission name: '{mission}'.")
    pg.write(mission)
    pg.moveTo(window.topleft[0] + window.width / 2 + 160, window.topleft[1] + window.height / 2 + 70) # Move to OK button
    pause()

    pg.click() # Click OK button
    pause()
    return

def input_mission_data(data_dir:str, window) -> None:
    """Open the folder input, write the mission data directory for processing.
    Parameters
    data_dir (str) : Directory for LiDAR data
    """
    logging.debug("Inputting mission data to DJI Terra.")
    pg.moveTo(window.topright[0] - 170, window.topright[1] + 182)
    pg.click()
    pause()
    
    pg.write(data_dir)
    pause()

    pg.press('enter')
    pause()

    pg.press('tab')
    pg.press('enter')
    logging.info('Finishing inputting LiDAR data to DJI Terra')
    pause()
    return
