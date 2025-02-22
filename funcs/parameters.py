import logging
import pyautogui as pg
from funcs.utils import pause

"""
NOTES

All from top right

"""

def modify_parameters(window) -> None:
    """
    Modify the oarameters to suit the standard processing workflow.

    Note that these options will select medium quality cloud,
    disable ortho map and change output datum and geoids to second option.
    """

parameters_toggle = (-292, 262)
cloud_toggle = (-292, 278)
by_percentage_toggle = (-283, 599)
density_dropdown = (-200, 634)
merge_clouds = (-52, 525)
density_medium = (-200, 686)
# reclick "cloud toggle"
# disable 2D map
ortho_toggle = (-30, 418)
advanced_toggle = (-200, 617)
horiz_datum = (-200, 825)
second_datum_input = (-200, 907)
# scroll to bottom (page down)
geoid = (-200, 602)
second_geoid_input = (-200, 723)
start_processing = (-200, 1000)