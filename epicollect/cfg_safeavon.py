# SafeAvon sampling results
# ========================

INPUT_CSV_FILENAME = 'form-1__data-entry.csv'
OUTPUT_FOLDER = "safeavon"

COL_RIVER = None
COL_NAME = 14
COL_DATE = 13
COL_PLACE = 4
COL_LAT = 5
COL_LONG = 6
COL_ACCURACY = 7
COL_NORTHING = 8
COL_EASTING = 9
COL_UTMZONE = 10
COL_DESCRIPTION = 11
COL_TIME = 12
COL_CSO = 15
COL_CONDUCTIVITY = 16
COL_TEMPERATURE = 17
COL_NITRATES = 18
COL_PHOSPHATES = 19
COL_RIVER_HEIGHT = 20
COL_NOTES = 21
COL_RIVER_FLOW = None
COL_WEATHER = None
COL_RECENT_RAIN = None
COL_AMMONIA = None
COL_ALGAL_BLOOMS = None
COL_POLLUTION = None

# We map titles which start with the terms on the right of each entry to the list to
# the name on the left (case insensitive)
SYNONYMS = [
("Abbey Mill", "Abbey Mill"),
("After sewage works", "After sewage works"),
("After ST outflow", "After ST outflow"),
("Alveston Swiffen Bank", "Alveston Swiffen Bank"),
("Alveston Weir", "Alveston Weir"),
("Avon Smith's Meadow", "Avon Smiths Meadow", "AvonSmithsMeadow", "AvonSmith'sMeadow", "Avon  Smiths Meadow", "Avon Smith Meadow","Avon  Smith's Meadow", "AvonMeadow", "Avon meadow"),
("Barton","Barton"),
("Bell Brook","Bell Brook"),
("Black Bear","Black Bear"),
("Black Bear","Black Bear"),
("Brailes main road","Brailes main road"),
("Bredon Marina","Bredon Marina","Dock Lane Bredon","Dock Lane.Bredon", "Dock lane. Bredon", "Bredon docklane"),
("Cam, Chimping Campden Craves", "Cam Chipping Campden Craves", "Cam Chipping Campden", "Chipping Campden Craves", "Craves Chipping Campden"),
("Carrant Brook, Bredon Road", "Carrant Bredon Rd", "Carrant Bredon Road", "Carrant. Bredon Road", "Carrant. Bredon Rd"),
("Carrant Brook, Back", "Carrant Brook Back", "Carrant Brook Back Lane"),
("Carrant Brook Beckford", "Carrant Brook Beckford Back Lane"),
("Carrant Brook, M5 Bridge", "Carrant Brook M5", "Carrant Brook M5 Bridge", "Carrant M5 Bridge"),
("Carrant Brook, Mitton Bridge", "Carrant Mitton Bridge", "Carrant Mitton Path", "Mitton path", "Mitton parh"),
("Carrant Brook, Bredon Road", "Carrant Brook Bredon Rd"),
("Carrant Brook, Crashmore Lane", "Carrant crashmore lane"),
("Carters Lane", "Carters Lane", "Carter Lane"),
("Clifford Chambers Mill Bridge", "Clifford Mill Bridge", "Clifford Chambers", "Clifford Chambers mill bridge", "Clifford mill bridge", "Clifford  mill bridge"),
("Fosseway Brook, Cross Leys", "Cross Leys", "CrossLeys", "Fosseway Brook, Cross Leys", "Fosseway Brook; Cross Leys", "Fosseway Brook: Cross Leys"),
("Stour, Fell Mill Footbridge", "Fell Mill Footbridge", "Fell Mill River Bridge", "Fell Mill Lane Footbridge"),
("Fladbury Paddle Club", "Fladbury Paddle Club"),
("Ford Langley", "Ford Langley"),
("Fosseway Brook", "Fosseway Brook, Middle Street", "Fosseway Brook; Middle Street", "Fosseway Brook: Middle Street", "Fosseway Brook: Middle St"),
("Fosseway Brook", "Fosseway Brook, Severn Trent Outflow", "Fosseway Brook, ST Outflow", "Fosseway Brook: ST Outflow"),
("Great Comberton Quay", "Great Comberton Quay", "Quay Lane Great Comberton"),
("Hampton Lucy", "Hampton Lucy"),
("Hampton Wood", "Hampton Wood"),
("Heath Culvert", "Heath Culvert Ilmington"),
("Heath Gate", "Hath Gate"),
("High Street Brailes", "High St Brailes", "High street", "High Street Brailes", "High Street,Brailes", "High Street, Lower Brailes"),
("Site 1: Ilmington Middle Street", "Ilmington Middle St", "Illmington middle st","Middle Street","Middle Street Ilmington","MiddleStreet","Site 1 : Middle Street", "Site 1 : Middle Street", "Site 1  :  Middle"),
("Isbourne","Isbourne"),
("Langley Ford","Langley Ford","Langley","The Ford"),
("Lower Lode","Lower Lode", "Lowerl Lode"),
("Lucy's Mill Bridge","Lucy's Mill Bridge"),
("Luddington Avonbank Drive","Luddington Avonbank Drive","Luddington Avon Bank", "Luddington Avon Drive", "Avonbank Drive", "Avonbank"),
("Luddington Pitch","Luddington Pitch"),
("Mill Bridge, Peopleton", "Mill  Bridge, Peopleton", "Mill Bridge Peopleton", "Mill Bridge, Peopleton", "Mill Bridge,Peopleton", "Mill Bridge  Peopleton"),
("Mill Stour, Newbold", "Mill Stour Newbold","Newbold Mill Stour","Stour,Newbold,Mill"),
("New barn", "New barn", "New barn Brailes", "New Barn Farm", "New Barn Farm Brailes", "New Barn Farm,Brailes","NewBarn", "Sutton Brook - New Barn Farm", "Sutton Brook, New Barn Farm", "Sutton Brook,Brailes","New Farm Barn Brailes"),
("Pershore Bridges","Pershore bridges"),
("Pershore leisure centre","Pershore leisure centre"),
("Piddle Brook Long Lane Pinvin","Piddle Brook Long Lane Pinvin"),
("Piddle Brook North of Radford","Piddle Brook North of Radford"),
("Piddle Brook Norton Beachamp Bridge", "Piddle Brook Norton Beachamp Bridge",),
("Piddle Brook Bridge","Piddle Brook Bridge", "Piddle Brook Wyre Piddle Bridge","Piddlebrook bridge", "Piddlebrook WyrePiddleBridge", "PiddleBrook-Wyre Piddle Bridge","PiddleBrookBridge","Piddlebrook Wyre piddle bridge"),
("Pitch 16", "Pitch 15", "Pitch 16", "Pitch16"),
("Preston Bagot Brook","Preston Bagot Brook","Preston  Bagot Brook"),
("Preston Bagot Canal", "Preston Bagot Canal","Preston Bigot Canal"),
("Stour, Preston River Bridge", "Preston River Bridge", "Preston onStour River Bridge","Preston- on- stour river bridge", "Preston- on- stour"),
("Stowe, Lower Fields Farm", "R.Stowe - Lower Fields Farm", "R.Stowe, Lower Fields Farm","R.Stowe,  Lower Fields Farm, Napton","R.Stowe,  Lower Field's Farm, Napton"),
("Stowe, New Zealand Spinney", "R. Stowe,New Zealand Spinney","R.Stowe, New Zealand Spinney, Stockton","R.Stowe, New Zealand Spinney"),
("Stowe, Spring", "R. Stowe,Spring","R.Stowe, Spring by Howcombe Allotments, Napton","R.Stowe, Spring by Howcombe Allotments,Napton"),
("Avon, Quay Lane", "River Avon at Quay Lane"),
("Stour, Cherington", "River Stour Cherington after sewerage works"),
("School Lane", "School Lane"),
("Severn Sailing Club","Severn Sailing Club","Seven sailing club","SSC Bedons Norton","SSC Bredon's Norton","SSC BREDONS NORTON"),
("Severn Trent Outflow", "Severn Trent Outflow"),
("Sherbourne Brook", "Shaerbourne Brook", "Sherborne Brook", "Sherbourne Brook"),
("Shipston - Mill Bridge", "Shipston - Mill Bridge","Shipston mill bridge"),
("Site 2: Cross Leys culvert","Site 2 : Cross Leys Culvert", "Site 2  :  Cross"),
("Site 3: Severn Trent Plant","Site 3 : Severn Trent Water Processing plant outflow", "Site 3  :  Severn"),
("ST Outflow", "ST Outflow"),
("Stour, Ascott village","Stour Ascott village"),
("Stour, Mill Bridge Shipston", "Stour Bridge Shipston", "Stour, Mill Bridge, Shipston", "Stour, Shipston Mill Bridge", "Stour, Shipston, Mill Bridge"),
("Stour, Mill House Newbold", "Stour Mill house Newbold", "Stour, Mill House, Newbold", "Stour, Mill Newbold", "Stour, Newbold, MillHouse", "Stour, Newbold, millstream","Stour, Newbold, Mill"),
("Stour, Shipston Mill Bridge","Stour Shipstn Mill Bridge","Stour Shipston bridge","Stour Shipston Mill Bridge","Stour Shipston Fell Mill Bridge"),
("Stour, Stretton-on-Fosse sewage","Stour Stretton-on-Fosse sewage"),
("Stour, Stretton-on-Fosse village","Stour Stretton-on-Fosse village"),
("Stour, Whichford", "Stour Whichford", "Stout Whichford"),
("Stour, Willington", "Stour Willington"),
("Stour, Cherington", "Stour Cherington"),
("Stour, Ascott", "Stour Ascott","Stout Ascott village"),
("Stratford Upon Avon by RSC", "Stratford upon avon by RSC"),
("STW outfall Ilmington", "STW outfall Ilmington"),
("Sutton Brook, High Street", "Sutton Brook - High St - Brailes", "Sutton Brook - High St, Brailes", "Sutton Brook,High Street","Sutton Brook - High Street Brailes","Sutton Brook - High Street, Brailes"),
("Swiffen Bank","Swiffen Bank"),
("Swillgate A38","Swilgate A38","Swillgate A38","Swillgate A39", "Carrant A38"),
("Swillgate","Swillgate lowdilow lane"),
("Swillgate TNR 2nd bridge","Swillgate TNR 2nd bridge"),
("Talton Lodge","Talton Lodge"),
("The craves","The Craves","Th craves chipping campden"),
("The Dell","The dell"),
("Twyning Quay","Twyning Fleet","Twyning key","Twyning Quay"),
("Walcot Lane", "Walcot Lane"),
("Welford Boat Station", "Welford Boat Station"),
("Weston on Avon", "Weston on Avon"),
("Whitsun Brook, Atch", "Whistun Brook Atch", "Whitsun Brook Atch Lench Road"),
("Whitsun Brook, Church Lench Bridge", "Whitsun Brook Church Lench Bridge"),
("Whitsun Brook, Bishampton","Whitsun Brook north of Bishampton"),
("Whitsun Brook, Rous Church Lench", "Whitsun Brook Rous Church Lench"),
("Whitsun Brook, Rous Lench Bishampton", "Whitsun Brook, Rous Lench Bishampton","Whitsun Brook Rous Lench Bishampton"),
("Whitsun Brook, Low road, Church Lench", "Whitsun Brook, Low Road, Church Lench","Whitsun Brook. Low road, Church Lench"),
("WyrePiddleBrook","WyrePiddleBrook"),
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
MAX_NITRATES = 10


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

BAR_WIDTH = 4