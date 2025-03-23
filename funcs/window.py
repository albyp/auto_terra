import pygetwindow as gw
import logging
import time

def get_terra_window() -> object:
    """Find DJI Terra window and return its position and size."""
    logging.debug("Checking for DJI Terra window")
    for window in gw.getWindowsWithTitle("DJI Terra"):
        if "DJI Terra" in window.title:
            logging.debug("Found DJI Terra window, returning object.")
            return window
        logging.error("Failed to find DJI Terra window, not running.")
        return None
    
def focus_terra(window) -> None:
    """Focus the DJI Terra window."""
    logging.debug("Focusing DJI Terra window.")
    window.activate()
    time.sleep(0.5)