# Parse raw exported sample data from epicollect into graphs for use
# within a kml file including output of individual tidied .csv files.
# Different river synonyms and placenames are grouped together during
# this process.
#
# R. Hunt
# richard@cooljacketcoding.co.uk

import os
import sys
import csv
from collections import defaultdict
from collections import namedtuple
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from datetime import datetime, timedelta, timezone
import numpy as np
import importlib

# Set to 1 for one-off test
TEST = 0

# If non-zero, disregard any data that doesn't have anything in this many weeks
ACTIVE_WEEKS_TIME = 0

# If non-zero, colour markers blue (i.e. leave natural) to show old
SHOW_AGED_WEEKS_TIME = 5

# Otherwise use these links depending whether one or both over threshold
RED_MARKER = "<Style><IconStyle><Icon><href>http://maps.google.com/mapfiles/kml/paddle/red-circle.png</href></Icon></IconStyle></Style>"
YELLOW_MARKER = "<Style><IconStyle><Icon><href>http://maps.google.com/mapfiles/kml/paddle/ylw-circle.png</href></Icon></IconStyle></Style>"
GREEN_MARKER = "<Style><IconStyle><Icon><href>http://maps.google.com/mapfiles/kml/paddle/grn-circle.png</href></Icon></IconStyle></Style>"
BLUE_MARKER = "<Style><IconStyle><Icon><href>http://maps.google.com/mapfiles/kml/paddle/blu-circle.png</href></Icon></IconStyle></Style>"


cfg = None

# INTERNAL DATE
###############

SampleEntry = namedtuple('SampleEntry', 'name date river place latitude longitude accuracy northing easting utmzone location_description time river_height river_flow weather recent_rain reading_conductivity reading_temperature reading_phosphates reading_nitrates reading_ammonia reading_algal_blooms reading_pollution reading_notes')

sampling_data = defaultdict(list)


# FUNCTIONS FOR PLOTTING
########################

# Define a function to calculate global min and max values
def calculate_global_limits(sampling_data):
    conductivity_min, conductivity_max = float('inf'), float('-inf')
    phosphates_min, phosphates_max = float('inf'), float('-inf')
    nitrates_min, nitrates_max = float('inf'), float('-inf')
    ammonia_min, ammonia_max = float('inf'), float('-inf')
    temperature_min, temperature_max = float('inf'), float('-inf')
    min_date, max_date = datetime.max, datetime.min

    for river, data in sampling_data.items():
        reading_conductivity = [entry.reading_conductivity for entry in data]
        reading_phosphates = [entry.reading_phosphates for entry in data]
        reading_nitrates = [entry.reading_nitrates for entry in data]
        reading_ammonia = [entry.reading_ammonia for entry in data]
        reading_temperature = [entry.reading_temperature for entry in data]
        dates = [datetime.strptime(entry.date, '%d/%m/%Y') for entry in data]

        conductivity_min = min(conductivity_min, *reading_conductivity)
        conductivity_max = max(conductivity_max, *reading_conductivity)

        phosphates_min = min(phosphates_min, *reading_phosphates)
        phosphates_max = max(phosphates_max, *reading_phosphates)

        nitrates_min = min(nitrates_min, *reading_nitrates)
        nitrates_max = max(nitrates_max, *reading_nitrates)

        ammonia_min = min(ammonia_min, *reading_ammonia)
        ammonia_max = max(ammonia_max, *reading_ammonia)

        temperature_min = min(temperature_min, *reading_temperature)
        temperature_max = max(temperature_max, *reading_temperature)

        min_date = min(min_date, *dates)
        max_date = max(max_date, *dates)

    return (conductivity_min, conductivity_max,
            phosphates_min, phosphates_max,
            nitrates_min, nitrates_max,
            ammonia_min, ammonia_max,
            temperature_min, temperature_max,
            min_date, max_date)


# Define a function to create the plots for each location
def plot_river_data(location, data, global_limits):

    # Extract data for the location, clipping conductivity data
    dates = [mdates.date2num(datetime.strptime(entry.date, '%d/%m/%Y')) for entry in data]
    reading_conductivity = [min(entry.reading_conductivity, cfg.MAX_CONDUCTIVITY) for entry in data]
    reading_phosphates = [entry.reading_phosphates for entry in data]
    reading_nitrates = [entry.reading_nitrates for entry in data]
    reading_ammonia = [entry.reading_ammonia for entry in data]
    reading_temperature = [entry.reading_temperature for entry in data]

    # Unpack global limits
    conductivity_min, conductivity_max, phosphates_min, phosphates_max, nitrates_min, nitrates_max, ammonia_min, ammonia_max, temperature_min, temperature_max, min_date, max_date = global_limits

    # Limit conductivity axis
    if conductivity_max > cfg.MAX_CONDUCTIVITY:
        conductivity_max = cfg.MAX_CONDUCTIVITY

    if temperature_max > cfg.MAX_TEMPERATURE_C:
        temperature_max = cfg.MAX_TEMPERATURE_C

    if phosphates_max > cfg.MAX_PHOSPHATES:
        phosphates_max = cfg.MAX_PHOSPHATES

    if nitrates_max > cfg.MAX_NITRATES:
        nitrates_max = cfg.MAX_NITRATES

    # Create a figure and subplots (optimize for small size)
    fig, axs = plt.subplots(2, 1, figsize=(cfg.FIG_SIZE_X_INCHES, cfg.FIG_SIZE_Y_INCHES), dpi=600, sharex=True)

    # Set the font size in pixels (roughly equivalent to 16 pixels)
    label_fontsize = 8 * (72.27 / fig.dpi)  # Convert 16 pixels to relative fontsize
    tick_fontsize = 7 * (72.27 / fig.dpi)

    # Define the bar plots for each reading and temperature
    def create_subplot(ax, y_values, y_label, min_y, max_y, threshold_y, colour_y, y2_values, y2_label, min_y2, max_y2, threshold_y2, colour_y2):

        offset_dates = [(date + cfg.BAR_WIDTH) for date in dates]

        # Primary y-axis: plot the main reading
        ax.bar(dates, y_values, color=colour_y, width=cfg.BAR_WIDTH, label=y_label)
        ax.set_ylabel(y_label, fontsize=label_fontsize, labelpad=cfg.YAXIS_LABEL_SPACING)
        ax.set_ylim(min_y, max_y)
        ax.tick_params(axis='both', which='major', labelsize=tick_fontsize, width=0.1, length=1, pad=cfg.TICK_LABEL_SPACING)

        # Secondary y-axis: plot the temperature as bars
        ax_twin = ax.twinx()
        ax_twin.bar(offset_dates, y2_values, color=colour_y2, width=cfg.BAR_WIDTH, label=y2_label)
        ax_twin.set_ylabel(y2_label, fontsize=label_fontsize, labelpad=cfg.YAXIS_LABEL_SPACING)
        ax_twin.set_ylim(min_y2, max_y2)
        ax_twin.tick_params(axis='y', labelsize=tick_fontsize, width=0.1, length=1, pad=cfg.TICK_LABEL_SPACING)

        # Thresholds
        if (threshold_y != 0):
            ax.axhline(y=threshold_y, color=colour_y, linestyle='dotted', linewidth=0.25)

        if (threshold_y2 != 0):
            ax_twin.axhline(y=threshold_y2, color=colour_y2, linestyle='dotted', linewidth=0.25)

        # Legends for both y-axes
        ax.legend(loc='upper left', fontsize=label_fontsize)
        ax_twin.legend(loc='upper right', fontsize=label_fontsize)

        # Format x-axis ticks
        ax.set_xticks(dates)
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
        ax.xaxis.set_major_locator(mdates.MonthLocator())  # Major ticks every month
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.set_xlim(min_date, max_date)
        ax.xaxis.set_tick_params(width=0.1, length=1, pad=cfg.TICK_LABEL_SPACING)
        for spine in ax.spines.values():
            spine.set_linewidth(0.1)
        for spine in ax_twin.spines.values():
            spine.set_linewidth(0.1)

    # Subplots
    create_subplot(axs[0], reading_conductivity, 'Conductivity uS/cm', conductivity_min, conductivity_max, cfg.THRESHOLD_CONDUCTIVITY, 'orange',
                   reading_ammonia, 'Ammonia ppm', ammonia_min, ammonia_max, cfg.THRESHOLD_AMMONIA, 'lightblue');

    create_subplot(axs[1], reading_phosphates, 'Phosphates ppm', phosphates_min, phosphates_max, cfg.THRESHOLD_PHOSPHATES, 'red',
                   reading_nitrates, 'Nitrates ppm', nitrates_min, nitrates_max, cfg.THRESHOLD_NITRATES, 'blue');

    # Margins around all plots
    plt.subplots_adjust(left=cfg.MARGIN_LEFT_FRACTION, right=cfg.MARGIN_RIGHT_FRACTION, top=cfg.MARGIN_TOP_FRACTION, bottom=cfg.MARGIN_BOTTOM_FRACTION, hspace=cfg.SPACE_BETWEEN_SUBPLOTS)

    fig.suptitle(f'{location}', fontsize=label_fontsize, fontweight='bold')

    # Save the figure as a PNG file with the location name
    filename = cfg.OUTPUT_FOLDER + '/' + location.replace('/','_')
    plt.savefig(f'{filename}.png', bbox_inches='tight', pad_inches=0)

    if TEST == 1:
        plt.show()

    plt.close()


# FILE HANDLING
###############
def read_river_data(csv_file):
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        # Extract information from row on spreadsheet
        for row in reader:
            if cfg.COL_RIVER == None:
                one_for_us = True
                river = None
            else:
                one_for_us = False
                river = row[cfg.COL_RIVER].lower().strip()
                river_cleaned_up = river.lower().strip()
                for river_name_set in cfg.RIVER_NAMES:
                    for river_name_monitoring in river_name_set:
                        if river_name_monitoring.lower().strip() == river_cleaned_up:
                            one_for_us = True
                            river = river_name_set[0]
                            break

            if one_for_us:
                location_description = '' if cfg.COL_DESCRIPTION == None else row[cfg.COL_DESCRIPTION]
                name = row[cfg.COL_NAME]
                date = row[cfg.COL_DATE]
                place = row[cfg.COL_PLACE]
                latitude = float(row[cfg.COL_LAT]) if row[cfg.COL_LAT] else None
                longitude = float(row[cfg.COL_LONG]) if row[cfg.COL_LONG] else None
                accuracy = int(row[cfg.COL_ACCURACY]) if row[cfg.COL_ACCURACY] else None
                northing = int(row[cfg.COL_NORTHING]) if row[cfg.COL_NORTHING] else None
                easting = int(row[cfg.COL_EASTING]) if row[cfg.COL_EASTING] else None
                utmzone = row[cfg.COL_UTMZONE]
                time = row[cfg.COL_TIME]
                river_height = row[cfg.COL_RIVER_HEIGHT]
                river_flow = '' if cfg.COL_RIVER_FLOW == None else row[cfg.COL_RIVER_FLOW]
                weather = '' if cfg.COL_WEATHER == None else row[cfg.COL_WEATHER]
                recent_rain = '' if cfg.COL_RECENT_RAIN == None else row[cfg.COL_RECENT_RAIN]
                reading_conductivity = float(row[cfg.COL_CONDUCTIVITY]) if row[cfg.COL_CONDUCTIVITY] else 0
                reading_temperature = float(row[cfg.COL_TEMPERATURE]) if row[cfg.COL_TEMPERATURE] else 0
                reading_phosphates = float(row[cfg.COL_PHOSPHATES]) if row[cfg.COL_PHOSPHATES] else 0
                reading_nitrates = float(row[cfg.COL_NITRATES]) if row[cfg.COL_NITRATES] else 0
                if cfg.COL_AMMONIA == None:
                    reading_ammonia = 0
                else:
                    reading_ammonia = float(row[cfg.COL_AMMONIA]) if row[cfg.COL_AMMONIA] else 0
                reading_algal_blooms = '' if cfg.COL_ALGAL_BLOOMS == None else row[cfg.COL_ALGAL_BLOOMS]
                reading_pollution = '' if cfg.COL_POLLUTION == None else row[cfg.COL_POLLUTION]
                reading_notes = row[cfg.COL_NOTES]

                # Pre-process input placename to map any incorrect spellings
                place = place.strip()
                for synonym in cfg.SYNONYMS:
                    for variant in synonym:
                        if place.lower().startswith(variant.lower()):
                            place = synonym[0]
                            break

                # And now look to see if we map to a specific location
                place_split = place.split()
                if place_split[0].isdigit():
                    # An 'official' location so override name and lat/long from our record for consistency
                    place_number = int(place_split[0])
                    for entry in cfg.SAMPLING_LOCATIONS:
                        if (entry[0] == river) and (entry[1] == place_number):
                            place = entry[2]
                            latitude = entry[3]
                            longitude = entry[4]
                            break
                else:
                    for entry in cfg.SAMPLING_LOCATIONS:
                        if (place == entry[2]):
                            latitude = entry[3]
                            longitude = entry[4]
                            break

                # Store processed sample
                location = place if river == None else river + ', ' + place
                sample_entry = SampleEntry(
                    name, date, river, place, latitude, longitude, accuracy, 
                    northing, easting, utmzone, location_description, time, river_height, river_flow, 
                    weather, recent_rain, reading_conductivity, reading_temperature, 
                    reading_phosphates, reading_nitrates, reading_ammonia, reading_algal_blooms, 
                    reading_pollution, reading_notes
                )
                sampling_data[location].append(sample_entry)

def main():

    # Read in data and find largest range so can be common across all graphs
    print('Reading in river data')
    read_river_data(cfg.INPUT_CSV_FILENAME)
    global_limits = calculate_global_limits(sampling_data)
    active_list = defaultdict(list)
    bad_quality_list = defaultdict(list)

    # Create the graphs of all sampling locations
    print('Creating graphs')
    if TEST == 1:
        location, data = next(iter(sampling_data.items()))
        plot_river_data(location, data, global_limits)
    else:
        for location, data in sampling_data.items():
            # Check if active
            is_active = False
            most_recent_weeks_ago = 0
            most_recent_sample_seconds_ago = 0
            bad_quality_list[location] = -1
            for sample_entry in data:
                timestamp = datetime.strptime(sample_entry.date, "%d/%m/%Y").replace(tzinfo=timezone.utc)
                now = datetime.now(timezone.utc)
                time_ago_seconds = (now - timestamp).total_seconds()
                weeks_difference = time_ago_seconds / (7 * 24 * 60 * 60)
                if ((0 == ACTIVE_WEEKS_TIME) or (weeks_difference <= ACTIVE_WEEKS_TIME)):
                    is_active = True
                    if (0 == SHOW_AGED_WEEKS_TIME) or (weeks_difference <= SHOW_AGED_WEEKS_TIME):
                        if (0 == most_recent_sample_seconds_ago) or (time_ago_seconds < most_recent_sample_seconds_ago):
                            most_recent_sample_seconds_ago = time_ago_seconds
                            bad_quality = 0
                            if sample_entry.reading_conductivity >= cfg.THRESHOLD_CONDUCTIVITY:
                                bad_quality += 1
                            if sample_entry.reading_phosphates >= cfg.THRESHOLD_PHOSPHATES:
                                bad_quality += 1
                            if sample_entry.reading_nitrates >= cfg.THRESHOLD_NITRATES:
                                bad_quality += 1
                            if sample_entry.reading_ammonia >= cfg.THRESHOLD_AMMONIA:
                                bad_quality += 1
                            bad_quality_list[location] = bad_quality
                if (0 == most_recent_weeks_ago):
                    most_recent_weeks_ago = weeks_difference
                else:
                    if weeks_difference < most_recent_weeks_ago:
                        most_recent_weeks_ago = weeks_difference
            
            if (is_active):
                active_list[location] = most_recent_weeks_ago
                print (location + f" - sampled {most_recent_weeks_ago:.1f} weeks ago")
                plot_river_data(location, data, global_limits)
            else:
                print (location + f" - INACTIVE ({most_recent_weeks_ago:.1f} weeks ago)")

    # Create a kml file to reference the above from
    print('Generating Google Earth .kml file')
    num_graphs = 0
    num_added_to_kml = 0
    with open(cfg.OUTPUT_FOLDER + '/river_overview.kml', 'w') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        file.write('  <Document>\n')
        file.write('    <name>River sampling results</name>\n')
        for location, data in sampling_data.items():
            if location in active_list:
                for sample in data:
                    latitude = sample[4]
                    longitude = sample[5]
                    if latitude != None and longitude != None:
                        break
                num_graphs += 1
                filename = location.replace('/','_')
                if latitude != None and longitude != None:
                    bad_quality = bad_quality_list[location]
                    file.write('        <Placemark>\n')
                    if (0 == bad_quality):
                        file.write(GREEN_MARKER)
                    if (1 == bad_quality):
                        file.write(YELLOW_MARKER)
                    elif (bad_quality >= 2):
                        file.write(RED_MARKER)
                    else:
                        file.write(BLUE_MARKER)
                    file.write('          <name></name>\n')
                    file.write('          <description><![CDATA[\n')
                    file.write('            <img src="' + filename + '.png" alt="' + filename + '" width="594" height="446">\n')
                    file.write('          ]]></description>\n')
                    file.write('          <Point>\n')
                    file.write('            <coordinates>' + str(longitude) + ',' + str(latitude) + ',0</coordinates>\n')
                    file.write('          </Point>\n')
                    file.write('        </Placemark>\n')
                    num_added_to_kml += 1
                else:
                    print('No location for '+location);
        file.write('  </Document>\n')
        file.write('</kml>\n')
    print('Created ' + str(num_graphs) + ' graphs and linked ' + str(num_added_to_kml) + ' into kml file')

    # Output cleaned csv
    print('Generating .csv files')
    for location, data in sampling_data.items():
        filename = cfg.OUTPUT_FOLDER + '/' + location.replace('/','_') + '.csv'
        with open(filename, 'w') as file:
            file.write('name,date,river,place,latitude,longitude,accuracy,location_description,time,river_height,river_flow,weather,recent_rain,reading_conductivity,reading_temperature,reading_phosphates,reading_nitrates,reading_ammonia,reading_algal_blooms,reading_pollution,reading_notes\n')
            for sample in data:
                # exclude northing, easting, and utmzone present in sample tuple, add quotes to place and reading notes
                filtered_entry = sample[:3] + (f'"{sample[3]}"',) + sample[4:7] + (f'"{sample[10]}"',) + sample[11:-1] + (f'"{sample[-1]}"',)
                file.write(','.join(map(str, filtered_entry)) + '\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_epicollect.py <cfg_file>")
    else:
        module_name = sys.argv[1]
        try:
            cfg = importlib.import_module(module_name)
            print(f"Using configuration {module_name}")
            main()
        except ModuleNotFoundError:
            print(f"Module '{module_name}' not found.")
        except AttributeError as e:
            print(f"Attribute error: {e}")
