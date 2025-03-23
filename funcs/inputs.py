import pyautogui as pg
import logging
from funcs.utils import pause, move_click_pause
import time

def new_lidar_mission(window) -> None:
    """
    Create new mission in DJI Terra.

    This function triggers the 'New Mission' shortcut and selects the 'LiDAR Mission' type by selecting the button.

    Args:
        window (object) : A `pygetwindow` Window object representing the DJI Terra application

    Returns:
        None
    """
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


def name_mission(mission:str, window) -> None:
    """
    Write mission name to DJI Terra project.

    This function writes the given mission name to the DJI Terra project.

    Args:
        mission (str) : String to input to DJI Terra
        window (object) : A `pygetwindow` Window object representing the DJI Terra application
    
    Returns:
        None
    """
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


def input_mission_data(data_dir:str, window) -> None:
    """
    Input the directory for LiDAR data to be loaded from
    
    Open the folder input manu, input the data_dir string and accept the prompts.

    Args:
        data_dir (str) : String of the directory where LiDAR data is stored
        window (object) : A `pygetwindow` Window object representing the DJI Terra application

    Returns:
        None
    """
    logging.debug("Inputting mission data to DJI Terra.")
    time.sleep(1)
    pg.moveTo(window.topright[0] - 170, window.topright[1] + 182)
    pg.click()
    pause()
    time.sleep(0.1)
    
    pg.write(data_dir)
    pause()
    time.sleep(0.1)

    pg.press('enter')
    pause()

    pg.press('tab')
    pg.press('enter')
    # TODO Add extended wait if large datasets are being imported (shows loading bar)
    # TODO Implement locateOnScreen to check for 'Tip - Missing certain data in the imported files'
    logging.info('Finishing inputting LiDAR data to DJI Terra')
    pause()


def start_processing() -> None:
    """
    Modify the oarameters to suit the standard processing workflow.

    Note that these options will select medium quality cloud,
    disable ortho map and change output datum and geoids to second option.
    """
    logging.info("Start processing.")
    # move_click_pause(window, start_processing)
    pg.moveTo(pg.locateOnScreen('funcs/start_processing.png', confidence=0.8))
    pg.click()


def ok_processing(window) -> None:
    pg.moveTo(pg.locateOnScreen('funcs/ok_processing.png', confidence=0.8))
    pg.click()
    logging.info("Initiated 'Start Processing' sequence.")
    # Move to home button and click to expand
    pg.moveTo(window.topleft[0] + 40, window.topleft[1] + 45)
    pg.click()