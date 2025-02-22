import logging
import pyautogui as pg
import time

def select_base_settings(window) -> None:
    """Opens the Base Station settings menu."""
    logging.debug("Opening base station settings menu.")
    # Offset from top right
    base_settings = (-30, 221)
    x = window.topright[0] + base_settings[0]
    y = window.topright[1] + base_settings[1]
    pg.moveTo(x, y)
    pg.click()
    return

def change_coordinate_system(epsg, window) -> None:
    """Open the coordinate system menu and change the system to given epsg code.
    Parameters
    epsg (str) : EPSG code for base coordinate system.
    window (object) : pygetwindow object
    """
    logging.debug("Opening coordinate sytem modifier")
    # Offset from center
    epsg_search = (-229, -85)
    center_x = window.topleft[0] + window.width / 2
    center_y = window.topleft[1] + window.height / 2
    x = center_x + epsg_search[0]
    y = center_y + epsg_search[1]
    pg.moveTo(x, y)
    pg.click()
    logging.info("Inputting EPSG code.")
    pg.moveTo(center_x + 0, center_y - 60) # Move to search input
    pg.click()
    pg.write(epsg)
    logging.debug("Selecting EPSG.")
    pg.moveRel(0, 107) # Move to the found EPSG
    pg.click()
    logging.debug("Move to OK button.")
    pg.moveTo(center_x + 200, center_y + 108) # Move to the OK button
    pg.click()
    logging.debug("Finished inputting EPSG.")
    return

def input_coordinates(coordinates:dict, window):
    """Input base station coordinates from dictionary.
    
    Parameters:
    coordinates (dict) : x, y, z values for base coordinate
    window (object) : pygetwindow object
    """
    logging.info("Inputting base coordinates.")
    center_x = window.topleft[0] + window.width / 2
    center_y = window.topleft[1] + window.height / 2
    # X Input
    pg.moveTo(center_x - 388, center_y - 6)
    pg.click()
    pg.write(coordinates['x'])
    # Y Input
    pg.moveRel(180, 0)
    pg.click()
    pg.write(coordinates['y'])
    # Z Input
    pg.moveRel(180, 0)
    pg.click()
    pg.write(coordinates['z'])
    # Batch edit button
    pg.moveTo(center_x + 80, center_y - 10)    
    pg.click()
    pg.moveTo(center_x + 420, center_y + 175)
    pg.click()
    logging.debug("Finished inputting base coordinates.")
    return