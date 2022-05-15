import folium
from data_cleaning import *

# good condition meteorites
found_valid_df = correct_lat_long_df[correct_lat_long_df['nametype'] == 'Valid']
# withered condition meteorites
found_relict_df = correct_lat_long_df[correct_lat_long_df['nametype'] == 'Relict']

def display_meteorites_withered_condition():
    first_map = folium.Map(location = [0,0], tiles = 'Stamen Terrain', zoom_start = 1)
    for i in found_relict_df.index:
        folium.Marker(location = [found_relict_df.loc[i, 'reclat'], found_relict_df.loc[i, 'reclong']], popup = found_relict_df.loc[i, 'name']).add_to(first_map)
    return first_map

def display_meteorites_good_condition_after_2010():
    second_map = folium.Map(location = [0,0], tiles = 'Stamen Terrain', zoom_start = 1)
    for i in found_valid_df[found_valid_df['year'] > 2010].index:
        folium.Marker(location = [found_valid_df.loc[i, 'reclat'], found_valid_df.loc[i, 'reclong']], popup = found_valid_df.loc[i, 'name']).add_to(second_map)
    return second_map


def display_meteorites_good_condition_2008_to_2010():
    third_map = folium.Map(location = [0,0], tiles = 'Stamen Terrain', zoom_start = 1)
    for i in found_valid_df[(found_valid_df['year'] > 2007) & (found_valid_df['year'] < 2011)].index:
        folium.Marker(location = [found_valid_df.loc[i, 'reclat'], found_valid_df.loc[i, 'reclong']], popup = found_valid_df.loc[i, 'name']).add_to(third_map)
    return third_map

def display_meteorites_good_condition_2005_to_2007_with_circular_marker():
    fourth_map = folium.Map(location = [0,0], tiles = 'Stamen Terrain', zoom_start = 1)
    for i in correct_lat_long_df[(correct_lat_long_df['nametype'] == 'Valid') & (correct_lat_long_df['year'] > 2004) & (correct_lat_long_df['year'] < 2008) & (correct_lat_long_df['fall'] == 'Found')].index:
        folium.CircleMarker(location = [found_valid_df.loc[i, 'reclat'], found_valid_df.loc[i, 'reclong']], popup = ((found_valid_df.loc[i, 'name'] + str(found_valid_df.loc[i, 'mass']/1000)) + ' kg'), radius = found_valid_df.loc[i, 'mass'] / 1000000).add_to(fourth_map)
    return fourth_map


display_meteorites_good_condition_2005_to_2007_with_circular_marker()