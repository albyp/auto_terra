import logging
import pyautogui as pg
from funcs.utils import pause

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


def modify_parameters(window, auto_accept=False) -> None:
    """
    Modify the oarameters to suit the standard processing workflow.

    Note that these options will select medium quality cloud,
    disable ortho map and change output datum and geoids to second option.

    Args:
        window (object) : A `pygetwindow` Window object representing the DJI Terra application
        auto_accept (boolean) : Allow the user to auto accept the final processing step

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
    start_processing = (-200, 1000)
    final_ok = (-720, 820)

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
    pg.scroll(-5000)
    move_click_pause(window, geoid)
    move_click_pause(window, second_geoid_input)
    move_click_pause(window, start_processing)
    
    if auto_accept:
        move_click_pause(window, final_ok)
        logging.info("Initiated 'Start Processing' sequence.\nI like your style!")