#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
This is a script that demonstrates various geospatial functionalities related to map visualization and routing calculation.

Author: Madeline Mulder
Date: June 18, 2023

Usage:
    python geofunctions.py

Description:
    This script contain several functions that perform several operations based on user input and generates maps and distance calculations.

    It supports the following operations:
    - Map creation
    - Data visualization
    - Statistical calculations
    - User input

Examples:
    1. Create a folium map and define map coordinate, zoom level, and tile type:
        geofunctions.create_map()

    2. Draw a polygon on a folium map:
        geofunctions.add_polygon_to_map(m)
        
    2. Add a shapefile to a folium map:
        geofunctions.add_polygon_to_map(m, 'path\\polygon.shp')
        
    2. Calculate the geodesic distance between user-defined points:
        geofunctions.user_routing()
"""


# ## Install Packages

# In[2]:


import geopandas as gpd
import folium
from folium.plugins import Draw
import geopy


# ## Function 1: Create A Map

# In[9]:


def create_map():
    """
    Creates a custom Folium map based on user input.

    Returns:
        folium.Map: Custom map with user-specified location, zoom level, and tile style.
    """
    def user_input():
        """
        Allows user to input their own coordinates for the map.

        Returns:
            list: User-specified latitude and longitude as a list.
        """
        y = float(input("Enter latitude: "))
        x = float(input("Enter longitude: "))
        location = [y,x]
        return location

    
    def zoom_level():
        """
        Allows user to choose their own zoom level for the map.

        Returns:
            int: User-specified zoom level.
        """
        scale = int(input("Enter zoom level: "))
        return scale
         
    
    def tile_style():
        """
        Allows user to choose their own tile style for the map.

        Returns:
            str: User-specified tile style.
        """
        tile = str(input("Enter desired tile type: "))
        return tile

    
    def create_custom_map(location, zoom_start, tile_style):
        
        """
        Create a Folium map centered at the user-specified location.

        Args:
            location (list): Latitude and longitude coordinates as [latitude, longitude].
            zoom_start (int): Zoom level for the map.
            tile_style (str): Tile style for the map.

        Returns:
            folium.Map: Custom map with the specified location, zoom level, and tile style.
        """
        
        # Create a Folium map centered at the specified location
        custom_map = folium.Map(location=location, zoom_start=zoom_start, control_scale=True)

        # Add the selected tile layer to the map
        tile_layer = folium.TileLayer(tile_style=tile_style).add_to(custom_map)
        tile_layer.control = False

        # Add interactive addition to the map (allow users to place markers with their coordinates on the map)
        folium.ClickForMarker("<b>Latitude:</b> ${lat}<br /><b>Longitude:</b> ${lng}").add_to(custom_map)

        # Return the custom map
        return custom_map
    
    #Use the user inputs from earlier functions as arguments for the creating a map function 
    user_location = user_input()
    user_zoom = zoom_level()
    tile = tile_style()
    user_map = create_custom_map(user_location, user_zoom, tile)
   
    return user_map 


# ## Function two: Add A Polygon to the Map

# In[10]:


def add_polygon_to_map(m, shapefile_path=None):
    """
    Adds a user-drawn polygon to the map and optionally loads a shapefile. Includes possibility to export drawn polygon as a geojson

    Args:
        m (folium.Map): Map object to which the polygon drawing and shapefile will be added.
        shapefile_path (str, optional): Path to a shapefile to be loaded and displayed on the map. Default is None.

    Returns:
        folium.Map: Map object with the polygon drawing control and, if provided, the loaded shapefile added.
    """
    # Add draw control to the map so that a user can draw a polygon on the map
    draw_control = Draw(export=True)
    m.add_child(draw_control)
    # If a shapefile path is provided, load the shapefile and add it to the map
    if shapefile_path:
        data = gpd.read_file(shapefile_path)
        m.add_child(folium.GeoJson(data))

    # Return the updated map
    return m


# ## Funcation Three: A Simple Routing Distance Calculator

# In[15]:


from geopy.distance import geodesic


def user_routing():
    """
     Calculates the geodesic distance between two user-specified locations for a routing scenario.
     
     Returns:
         Float: Geodesic distance between two points in kilometers
     """
    
    def start_location():
        """
        Allows user to input their own start coordinates for the route.

        Returns:
            tuple: Start location coordinates as (longitude, latitude).
        """
        y = float(input("Enter starting point latitude: "))
        x = float(input("Enter starting point longitude: "))
        location_start = (x,y)
        return location_start

    def end_location():
        """
        Allows user to input their own end coordinates for the route.

        Returns:
            tuple: End location coordinates as (longitude, latitude).
        """
        y = float(input("Enter end point latitude: "))
        x = float(input("Enter end point longitude: "))
        location_end = (x,y)
        return location_end

    def simple_routing(start_location, end_location):
        """
        Calculates the distance between the start and end locations.

        Args:
            start_location (tuple): Start location coordinates as (longitude, latitude).
            end_location (tuple): End location coordinates as (longitude, latitude).

        Returns:
            None
        """
        
        # Calculate the distance between the start and end locations
        distance = round(geodesic(start_location, end_location).km, 2)

        # print route distance
        print('Route Distance: {} KM'.format(distance))
    
    start = start_location()
    end = end_location()
    routing = simple_routing(start, end)
    
    # Return the total route distance
    return routing


# In[ ]:




