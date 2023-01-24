# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:36:29 2023

@author: jc343421
"""


import geopandas

areas_pakistan = geopandas.read_file("../data/pakistan_districts/pakistan_districts.shp")

result = areas_pakistan.explore(column='cartodb_id', tooltip=["districts","cartodb_id"])

result.save("interactive_pakistan.html")
