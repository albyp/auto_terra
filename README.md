# DJI Terra LiDAR Processing (Auto_Terra)

# Overview

This Python script automates the LiDAR processing workflow in DJI Terra using `pyautogui` for UI interaction. It facilitates mission creation, data input, and parameter modification with minimal config setup and user interaction.

# Features

- Detects and focuses the DJI Terra application
- Creates a new LiDAR mission and names it
- Inputs mission data from specified directory
- Configures the base settings, including coordinate system and base station coordinates
- Modifies processing parameters for standard workflows
- Automates clicking and UI navigation to streamline operations
- Returns the mouse to its initial position after execution

> **Note**
> The script currently takes approximately 20 seconds per mission to execute, including user input to accept processing prompt.

# Installation

## Prerequisites

Ensure you have Python installed (preferably Python 3.9+). Install the required dependencies using:
`pip install -r requirements.txt`

## Dependencies

This script requries the following Python libraries:
- `pyautogui` (for UI automation)
- `pygetwindow` (for window detection and locations)
- `logging` (for debugging and monitoring script execution)
- `pynput` (check for keyboard and mouse inputs for script interruption)

# Usage

1. Update the `config.py` file to suit your needs
2. Open DJI Terra and maximize it on the primary monitor
3. Run the script using:
    `python main.py`
4. The script will automatically perform the following:
    - Detect and focus the DJI Terra window
    - Create a new LiDAR mission
    - Input mission data directory
    - Configure base settings and coordinate systems
    - Modify processing parameters
    - Initiate processing (if `AUTO_ACCEPT = True` in `config.py`)

# Configuration

The script uses a `config.py` file to define default values:
``` python
# Determine whether to auto accept the processing task once inputs are complete
AUTO_ACCEPT = False

# Base coordinate EPSG code
EPSG = "28350"

# Base coordinates (for RTK base used with drone)
BASE_COORDINATES = {
    "x": "420550.295",
    "y": "6302560.234",
    "z": "301.750"
}

# Mission inputs, use single line for single mission
MISSIONS = [
    ['YYMMDD-ProjectName', 'C:\\Pix4D\\YYMMDD-ProjectName\\1. LiDAR'],
    ['YYMMDD-ProjectName2', 'C:\\Pix4D\\YYMMDD-ProjectName2\\1. LiDAR']
]
```
Modify these values as needed to suit your project requirements.
There is an `example.config.py` containing the boilerplate for the config. Update this as required and rename to `config.py`.

# Notes

- The script assumes a consistent UI layout in DJI Terra; UI changes in software updates may require adjustments.
- Run the script when DJI Terra is maximized and on the primary monitor to ensure `pyautogui` `locateOnScreen()` function works as expected.
- The Horizontal Datum and Geoid settings currently select the 2nd option from the list.
- Logs will be generated for debugging and process tracking.

# Future Enhancements

> **Note**
> - 🟢 indicates the feature is currently in development
> - 🔵 indicates the feature is being planned

- 🟢 Change `moveTo(x, y)` functions to `moveTo(pyautogui.locateOnScreen())` functions
- 🔵 Add exception handling for UI changes or unexpected errors
- [ ] Develop a GUI for easier configuration
- [ ] Add full control over Horizontal Datum and Geoid selection for output
- [ ] Auto rename the output point cloud and option to move to specific destination

# Known Issues

- Cancel button on `processing_confirm` still results in 'OK'
- When not running in Maximised state, error occurs at base coordinate functions

# License

This project is licensed under the MIT License.

# Author

Alby Palmer - 2025