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

# Depreciated, use `MISSIONS` list instead
MISSION_NAME = "YYMMDD-ProjectName_LiDAR"
MISSION_DATA_DIR = "C:\\Pix4D\\YYMMDD-ProjectName\\1. LiDAR"