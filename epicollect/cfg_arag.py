# Avonvale River Action Group
# ===========================

INPUT_CSV_FILENAME = 'form-1__wqmn-water-quality-survey.csv'
OUTPUT_FOLDER = "arag"

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
COL_CSO = None
COL_CONDUCTIVITY = 19
COL_TEMPERATURE = 20
COL_NITRATES = 22
COL_PHOSPHATES = 21
COL_RIVER_HEIGHT = 15
COL_NOTES = 26
COL_RIVER_FLOW = 16
COL_WEATHER = 17
COL_RECENT_RAIN = 18
COL_AMMONIA = 23
COL_ALGAL_BLOOMS = 24
COL_POLLUTION = 25

# River names we are monitoring, case insensitive, we use the first one
RIVER_NAMES = [ ("Warwickshire Avon", "warwickshire avon fladbury", "warwickshire river avon", "warks avon", "River Avon Worcs", "Warwickshire  Avon"),
                ("Warwickshire Arrow", "Arrow", "Warks Arrow"),
                ("Alne", "River Alne"),
                ("Isbourne","Isbourne"),
                ("Badsey Brook","Badsey Brook"),
                ("Elmley Brook","Elmley Brook","River Avon tributary brook")
              ]

# We map some names for consitency, include the location number if there is one (will be then stripped out)
# Names get changed to the first one in the list
SYNONYMS = [ ("220 Fladbury, Jubilee Bridge", "fladbury, Jubilee Bridge"),
             ("220 Fladbury, Jubilee Bridge", "Jubilee Bridge Fladbury"),
             ("220 Fladbury, Jubilee Bridge", "Jubilee Bridge"),
             ("270 Pershore, Leisure Centre", "Leisure Centre Pershore", "Pershore Leisure Centre", "Pershore les cent 270", "Pershore Leisure Centre 270"),
             ("230 Charlton, Merry Brook", "230merry brook"),
             ("120 Offenham, Dead Mens Ait", "120a offenham Dead Mens Ait (opp)"),
             ("100 Wootten Warwen", "Pennyford Lane Bridge", "Pennyford Bridge lane", "Pennyford Lane (BAA WATER)", "Pennyford bridge"),
             ("Lido Stratford upon Avon", "Lido"),
             ("120 Spernal Lane", "Spernall Lane Bridge", "Spernal Lane Bridge", "spernall", "spernal lane"),
             ("Cleeve Prior", "103 Cleeve Prior"),
             ("240 Cropthorne, Holland House", "Holland House", "Holland House site 240"),
             ("25 Hinton, Bridge","25 Hinton, bridge"),
             ("30 Hampton, Bridge","30 Hampton, bridge"),
             ("108 B4510 Bridge", "200 B4510 bridge"),
             ("245 Cropthorne Main Street, Bridge", "245 Cropthorne Main Street Bridge"),
             ("280 Pershore, Bridges", "Pershore bridges"),
             ("Rugby, Steam Turbine", "Rugby; Steam Turbine", "Rugby (Steam Turbine)"),
             ("Barford Below","Barford B"),
             ("Barford Above","Barford A")
           ]

# Locations which have a number
# If we find a number in the place name in spreadsheet, then try to look up that number for the river in this list first
# Place name in table below must be the same as SYNONYMS above but without the number
SAMPLING_LOCATIONS = [
    ("Isbourne", 25, "Hinton, Bridge", 52.063505, -1.967044),
    ("Isbourne", 30, "Hampton, Bridge", 52.085601, -1.956927),
    ("Warwickshire Avon", 50, "B4510 bridge", 52.104597, -1.916057),
    ("Warwickshire Avon", 100, "Bidford Bridge", 52.163627, -1.856484),
    ("Badsey Brook", 108, "B4510 Bridge", 52.091779, -1.907077),
    ("Elmley Brook", 245, "Cropthorne Main Street, Bridge", 52.100479, -2.007295),
    ("Warwickshire Avon", 115, "Twyford ANT landing", 52.117573, -1.930736),
    ("Warwickshire Avon", 120, "Offenham, Dead Mens Ait", 52.109891, -1.929374),
    ("Warwickshire Avon", 130, "Evesham, de Montfort bridge", 52.105462, -1.929985),
    ("Warwickshire Avon", 140, "Evesham, slip above weir", 52.094453, -1.939439),
    ("Warwickshire Avon", 150, "Evesham, Waterside/Abbey Moorings", 52.09077, -1.94410),
    ("Warwickshire Avon", 160, "Evesham, Battleton Brook", 52.08820, -1.94588),
    ("Warwickshire Avon", 165, "Evesham Corporation Meadow", 52.086446, -1.956054),
    ("Warwickshire Avon", 170, "Evesham Hampton Ferry", 52.09155, -1.95809),
    ("Warwickshire Avon", 175, "Evesham, Blind Lane", 52.09547, -1.95607),
    ("Warwickshire Avon", 180, "Evesham, Worcester Rd ATS", 52.102447, -1.953149),
    ("Warwickshire Avon", 190, "Chadbury, Lock", 52.112619, -1.964094),
    ("Warwickshire Avon", 200, "Chadbury, Wood Norton", 52.120157, -1.983626),
    ("Warwickshire Avon", 210, "Fladbury, Paddle Club", 52.118181, -2.006461),
    ("Warwickshire Avon", 220, "Fladbury, Jubilee Bridge", 52.108816, -2.000528),
    ("Warwickshire Avon", 230, "Charlton, Merry Brook", 52.10853, -1.98801),
    ("Warwickshire Avon", 240, "Cropthorne, Holland House", 52.102836, -2.006356),
    ("Warwickshire Avon", 245, "Cropthorne Main Street Bridge", 52.100434, -2.007293),
    ("Warwickshire Avon", 250, "Cropthorne, below pump house", 52.103992, -2.020204),
    ("Warwickshire Avon", 255, "Cropthorne strawberry farm", 52.105278, -2.029053),
    ("Warwickshire Avon", 260, "Lower Moor, below STW", 52.124358, -2.048519),
    ("Warwickshire Avon", 261, "Wyre Piddle Anchor", 52.125235, -2.051679),
    ("Warwickshire Avon", 265, "Wyre Piddle", 52.12369, -2.05767),
    ("Warwickshire Avon", 270, "Pershore, Leisure Centre", 52.112278, -2.071453),
    ("Warwickshire Avon", 205, "Pershore, Bridges", 52.10525, -2.07059),
    ("Warwickshire Avon", 280, "Pershore, Bridges", 52.10525, -2.07059),
    ("Warwickshire Avon", 290, "Pensham", 52.10042, -2.088309),
    ("Warwickshire Avon", 300, "Eckington, Bridge", 52.078815, -2.11487),
    ("Warwickshire Avon", 305, "Mary Brook", 52.096218, -2.049696),
    ("Warwickshire Avon", 310, "Defford, Arden Sailing Club", 52.079476, -2.127854),
    ("Warwickshire Arrow", 100, "Studley", 52.27419029342931, -1.883789898760419),
    ("Warwickshire Arrow", 120, "Spernal Lane", 52.26057296331432, -1.8762366844985907),
    ("Warwickshire Arrow", 200, "Salford Bridge", 52.16338142682303, -1.8803195030184976),
    ("Alne", 100, "Wootten Warwen (=Pennyford Lane Bridge)", 52.2581988721852, -1.783556704096704),
    ("Alne", 130, "Little Alne", 52.250200998557055, -1.7935596094704758),
    ("Alne", 150, "Great Alne (Pelham Lane)", 52.23257559455438, -1.8317339626316056),
    ("Warwickshire Avon", 0, "Barford Below", 52.245253, -1.617944),
    ("Warwickshire Avon", 0, "Barford Above", 52.256291, -1.597904)
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