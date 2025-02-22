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

# Installation

## Prerequisites

Ensure you have Python installed (preferably Python 3.9+). Install the required dependencies using:
`pip install -r requirements.txt`

## Dependencies

This script requries the following Python libraries:
- `pyautogui` (for UI automation)
- `pygetwindow` (for window detection and locations)
- `logging` (for debugging and monitoring script execution)

# Usage

1. Open DJI Terra and maximise it on a monitor to ensure best compatability.
2. Run the script using:
    `python main.py`
3. The script will automatically perform the following:
    - Detect and focus the DJI Terra window
    - Create a new LiDAR mission
    - Input mission data directory
    - Configure base settings and coordinate systems
    - Modify processing parameters
    - Initiate processing (if `auto_accept=True` in `modify_parameters`)

# Configuration

The script uses a `config.py` file to define default values:
``` python
MISSION_NAME = "YYMMDD-ProjectName_LiDAR"
MISSION_DATA_DIR = "C:\\Pix4D\\YYMMDD-ProjectName\\1. LiDAR"
EPSG = "28350" # EPSG code for coordinate system
BASE_COORDINATES = {
    "x": "420550.295",
    "y": "6302560.234",
    "z": "301.750"
}
```
Modify these values as needed to suit your project requirements.

# Notes

- The script assumes a consistent UI layout in DJI Terra; UI changes in software updates may require adjustments.
- Run the script in an environment where screen resolution and scaling match the expected layout.
- Logs will be generated for debugging and process tracking.

# Future Enhancements

- Add exception handling for UI changes or unexpected errors
- Develop a GUI for easier configuration

# License

This project is licensed under the MIT License.

# Author

Alby Palmer - 2025