# Avonvale River Action Group
# ===========================

INPUT_CSV_FILENAME = 'form-1__wqmn-water-quality-survey.csv'
OUTPUT_FOLDER = "wensum"

COL_NAME = 4
COL_DATE = 5
COL_RIVER = 6
COL_PLACE = 7
COL_LAT = 8
COL_LONG = 9
COL_ACCURACY = 10
COL_NORTHING = 11
COL_EASTING = 12
COL_UTMZONE = 13
COL_DESCRIPTION = None
COL_TIME = 14
COL_RIVER_HEIGHT = 15
COL_RIVER_FLOW = 16
COL_WEATHER = 17
COL_RECENT_RAIN = 18
COL_CSO = None
COL_CONDUCTIVITY = 19
COL_TEMPERATURE = 20
COL_PHOSPHATES = 21
COL_NITRATES = 23
COL_AMMONIA = 24
COL_ALGAL_BLOOMS = 25
COL_POLLUTION = 26
COL_NOTES = 29

# River names we are monitoring, case insensitive, we use the first one
RIVER_NAMES = [ ("Wensum", "Wensum")
              ]

# We map some names for consitency, include the location number if there is one (will be then stripped out)
# Names get changed to the first one in the list
SYNONYMS = [ 

           ]

# Locations which have a number
# If we find a number in the place name in spreadsheet, then try to look up that number for the river in this list first
# Place name in table below must be the same as SYNONYMS above but without the number
SAMPLING_LOCATIONS = [
]

# Thresholds for graphs
THRESHOLD_CONDUCTIVITY = 1000
THRESHOLD_PHOSPHATES = 0.306
THRESHOLD_NITRATES = 5
THRESHOLD_AMMONIA = 0.6

# Maximums for graphs
MAX_CONDUCTIVITY = 3000
MAX_TEMPERATURE_C = 30
MAX_PHOSPHATES = 2
MAX_NITRATES = 20


# OUTPUT CONFIGURATION
######################

# Graph configuration
FIG_SIZE_X_INCHES = 1
FIG_SIZE_Y_INCHES = 0.75

# ...positions as fraction of figure size
MARGIN_TOP_FRACTION = 0.995
MARGIN_BOTTOM_FRACTION = 0.11
MARGIN_LEFT_FRACTION = 0.08
MARGIN_RIGHT_FRACTION = (1 - MARGIN_LEFT_FRACTION)

YAXIS_LABEL_SPACING = 0.5
TICK_LABEL_SPACING = 0.5
SPACE_BETWEEN_SUBPLOTS = 0.1

BAR_WIDTH = 10