import logging

# Select panel button
def select_panel_button(window_x, window_y, window_width, window_height, trans_x, trans_y) -> None:
    """Takes the window top left coordinates to calculate a button, moves to and clicks button.
    Parameters:
    window_x (int): The top right x coordinate
    window_y (int): The top right y coordinate
    """
    logging.debug("Calculating the coordinates for 'Select Folder' button")

    x = window_x + window_width + trans_x
    y = window_y + window_height + trans_y
    select_folder = (-159, +180)