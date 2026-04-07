# Avonvale River Action Group and SafeAvon
# ========================================
# Comment out filenames to not parse

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

# STEP 1
#
# River names we are monitoring, checked against the "RIVER" column along with their synonyums.  We use
# the first entry name.  If no river found then included in output regardless.
#
# If river column empty then we attempt to parse from the PLACE column which may include it before ' - ' or ','
# and if find it then separate it out from PLACE and use it for RIVER.  This then avoids this type of duplicate entry.
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
                ("Bell Brook","Bell Brook","Bell brook"),
                ("Sherbourne Brook","Sherbourne Brook","Sherbourne brook","Shaerbourne Brook", "Sherborne Brook", "Sherbourne Brook"),
                ("Bow Brook", "Bow brook"),
                ("Cam Brook", "Cam brook"),
                ("Fosseway Brook", "Fosseway brook"),
                ("Piddle Brook", "Piddle brook"),
                ("Tributary (Alne River)", "tributary (alne river)"),
                ("Stratford-upon-avon canal", "stratford-upon-avon canal"),
                ("Stowe", "stowe river"),
                ("Whitsun Brook", "Whitsun brook"),
                ("Howcombe Spring", "Howcombe spring"),
                ("Knee brook", "Knee brook"),
                ("Itchen", "Itchen river"),
                ("Nethercote Brook", "Nethercote brook"),
                ("Blockley Brook","Blockley Brook")
              ]


# STEP 2
#
# Volunteers are varied and also not always consistent with their names, so we need to map to one for consitency,
# include the location number if there is one (will be then stripped out). Names are checked case insenstive and then get changed
# to the first one in the list.  For this reason will sometimes see the same repeated match to correct case for some entries.
SYNONYMS = [ ("220 Fladbury, Jubilee Bridge", "fladbury, Jubilee Bridge", "Jubilee Bridge Fladbury", "Jubilee Bridge", "Jubilee"),
             ("Eckington, Bridge","400 Eckington Bridge", "Eckington Bridge","390 Eckington Bridge","300 Eckington Bridge"),
             ("Pershore, Leisure Centre", "270 Pershore, Leisure Centre", "Leisure Centre Pershore", "Pershore Leisure Centre", "Pershore les cent 270", "Pershore Leisure Centre 270","Pershore LC 270","L centre Pershore 270","Pershore"),
             ("230 Charlton, Merry Brook", "230merry brook"),
             ("120 Offenham, Dead Mens Ait", "120a offenham Dead Mens Ait (opp)"),
             ("100 Wootten Warwen", "Pennyford Lane Bridge", "Pennyford Bridge lane", "Pennyford Lane (BAA WATER)", "Pennyford bridge"),
             ("Lido Stratford upon Avon", "Lido"),
             ("120 Spernal Lane", "Spernall Lane Bridge", "Spernal Lane Bridge", "spernall", "spernal lane"),
             ("103 Cleeve Prior", "Cleeve Prior", "Cleeve Prior 103"),
             ("240 Cropthorne, Holland House", "Holland House", "Holland House site 240"),
             ("25 Hinton, Bridge","25 Hinton, bridge"),
             ("30 Hampton, Bridge","30 Hampton, bridge"),
             ("108 B4035 Bridge", "108 B4510 Bridge"),
             ("245 Cropthorne Main Street, Bridge", "245 Cropthorne Main Street Bridge","Cropthorne Main Street, Bridge","Cropthorne Main Street Bridge","Main Street Cropthorne", "Cropthorne Main Street"),
             ("280 Pershore, Bridges", "Pershore bridges"),
             ("Rugby, Steam Turbine", "Rugby; Steam Turbine", "Rugby (Steam Turbine)", "Rugby Steam Turbine"),
             ("Barford Below","Barford B"),
             ("Barford Above","Barford A"),
             ("100 Bidford Bridge", "Bidford 100"),
             ("Priory Water","Priory water"),
             ("305 Mary Brook","305 Mary Brook","305","Comberton to Pershore Road Bridge","Great Comberton to Pershore","305"),
             ("Tewkesbury - Abbey Mill", "Abbey Mill"),
             ("After sewage works", "After sewage works"),
             ("After ST outflow", "After ST outflow"),
             ("Alveston - Swiffen Bank", "Swiffen Bank", "Alveston Swiffen Bank", "Alveston Swiffen Bank","Swiffen Bank","Alveston - Swiffen Bank"),
             ("Alveston Weir", "Alveston Weir"),
             ("Avon Smith's Meadow","Avon Smith's Meadow", "Avon Smiths Meadow", "AvonSmithsMeadow", "AvonSmith'sMeadow", "Avon  Smiths Meadow", "Avon Smith Meadow","Avon  Smith's Meadow", "AvonMeadow", "Avon meadow"),
             ("Barton - Heart of England Forest", "Barton","Barton"),
             ("Tewkesbury - Black Bear Pub","Black Bear"),
             ("Brailes main road","Brailes main road"),
             ("Bredon - Bredon Marina","Bredon - Bredon Marina","Bredon Marina","Dock Lane Bredon","Dock Lane.Bredon", "Dock lane. Bredon", "Bredon docklane"),
             ("Carrant Brook, Bredon Road", "Carrant Bredon Rd", "Carrant Bredon Road", "Carrant. Bredon Road", "Carrant. Bredon Rd"),
             ("Carrant Brook Beckford", "Carrant Brook Beckford Back Lane"),
             ("Tewkesbury - M5 Bridge", "Carrant Brook, M5 Bridge", "Carrant Brook M5", "Carrant Brook M5 Bridge", "Carrant M5 Bridge","Carrant m5"),
             ("Tewkesbury - Mitton Path", "Carrant Brook, Mitton Bridge", "Carrant Mitton Bridge", "Carrant Mitton Path", "Mitton path", "Mitton parh"),
             ("Carrant Brook, Bredon Road", "Carrant Brook Bredon Rd"),
             ("Beckford - Crashmore Ln", "Carrant Brook, Crashmore Lane", "Carrant crashmore lane"),
             ("Carters Lane", "Carters Lane", "Carter Lane"),
             ("Clifford Chambers - Mill Bridge", "Clifford Chambers Mill Bridge", "Clifford Mill Bridge", "Clifford Chambers", "Clifford Chambers mill bridge", "Clifford mill bridge", "Clifford  mill bridge"),
             ("Fosseway Brook, Cross Leys", "Cross Leys", "CrossLeys", "Fosseway Brook, Cross Leys", "Fosseway Brook; Cross Leys", "Fosseway Brook; Cross Leys"),
             ("Stour, Fell Mill Footbridge", "Fell Mill Footbridge", "Fell Mill River Bridge", "Fell Mill Lane Footbridge"),
             ("Ford Langley", "Ford Langley"),
             ("Fosseway Brook", "Fosseway Brook, Middle Street", "Fosseway Brook; Middle Street", "Fosseway Brook; Middle Street", "Fosseway Brook; Middle St"),
             ("Source","source"),
             ("Fosseway Brook", "Fosseway Brook, Severn Trent Outflow", "Fosseway Brook, ST Outflow", "Fosseway Brook; ST Outflow"),
             ("Great Comberton Quay", "Great Comberton Quay", "Quay Lane Great Comberton"),
             ("Hampton Lucy - Bridge", "Hampton Lucy"),
             ("Hampton Wood", "Hampton Wood"),
             ("Heath Culvert", "Heath Culvert Ilmington"),
             ("Heath Gate", "Hath Gate"),
             ("High Street Brailes", "High St Brailes", "High street", "High Street Brailes", "High Street,Brailes", "High Street, Lower Brailes","High Street Brailes","Brailes main road","Sutton Brook, High Street"),
             ("Ilmington - Middle St", "Ilmington Middle Street","Site 1; Ilmington Middle Street", "Ilmington Middle St", "Illmington middle st","Middle Street","Middle Street Ilmington","MiddleStreet","Site 1 ; Middle Street", "Site 1 ; Middle Street", "Site 1  ;  Middle"),
             ("Winchombe - Silk Mill Ln","Isbourne"),
             ("Langley - Ford","Langley Ford","Langley","The Ford","ford langley"),
             ("Tewkesbury - Lower Lode Ln","Lower Lode", "Lowerl Lode"),
             ("Lucy's Mill Bridge","Lucy's Mill Bridge","Stratford-upon-Avon - Lucy`s Mill Bridge"),
             ("Luddington - Avonbank Dr","Luddington Avonbank Drive","Luddington Avonbank Drive","Luddington Avon Bank", "Luddington Avon Drive", "Avonbank Drive", "Avonbank"),
             ("Luddington Pitch","Luddington Pitch"),
             ("Peopleton - Mill Bridge","Mill Bridge, Peopleton", "Mill  Bridge, Peopleton", "Mill Bridge Peopleton", "Mill Bridge, Peopleton", "Mill Bridge,Peopleton", "Mill Bridge  Peopleton", "Peopleton - Mill Bridge"),
             ("Mill Stour, Newbold", "Mill Stour Newbold","Newbold Mill Stour","Stour,Newbold,Mill"),
             ("New barn", "New barn", "New barn Brailes", "New Barn Farm", "New Barn Farm Brailes", "New Barn Farm,Brailes","NewBarn", "Sutton Brook - New Barn Farm", "Sutton Brook, New Barn Farm", "Sutton Brook,Brailes","New Farm Barn Brailes"),
             ("Pershore Bridges","Pershore bridges"),
             ("Pershore leisure centre","Pershore leisure centre"),
             ("Piddle Brook Long Lane Pinvin","Piddle Brook Long Lane Pinvin"),
             ("Piddle Brook Norton Beachamp Bridge", "Piddle Brook Norton Beachamp Bridge","Norton Beachamp - Bridge"),
             ("Piddle Brook Bridge","Piddle Brook Bridge", "Piddle Brook Wyre Piddle Bridge","Piddlebrook bridge", "Piddlebrook WyrePiddleBridge", "PiddleBrook-Wyre Piddle Bridge","PiddleBrookBridge","Piddlebrook Wyre piddle bridge"),
             ("Pitch 16", "Pitch 15", "Pitch 16", "Pitch16"),
             ("Preston Bagot - Brook","Preston Bagot Brook","Preston  Bagot Brook"),
             ("Preston Bagot - Canal", "Preston Bagot Canal","Preston Bigot Canal"),
             ("Preston on Stour - Preston Ln Bridge", "Stour, Preston River Bridge", "Preston River Bridge", "Preston onStour River Bridge","Preston- on- stour river bridge", "Preston- on- stour"),
             ("Stowe, Lower Fields Farm", "R.Stowe - Lower Fields Farm", "R.Stowe, Lower Fields Farm","R.Stowe,  Lower Fields Farm, Napton","R.Stowe,  Lower Field's Farm, Napton"),
             ("Stockton - New Zealand Spinney", "R. Stowe,New Zealand Spinney","R.Stowe, New Zealand Spinney, Stockton","R.Stowe, New Zealand Spinney","New Zealand Spinney","Stowe, New Zealand Spinney"),
             ("Stowe, Spring", "R. Stowe,Spring","R.Stowe, Spring by Howcombe Allotments, Napton","R.Stowe, Spring by Howcombe Allotments,Napton"),
             ("Stour, Cherington", "River Stour Cherington after sewerage works"),
             ("Tiddington - School Ln", "School Lane"),
             ("Tiddington - Carters Ln", "Carters Lane"),
             ("Severn Sailing Club","Severn Sailing Club","Seven sailing club","SSC Bedons Norton","SSC Bredon's Norton","SSC BREDONS NORTON","Bredon`s Norton - Severn Sailing Club"),
             ("Severn Trent Outflow", "Severn Trent Outflow"),
             ("Shipston - Mill Bridge", "Shipston - Mill Bridge","Shipston mill bridge"),
             ("Site 2; Cross Leys culvert","Site 2 ; Cross Leys Culvert", "Site 2  ;  Cross","site 2; cross leys culvert"),
             ("Site 3; Severn Trent Plant","Site 3 ; Severn Trent Water Processing plant outflow", "Site 3  ;  Severn"),
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
             ("Sutton Brook, High Street", "Sutton Brook - High St - Brailes", "Sutton Brook - High St, Brailes", "Sutton Brook,High Street","Sutton Brook - High Street Brailes","Sutton Brook - High Street, Brailes"),
             ("Swillgate A38","Swilgate A38","Swillgate A38","Swillgate A39", "Carrant A38"),
             ("Tewkesbury - A38","Swillgate","Swillgate lowdilow lane"),
             ("Swillgate TNR 2nd bridge","Swillgate TNR 2nd bridge"),
             ("Newbold on Stour - Talton Lodge","Talton Lodge"),
             ("The Dell","The dell"),
             ("Twyning Quay","Twyning Fleet","Twyning key","Twyning Quay"),
             ("Walcot Lane", "Walcot Lane"),
             ("Welford-on-Avon - Boat Station", "Welford-on-Avon - Boat Station", "Warwickshire Avon, Welford Boat Station"),
             ("Welford on Avon above weir","Welford angling"),
             ("Weston-on-Avon - Duck Ln", "Weston-on-Avon - Duck Ln", "Weston on Avon", "Weston on Avon"),
             ("Naunton Beauchamp - Bridge","Piddle Brook Norton Beauchamp Bridge","Piddle Brook Norton Beachamp Bridge"),
             ("Church Lench - Atch Lench Rd Bridge","Church Lench Bridge", "Whitsun Brook Church Lench Bridge", "Whitson Brook, Atch","Atch", "Whistun Brook Atch", "Whitsun Brook Atch Lench Road"),
             ("Bishampton - Abberton Rd", "Bishampton - Abberton Rd", "Bishampton","Whitsun Brook north of Bishampton"),
             ("Rous Lench Bishampton", " Rous Lench Bishampton","Whitsun Brook Rous Lench Bishampton","Rous Lench - Rd to Bishampton"),
             ("Low road, Church Lench", " Low Road, Church Lench","Whitsun Brook. Low road, Church Lench"," Rous Church Lench", "Church Lench - Low Rd","Whitsun Brook Rous Church Lench"),
             ("WyrePiddleBrook","WyrePiddleBrook"),
             ("Bubbenhall road","Bubbenhall road, Bubbenhall","Bubbenhall road","Bubbenhall","Bubenhall road"),
             ("Stour, Shipston Mill Bridge","Stour, Shipston Mill Bridge","Stour, Mill Bridge Shipston","Stour, Shipston Mill Bridge"),
             ("Defford, Arden Sailing Club","Defford, Arden Sailing Club","Arden Sailing Club"),
             ("Carrant Brook, Back","Carrant Brook, Back","Carrant Brook Beckford","Carrant back lane Beckford 28/06/2024 Geoff"),
             ("Ilmington - Sewage Outflow", "STW outfall Ilmington","STW outfall Ilmington","ST Outflow","Site 3; Severn Trent Plant","Severn Trent Outflow"),
             ("Chimping Campden Craves", "Cam, Chimping Campden Craves", "Cam Chipping Campden Craves", "Cam Chipping Campden", "Chipping Campden Craves", "Craves Chipping Campden","The Craves","Th craves chipping campden"),
             ("Abbots Barton", "Eastern Meadows"),
             ("Fishermans seat", "Near sluice & bench", "Fishermans seat by the stile", "Fishermans bench by the stile", "Bench near stile","Fisherman’s bench by the stile","Fisherman’s seat by the stile","Fisherman’s bench by stile","Fishermans seat"),
             ("Chilland Ford", "Chilland"),
             ("Bush Inn Ovington", "Bush Inn, Ovington"),
             ("Meadow upper","meadow 1"),
             ("Meadow lower","meadow 2","meadow 2 (lower)"),
             ("Stourport confluence with Severn", "port; Stour confluence with Severn","port; Stour at Confluence with the Severn","port; confluence of Stour with Severn","port; Stour at confluence with Severn"),
             ("Stourport (Tesco footbridge)","port (Tesco footbridge)","port Tesco bridge", "port; Tesco pedestrian bridge","Tesco footbridge","Tesco bridge, Stourport","Tesco bridge"),
             ("A14 below Naseby reservoir","A14 Naseby res","Naseby reservoir A14","A14 below Naseby res.","At A14 below Naseby res","A14, below Naseby reservoir","A14 below Naseby reservoir"),
             ("The Wharf, Welford","Welford, The Wharf"),
             ("Stanford on Avon road bridge","Stanford on Avon"),
             ("Lilbourne - Cathorpe road","Lilbourne - Catthorpe road","Lilbourne; Station road bridge","Lilbourne road bridge","Lilbourne, Catthorpe road bridge","Lilbourne"),
             ("Church Lawford road bridge","Church Lawford, road bridge","Church Lawford"),
             ("Ashow footbridge","Ashow"),
             ("Warwick - Warwick Boat Club","Barford above"),
             ("Barford - Hampton Wood","Barford - Hampton Wood","Hampton Wood"),
             ("Village Green","Village Green"),
             ("Cheriton House","Cheriton House"),
             ("Fishing bench near stile", "Near stile & bench"),
             ("Marsh Cottage","Marsh cottage"),
             ("Itchen culvert","Ditch","Ditch by culvert","Culvert"),
             ("Beckford - Sewage Works","Carrant Beckford sewage works"),
             ("Beckford - Back Ln","Back","Carrant Brook, Back", "Carrant Brook Back", "Carrant Brook Back Lane"),
             ("Great Comberton - Quay Ln","Great Comberton Quay","Avon, Quay Lane", "River Avon at Quay Lane"),
             ("210 Fladbury, Paddle Club", "Fladbury - Fladbury Paddle Club", "Fladbury, Paddle Club", "Fladbury Paddle Club"),
             ("Snitterfield - Bell Brook", "Bell Brook", "Snitterfield - Bell Brook, Bell Brook", "Bell Brook 1"),
             ("Norton Lindsey - Sherbourne Brook","Sherbourne Brook","Shaerbourne Brook", "Sherborne Brook", "Sherbourne Brook","Sherbourne Brook 1","Shaerbourne Brook 1","Sherborne Brook 1"),
             ("Oxbow","Oxbow","Ox bow"),
             ("Chadbury, Whitehouse farm right of pumphouse", "201 Whitehouse farm right of pumphouse"),
             ("Chadbury, Whitehouse farm left of pumphouse", "202 Whitehouse farm left of pumphouse")
           ]


# STEP 3
# Locations which have a number or we want to give a fixed latitude and longitude
#
# If we find a number in the place name in spreadsheet, then try to look up that number for the river in this list first
# Place name in table below must be the same as SYNONYMS above but without the number
# Note numbers are not unique but river order
SAMPLING_LOCATIONS = [
    ("Isbourne", 25, "Hinton, Bridge", 52.063505, -1.967044),
    ("Isbourne", 30, "Hampton, Bridge", 52.085601, -1.956927),
    ("Warwickshire Avon", 100, "Bidford Bridge", 52.163627, -1.856484),
    ("Warwickshire Avon", 103, "Cleeve Prior", 52.147696, -1.884128),
    ("Badsey Brook", 108, "B4035 Bridge", 52.091779, -1.907077),
    ("Badsey Brook", 200, "B4510 bridge", 52.104597, -1.916057),
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
    ("Warwickshire Avon", 0, "Lucy's Mill Bridge", 52.18399258673163, -1.7081747999999999),
    ("Warwickshire Arrow",0,"Alcester - Gunnings Bridge",52.21722,-1.86818),
    ("Warwickshire Avon",0,"Alveston - Swiffen Bank",52.20641,-1.65400),
    ("Warwickshire Avon",0,"Alveston - Weir",52.21162,-1.66033),
    ("Warwickshire Avon",0,"Barford - Barford Community Orchard",52.23667,-1.60583),
    ("Warwickshire Avon",0,"Barford - Hampton Wood",52.23821,-1.62449),
    ("Warwickshire Avon",0,"Barford - Verdon Place",52.24657,-1.60410),
    ("Warwickshire Avon",0,"Barton - Heart of England Forest",52.16122,-1.83014),
    ("Warwickshire Avon",0,"Bredon - Bredon Marina",52.03360,-2.11704),
    ("Warwickshire Avon",0,"Severn Sailing Club",52.05072,-2.11747),
    ("Warwickshire Avon",0,"Evesham - St Andrew`s Church",52.08659,-1.95670),
    ("Warwickshire Avon",0,"Fladbury - Fladbury Paddle Club",52.11812,-2.00653),
    ("Warwickshire Avon",0,"Great Comberton - Quay Ln",52.08178,-2.07067),
    ("Warwickshire Avon",0,"Hampton Lucy - Bridge",52.21204,-1.62446),
    ("Warwickshire Avon",0,"Luddington - Avonbank Dr",52.17700,-1.73598),
    ("Warwickshire Avon",0,"Luddington - Pitch 16",52.17282,-1.74453),
    ("Warwickshire Avon",0,"Pershore - Leisure Centre",52.11129,-2.07169),
    ("Warwickshire Avon",0,"Pershore - Pershore Bridges",52.10434,-2.07104),
    ("Warwickshire Avon",0,"Stratford-upon-Avon - Lucy`s Mill Bridge",52.18369,-1.70782),
    ("Warwickshire Avon",0,"Stratford-upon-Avon - RSC",52.19069,-1.70307),
    ("Warwickshire Avon",0,"Stratford-upon-Avon - Trinity Church",52.18738,-1.70665),
    ("Warwickshire Avon",0,"Tewkesbury - Abbey Mill",51.99130,-2.16263),
    ("Warwickshire Avon",0,"Tewkesbury - Black Bear Pub",51.99743,-2.15613),
    ("Warwickshire Avon",0,"Tewkesbury - Lower Lode Ln",51.98348,-2.17704),
    ("Warwickshire Avon",0,"Tiddington - Carters Ln",52.20240,-1.67692),
    ("Warwickshire Avon",0,"Tiddington - School Ln",52.20241,-1.67869),
    ("Warwickshire Avon",0,"Twyning Green - The Fleet Inn",52.02704,-2.14044),
    ("Warwickshire Avon",0,"Twyning Green - Twyning Quay",52.02635,-2.14021),
    ("Warwickshire Avon",0,"Warwick - Longbridge Sewage Works",52.26311,-1.59854),
    ("Warwickshire Avon",0,"Warwick - Warwick Boat Club",52.25635,-1.59796),
    ("Warwickshire Avon",0,"Welford-on-Avon - Boat Station",52.17523,-1.79187),
    ("Warwickshire Avon",0,"Weston-on-Avon - Duck Ln",52.16743,-1.77448),
    ("Warwickshire Avon",0,"Wyre Piddle - Smiths Meadows",52.12289,-2.05746),
    ("Bell Brook",0,"Snitterfield - Bell Brook",52.24485,-1.66175),
    ("Blockley Brook",0,"Draycott - Above",52.02241,-1.74276),
    ("Blockley Brook",0,"Draycott - Below",52.02512,-1.73635),
    ("Bow Brook",0,"Peopleton - Mill Bridge",52.15178,-2.09651),
    ("Bow Brook",0,"Pershore - Walcot Ln",52.13050,-2.07864),
    ("Cam Brook",0,"Chipping Campden - Above Works",52.04930,-1.78022),
    ("Cam Brook",0,"Chipping Campden - Craves",52.04852,-1.78567),
    ("Cam Brook",0,"Chipping Campden - Lady Juliana's Gateway",52.04990,-1.77640),
    ("Cam Brook",0,"Chipping Campden - Sewage Treatment Works",52.05223,-1.76161),
    ("Cam Brook",0,"Chipping Campden - Works Exit",52.05221,-1.76157),
    ("Carrant Brook",0,"Aston on Carrant - Footbridge",52.01101,-2.08250),
    ("Carrant Brook",0,"Beckford - Back Ln",52.01843,-2.03878),
    ("Carrant Brook",0,"Beckford - Crashmore Ln",52.01453,-2.05770),
    ("Carrant Brook",0,"Beckford - Sewage Works",52.01556,-2.04428),
    ("Carrant Brook",0,"Tewkesbury - Bredon Rd",51.99844,-2.15275),
    ("Carrant Brook",0,"Tewkesbury - M5 Bridge",52.01184,-2.12026),
    ("Carrant Brook",0,"Tewkesbury - Mitton Path",51.99978,-2.14102),
    ("Carrant Brook",0,"Tewkesbury - Railway Bridge",52.01364,-2.10878),
    ("Fosseway Brook",0,"Ilmington - Cross Leys",52.09301,-1.68630),
    ("Fosseway Brook",0,"Ilmington - Heath Gate",52.09478,-1.67399),
    ("Fosseway Brook",0,"Ilmington - Middle St",52.09008,-1.69260),
    ("Fosseway Brook",0,"Ilmington - Sewage Outflow",52.09442,-1.67590),
    ("Howcombe Spring",0,"Napton on the Hill - Howcombe Allotments",52.24599,-1.32485),
    ("Isbourne",0,"Evesham - Pershore Rd Bridge",52.08562,-1.95699),
    ("Isbourne",0,"Winchcombe - A",51.93929,-2.00302),
    ("Isbourne",0,"Winchcombe - B",51.95867,-1.97006),
    ("Isbourne",0,"Winchcombe - C",51.96267,-1.95792),
    ("Isbourne",0,"Winchcombe - D",51.97114,-1.95350),
    ("Isbourne",0,"Winchcombe - Silk Mill Ln",51.95367,-1.96233),
    ("Itchen",0,"Southam - Stoney Mill Bridge",52.25610,-1.40647),
    ("Knee Brook",0,"Aston Magna - Above Outlet",52.02177,-1.70700),
    ("Knee Brook",0,"Aston Magna - Below Outlet",52.02202,-1.70684),
    ("Knee Brook",0,"Todenham - Before Stour",52.03572,-1.64331),
    ("Nethercote Brook",0,"Great Wolford - Above",52.00087,-1.62478),
    ("Nethercote Brook",0,"Great Wolford - Below",52.01013,-1.62650),
    ("Nethercote Brook",0,"Long Compton - Above",51.99602,-1.58582),
    ("Nethercote Brook",0,"Long Compton - Below",51.99764,-1.59626),
    ("Piddle Brook",0,"Naunton Beauchamp - Bridge",52.16998,-2.05835),
    ("Piddle Brook",0,"Pinvin - Long Ln",52.14840,-2.05523),
    ("Piddle Brook",0,"Radford - Evesham Rd",52.19681,-1.99251),
    ("Piddle Brook",0,"Wyre Piddle - Bridge",52.12639,-2.05653),
    ("Sherbourne Brook",0,"Norton Lindsey - Sherbourne Brook",52.25262,-1.66869),
    ("Stour",0,"Ascott - Village",52.01324,-1.53875),
    ("Stour",0,"Burmington - Nethercote Junction",52.03187,-1.61772),
    ("Stour",0,"Cherington - Sewage Treatment Works",52.02959,-1.58024),
    ("Stour",0,"Clifford Chambers - Mill Bridge",52.16637,-1.70803),
    ("Stour",0,"Newbold on Stour - Mill Ln",52.11358,-1.63309),
    ("Stour",0,"Newbold on Stour - Talton Lodge",52.12209,-1.65026),
    ("Stour",0,"Preston on Stour - Preston Ln Bridge",52.14650,-1.69979),
    ("Stour",0,"Shipston-on-Stour - Fell Mill Footbridge",52.07009,-1.61147),
    ("Stour",0,"Shipston-on-Stour - Mill Bridge",52.06221,-1.62179),
    ("Stour",0,"Stretton-on-Fosse - Above Works",52.04571,-1.67596),
    ("Stour",0,"Stretton-on-Fosse - Below Works",52.04570,-1.67187),
    ("Stour",0,"Whichford - Barrats Hill",52.01751,-1.54473),
    ("Stour",0,"Willington - Willington",52.05100,-1.61400),
    ("Stowe",0,"Napton on the Hill - Hackwell St",52.24711,-1.32029),
    ("Stowe",0,"Napton on the Hill - Howcombe Allotments",52.24592,-1.32475),
    ("Stowe",0,"Napton on the Hill - Lower Fields Farm",52.24391,-1.34783),
    ("Stowe",0,"Napton on the Hill - Sewage Works Footbridge",52.24293,-1.32875),
    ("Stowe",0,"Southam - Footbridge Near Holy Well",52.25204,-1.39681),
    ("Stowe",0,"Southam - Welsh Rd E",52.25136,-1.38333),
    ("Stowe",0,"Stockton - New Zealand Spinney",52.26169,-1.35245),
    ("Stratford-upon-Avon canal",0,"Preston Bagot - Canal",52.28699,-1.74503),
    ("Sutton Brook",0,"Lower Brailes - High St",52.05077,-1.54591),
    ("Sutton Brook",0,"Lower Brailes - New Barn Farm",52.04409,-1.54894),
    ("Swilgate",0,"Elmstone Hardwicke - Lowdilow Ln",51.93879,-2.10959),
    ("Swilgate",0,"Tewkesbury - A38",51.98835,-2.16368),
    ("Swilgate",0,"Tewkesbury - Tewkesbury Nature Reserve Bridge",51.98018,-2.14854),
    ("Swilgate",0,"Tewkesbury - Tirlebrook TNR Bridge",51.99096,-2.14900),
    ("Tributary (Alne River)",0,"Langley - Ford",52.25978,-1.71857),
    ("Tributary (Alne River)",0,"Preston Bagot - Brook",52.28631,-1.74778),
    ("Whitsun Brook",0,"Bishampton - Abberton Rd",52.16810,-2.01511),
    ("Whitsun Brook",0,"Church Lench - Atch Lench Rd Bridge",52.15880,-1.95732),
    ("Whitsun Brook",0,"Low road, Church Lench",52.16841,-1.96037),
    ("Whitsun Brook",0,"Rous Lench Bishampton",52.16985,-1.99032)
]

# STEP 4
#
# Some locations are missing rivers, which means they don't get merged
# We get away with it in some instances where never have a river assigned, but some have a mix
# Here have the location (after synonym match) and then specify the EXACT river case sensitive it is on
MISSING_RIVERS = [
    ("Bredon - Bredon Marina", "Warwickshire Avon"),
    ("Fladbury Paddle Club", "Warwickshire Avon"),
    ("Peopleton - Mill Bridge", "Bow Brook"),
    ("Piddle Brook North of Radford", "Piddle Brook","Piddle Brook North of Radford"),
    ("Bishampton - Abberton Rd", "Whitsun Brook"),
    ("Severn Sailing Club", "Warwickshire Avon"),
    ("piddle brook long lane pinvin","Piddle Brook"),
    ("weston-on-avon - duck ln","Warwickshire Avon"),
    ("fladbury - fladbury paddle club","Warwickshire Avon"),
    ("stratford upon avon by rsc","Warwickshire Avon"),
    ("pershore, leisure centre","Warwickshire Avon"),
    ("twyning quay","Warwickshire Avon"),
    ("Norton Lindsey - Sherbourne Brook","Sherbourne Brook"),
    ("barton - heart of england forest","Warwickshire Avon"),
    ("welford boat station","Warwickshire Avon"),
    ("Stockton - New Zealand Spinney","Stowe"),
    ("rous lench bishampton","Whitsun Brook"),
    ("Snitterfield - Bell Brook, Bell Brook","Bell Brook"),
    ("Norton Lindsey - Sherbourne Brook, Sherbourne Brook","Sherbourne Brook"),
    ("Naunton Beauchamp - Bridge","Piddle Brook"),
    ("low road, church lench","Whitsun Brook"),
    ("church lench bridge","Whitsun Brook"),
    ("carrant back lane beckford","Carrant Brook"),
    ("Lucy's Mill Bridge","Warwickshire Avon"),
    ("alveston - swiffen bank","Warwickshire Avon"),
    ("Chimping Campden Craves","Cam Brook"),
    ("tewkesbury - abbey mill","Warwickshire Avon"),
    ("Ilmington - Middle St","Fosseway Brook"),
    ("Ilmington - Sewage Outflow","Fosseway Brook"),
    ("Avon Smith's Meadow","Piddle Brook"),
    ("Luddington - Avonbank Dr","Warwickshire Avon"),
    ("Great Comberton - Quay Ln","Warwickshire Avon"),
    ("Tewkesbury - Mitton Path","Carrant Brook"),
    ("Langley - Ford","Tributary (Alne River)"),
    ("Preston Bagot - Brook","Tributary (Alne River)"),
    ("Chimping Campden Craves","Cam Brook"),
    ("Clifford Chambers - Mill Bridge","Stour"),
    ("Tiddington - School Ln","Warwickshire Avon"),
    ("Tiddington - Carters Ln","Warwickshire Avon"),
    ("Preston Bagot - Canal","Stratford-upon-avon canal"),
    ("Hampton Lucy - Bridge","Warwickshire Avon"),
    ("Barford - Hampton Wood","Warwickshire Avon"),
    ("Newbold on Stour - Talton Lodge","Stour"),
    ("Snitterfield - Bell Brook","Bell Brook"),
    ("Tewkesbury - Black Bear Pub","Warwickshire Avon"),
    ("Winchombe - Silk Mill Ln","Isbourne"),
    ("210 fladbury, paddle club","Warwickshire Avon"),
    ("Tewkesbury - A38","Swilgate"),
    ("Tewkesbury - Lower Lode Ln","Warwickshire Avon"),
    ("High Street Brailes","Sutton Brook"),
    ("Church Lench - Atch Lench Rd Bridge","Whitsun Brook"),
    ("Tewkesbury - M5 Bridge","Carrant Brook"),
    ("Beckford - Sewage Works","Carrant Brook"),
    ("Beckford - Back Ln","Carrant Brook"),
    ("Mill Stour, Newbold","Stour"),
    ("wyrepiddlebrook","Piddle Brook"),
    ("Piddle Brook Bridge","Piddle Brook")
]


# STEP 5
#
# Locations to exclude, useful if duplicate river name elsewhere in the country!  IN LOWER CASE
# TODO - probably also need to include river at some point?
EXCLUDE_LOCATIONS = ["beeses","conham river park upstream","conham park left pipe","conham river park downstream","priory water","melford park bridge","prysmian beat","stanford meadows","ham bridge","brambridge","st cross mill","durngate bridge","abbots barton","fishermans seat","chilland ford","upper chilland","d/s itchen abbas bridge","below itchen abbas fish farm outfall","bush inn ovington","ovington","armi sampling site opposite itchen stoke mill","water garden upper itchen","borough farm","school bridge","village green","cheriton","cheriton house","fishing bench near stile","marsh cottage","meadow lower","meadow upper","source","itchen culvert","springshot ditch"]


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
DPI = 600
LABELFONTSIZE = 24
TICKFONTSIZE = 16

# ...positions as fraction of figure size
MARGIN_TOP_FRACTION = 0.995
MARGIN_BOTTOM_FRACTION = 0.11
MARGIN_LEFT_FRACTION = 0.08
MARGIN_RIGHT_FRACTION = (1 - MARGIN_LEFT_FRACTION)

YAXIS_LABEL_SPACING = 0.5
TICK_LABEL_SPACING = 0.5
SPACE_BETWEEN_SUBPLOTS = 0.1

BAR_WIDTH = 5