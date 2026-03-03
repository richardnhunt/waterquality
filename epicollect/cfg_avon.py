# Avonvale River Action Group and SafeAvon
# ========================================

OUTPUT_FOLDER = "avon"

# WQMN survey
INPUT_CSV_FILENAME = 'form-1__wqmn-water-quality-survey.csv'
COL_NAME = 4
COL_DATE = 5
COL_RIVER = 6
COL_PLACE = 7
COL_LAT = 8
COL_LONG = 9
COL_TIME = 14
COL_RIVER_HEIGHT = 15
COL_CONDUCTIVITY = 19
COL_TEMPERATURE = 20
COL_PHOSPHATES = 21
COL_NITRATES = 23
COL_AMMONIA = 24
COL_NOTES = 29

# SafeAvon survey (original format)
SAFEORG_CSV_FILENAME = 'form-1__data-entry_org.csv'
COL_SAFEORG_NAME = 14
COL_SAFEORG_DATE = 13
COL_SAFEORG_RIVER = None
COL_SAFEORG_PLACE = 4
COL_SAFEORG_LAT = 5
COL_SAFEORG_LONG = 6
COL_SAFEORG_TIME = 12
COL_SAFEORG_RIVER_HEIGHT = 20
COL_SAFEORG_CONDUCTIVITY = 16
COL_SAFEORG_TEMPERATURE = 17
COL_SAFEORG_PHOSPHATES = 19
COL_SAFEORG_NITRATES = 18
COL_SAFEORG_AMMONIA = None
COL_SAFEORG_NOTES = 21

# SafeAvon survey (new format)
SAFEAVON_CSV_FILENAME = 'form-1__data-entry.csv'
COL_SAFE_NAME = 15 # e.g. SA0106 or "I don't have an ID / can't remember it"
COL_SAFE_DATE = 13 # e.g. 02/03/2026
COL_SAFE_RIVER = 3 # up to ' - ', e.g. Avon River - Tewkesbury - Black Bear Pub 01/03/2026 SA0001
COL_SAFE_PLACE = 4 # e.g. Avon River - Tewkesbury - Black Bear Pub
COL_SAFE_LAT = 6
COL_SAFE_LONG = 7
COL_SAFE_TIME = 14 # e.g. 10:00
COL_SAFE_RIVER_HEIGHT = 22
COL_SAFE_CONDUCTIVITY = 16
COL_SAFE_TEMPERATURE = 17
COL_SAFE_PHOSPHATES_HI = 20 # use whichever column has number in it, prefer hi
COL_SAFE_PHOSPHATES_LO = 21 # lo range phosphates
COL_SAFE_NITRATES = 18 # e.g. "10" or "0, 5" or "I did not take a nitrate measurement."
COL_SAFE_AMMONIA = None
COL_SAFE_NOTES = 25

# River names we are monitoring, case insensitive, we use the first one
RIVER_NAMES = [ ("Warwickshire Avon", "warwickshire avon fladbury", "warwickshire river avon", "warks avon", "River Avon Worcs", "Warwickshire  Avon","Avon","Worcestershire Avon","Avon river"),
                ("Warwickshire Arrow", "Arrow", "Warks Arrow", "Arrow river"),
                ("Alne", "River Alne"),
                ("Isbourne","Isbourne"),
                ("Badsey Brook","Badsey Brook"),
                ("Elmley Brook","Elmley Brook","River Avon tributary brook"),
                ("Mary Brook","Mary Brook"),
                ("Swilgate","Swilgate river"),
                ("Sutton Brook","Sutton brook"),
                ("Carrant Brook","Carrant brook"),
                ("Stour","Stour river"),
                ("Isbourne","Isbourne river") ,
                ("Bell Brook","Bell brook"),
                ("Sherbourne Brook","Sherbourne brook"),
                ("Bow Brook", "Bow brook"),
                ("Cam Brook", "Cam brook"),
                ("Fosseway Brook", "Fosseway brook"),
                ("Piddle Brook", "Piddle brook"),
                ("Tributary (Alne River)", "tributary (alne river)"),
                ("Stratford-upon-avon canal", "stratford-upon-avon canal"),
                ("Stowe", "stowe river"),
                ("Whitsun brook", "Whitsun brook"),
                ("Howcombe spring", "Howcombe spring"),
                ("Knee brook", "Knee brook"),
                ("Itchen", "Itchen river"),
                ("Nethercote brook", "Nethercote brook"),
                ("Blockley Brook","Blockley Brook")
              ]

# We map some names for consitency, include the location number if there is one (will be then stripped out)
# Names get changed to the first one in the list
SYNONYMS = [ ("220 Fladbury, Jubilee Bridge", "fladbury, Jubilee Bridge"),
             ("220 Fladbury, Jubilee Bridge", "Jubilee Bridge Fladbury"),
             ("220 Fladbury, Jubilee Bridge", "Jubilee Bridge"),
             ("400 Eckington Bridge", "Eckington Bridge"),
             ("270 Pershore, Leisure Centre", "Leisure Centre Pershore", "Pershore Leisure Centre", "Pershore les cent 270", "Pershore Leisure Centre 270","Pershore LC 270","L centre Pershore 270","Pershore"),
             ("230 Charlton, Merry Brook", "230merry brook"),
             ("120 Offenham, Dead Mens Ait", "120a offenham Dead Mens Ait (opp)"),
             ("100 Wootten Warwen", "Pennyford Lane Bridge", "Pennyford Bridge lane", "Pennyford Lane (BAA WATER)", "Pennyford bridge"),
             ("Lido Stratford upon Avon", "Lido"),
             ("120 Spernal Lane", "Spernall Lane Bridge", "Spernal Lane Bridge", "spernall", "spernal lane"),
             ("103 Cleeve Prior", "Cleeve Prior", "Cleeve Prior 103"),
             ("240 Cropthorne, Holland House", "Holland House", "Holland House site 240"),
             ("25 Hinton, Bridge","25 Hinton, bridge"),
             ("30 Hampton, Bridge","30 Hampton, bridge"),
             ("108 B4510 Bridge", "200 B4510 bridge"),
             ("245 Cropthorne Main Street, Bridge", "245 Cropthorne Main Street Bridge"),
             ("280 Pershore, Bridges", "Pershore bridges"),
             ("Rugby, Steam Turbine", "Rugby; Steam Turbine", "Rugby (Steam Turbine)"),
             ("Barford Below","Barford B"),
             ("Barford Above","Barford A"),
             ("100 Bidford Bridge", "Bidford 100"),
             ("Priory Water","Priory water"),
             ("305 Mary Brook","305 Mary Brook","305","Comberton to Pershore Road Bridge","Great Comberton to Pershore"),
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
             ("Whitsun Brook, Church Lench Bridge", "Whitsun Brook Church Lench Bridge", "Whitson Brook, Atch"),
             ("Whitsun Brook, Bishampton","Whitsun Brook north of Bishampton"),
             ("Whitsun Brook, Rous Lench Bishampton", "Whitsun Brook, Rous Lench Bishampton","Whitsun Brook Rous Lench Bishampton"),
             ("Whitsun Brook, Low road, Church Lench", "Whitsun Brook, Low Road, Church Lench","Whitsun Brook. Low road, Church Lench","Whitsun Brook, Rous Church Lench"),
             ("WyrePiddleBrook","WyrePiddleBrook"),
             ("Bubbenhall road","Bubbenhall road, Bubbenhall","Bubbenhall road","Bubbenhall","Bubenhall road"),
             ("High Street Brailes","High Street Brailes","Brailes main road","Sutton Brook, High Street"),
             ("Stour, Shipston Mill Bridge","Stour, Shipston Mill Bridge","Stour, Mill Bridge Shipston","Stour, Shipston Mill Bridge"),
             ("Defford, Arden Sailing Club","Defford, Arden Sailing Club","Arden Sailing Club"),
             ("Avon Smith's Meadow","Avon Smith's Meadow","Piddle Brook Bridge"),
             ("Carrant Brook, Back","Carrant Brook, Back","Carrant Brook Beckford","Carrant back lane Beckford 28/06/2024 Geoff"),
             ("STW outfall Ilmington","STW outfall Ilmington","ST Outflow","Site 3: Severn Trent Plant","Severn Trent Outflow"),
             ("Cam, Chimping Campden Craves","Cam, Chimping Campden Craves","The craves"),
             ("Cam, Chimping Campden Craves","Cam, Chimping Campden Craves","The craves"),

           ]

# Locations which have a number
# If we find a number in the place name in spreadsheet, then try to look up that number for the river in this list first
# Place name in table below must be the same as SYNONYMS above but without the number
SAMPLING_LOCATIONS = [
    ("Isbourne", 25, "Hinton, Bridge", 52.063505, -1.967044),
    ("Isbourne", 30, "Hampton, Bridge", 52.085601, -1.956927),
    ("Warwickshire Avon", 50, "B4510 bridge", 52.104597, -1.916057),
    ("Warwickshire Avon", 100, "Bidford Bridge", 52.163627, -1.856484),
    ("Warwickshire Avon", 103, "Cleeve Prior", 52.147696, -1.884128),
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
    ("Warwickshire Avon", 201, "Chadbury, Whitehouse farm right of pumphouse", 52.119645, -1.982726),
    ("Warwickshire Avon", 202, "Chadbury, Whitehouse farm left of pumphouse", 52.120003, -1.983989),
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
    ("Warwickshire Avon", 400, "Eckington Bridge", 52.0793, -2.1149),
    ("Warwickshire Arrow", 100, "Studley", 52.27419029342931, -1.883789898760419),
    ("Warwickshire Arrow", 120, "Spernal Lane", 52.26057296331432, -1.8762366844985907),
    ("Warwickshire Arrow", 200, "Salford Bridge", 52.16338142682303, -1.8803195030184976),
    ("Alne", 100, "Wootten Warwen (=Pennyford Lane Bridge)", 52.2581988721852, -1.783556704096704),
    ("Alne", 130, "Little Alne", 52.250200998557055, -1.7935596094704758),
    ("Alne", 150, "Great Alne (Pelham Lane)", 52.23257559455438, -1.8317339626316056),
    ("Warwickshire Avon", 0, "Barford Below", 52.245253, -1.617944),
    ("Warwickshire Avon", 0, "Barford Above", 52.256291, -1.597904),
    ("Warwickshire Avon", 0, "Lucy's Mill Bridge", 52.18399258673163, -1.7081747999999999)
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
FIG_SIZE_X_INCHES = 2
FIG_SIZE_Y_INCHES = 1.5

# ...positions as fraction of figure size
MARGIN_TOP_FRACTION = 0.995
MARGIN_BOTTOM_FRACTION = 0.11
MARGIN_LEFT_FRACTION = 0.08
MARGIN_RIGHT_FRACTION = (1 - MARGIN_LEFT_FRACTION)

YAXIS_LABEL_SPACING = 0.5
TICK_LABEL_SPACING = 0.5
SPACE_BETWEEN_SUBPLOTS = 0.1

BAR_WIDTH = 2