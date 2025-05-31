import logging
import pyautogui as pg
from funcs.utils import move_click_pause, pause

def modify_parameters(window) -> None:
    """
    Modify the parameters to suit the standard processing workflow.

    Note that these options will select medium quality cloud,
    disable ortho map and change output datum and geoids to second option.

    Args:
        window (object) : A `pygetwindow` Window object representing the DJI Terra application

    Returns:
        None
    """
    # Coordinates list
    parameters_toggle = (-292, 262)
    cloud_toggle = (-292, 375)
    by_percentage_toggle = (-283, 599)
    merge_clouds = (-52, 525)
    density_dropdown = (-200, 634)
    density_medium = (-200, 686)
    ortho_toggle = (-30, 418)
    advanced_toggle = (-200, 617)
    horiz_datum = (-200, 825)
    second_datum_input = (-200, 907)
    geoid = (-200, 602)
    second_geoid_input = (-200, 723)

    logging.info("Modifying process parameters.")
    logging.debug("Opening parameters toggle menu.")
    move_click_pause(window, parameters_toggle)

    # Modify cloud settings
    logging.debug("Changing point cloud settings.")
    move_click_pause(window, cloud_toggle)
    move_click_pause(window, by_percentage_toggle)
    move_click_pause(window, merge_clouds)
    move_click_pause(window, density_dropdown)
    move_click_pause(window, density_medium)
    logging.debug("Collapsing cloud toggle.")
    move_click_pause(window, cloud_toggle)

    # Disabling 2d map (ortho)
    logging.debug("Disabling 2D map (ortho).")
    move_click_pause(window, ortho_toggle)

    # Toggle advanced tab and adjust datum and geoid
    logging.debug("Changing output datum and geoid.")
    move_click_pause(window, advanced_toggle)
    move_click_pause(window, horiz_datum)
    move_click_pause(window, second_datum_input)
    pg.moveTo(500,500) # Janky solution to move mouse away for the locateOnScreen to find the correct button
    # pg.scroll(-5000)
    # move_click_pause(window, geoid)
    logging.debug("Finding geoid input button.")
    pg.moveTo(pg.locateOnScreen('funcs/param_geoid_default.png', 3))
    pause()
    pg.click()
    pause()
    # move_click_pause(window, second_geoid_input)
    logging.debug("Changing geoid to second option.")
    pg.moveRel(0, 117)
    pause()
    pg.click()