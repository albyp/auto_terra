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