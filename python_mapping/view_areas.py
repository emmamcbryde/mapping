# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:06:49 2022

@author: jc942017
"""
import os
absolute_path = os. getcwd()
#relative_path = "src/lib"
#full_path = os.path.join(absolute_path, relative_path)
import geopandas
#import geoplot
import pandas as pd
#import mapclassify
#import matplotlib.pyplot as plt
#import folium
area_info = pd.read_csv("../data/synopsis_and_latent_variable.csv")
area_info["analysis_unit"] = area_info["analysis_unit"].str[4:]
area_info = area_info.rename(columns = {"analysis_unit": "IAR_CODE16"})

areas = geopandas.read_file("../data/1270055002_iare_2016_aust_shape/IARE_2016_AUST.shp")
is_in_areas = area_info["IAR_CODE16"].isin(areas["IAR_CODE16"])
# find the locations that have additional a or b after them
invalid_locations = area_info[~is_in_areas]
#truncate their names back to the number only
invalid_locations["IAR_CODE16"] = invalid_locations["IAR_CODE16"].str[:-1]
# get the mean and mean
merged_rows = invalid_locations.groupby("IAR_CODE16").mean().reset_index()
# return these to the group through concatenation
area_info = pd.concat([area_info, merged_rows])

iar_areas = areas.merge(area_info, on="IAR_CODE16")

result = iar_areas.explore(column='latent_v_community', tooltip=["IAR_NAME16","latent_v_community"])

result.save("interactive.html")

