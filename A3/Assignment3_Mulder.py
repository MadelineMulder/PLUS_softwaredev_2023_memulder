#!/usr/bin/env python
# coding: utf-8

# # Step 1: Import Packages

# In[9]:


import folium
import pandas as pd
import os


# # Step 2: Create Data

# In[2]:


# create a dataframe with fake data on the location, timing, and severity of hurricanes in Grand Bahama Island
data = pd.DataFrame({
    'lon': [-78.75, -78.50, -78.49, -78.58, -78.64, -78.50],
    'lat': [26.51, 26.61, 26.57,26.53,26.57, 26.66],
    'name': ['Apple', 'Banana', 'Corn', 'Dad', 'Elephant', 'Frangipan'],
    'year': [1953, 1987, 1999, 2001, 2015, 2017],
    'severity': [5, 1, 2, 1, 4, 1]
}, dtype=str) 

data


# # Step 3: Create Map

# In[3]:


# create a basic web map of the study area (Grand Bahama Island) using folium with some basic styling
m = folium.Map(location=[26.533319, -78.647118],zoom_start=10,tiles='Stamen toner' )
m


# # Step 4: Create Bubble Map 

# In[4]:


# Cycle through the dataframe create earlier and create a circle for each hurricane that shows its location and severity 
# by means of the size and color of the circle
# Scale: yellow for severity level of 1, orange for severity level of 2 or 3, red for severity level of 4 or 5
for i in range(0,len(data)):
    severityStr = data.iloc[i]['severity']
    if severityStr == "1" : clr = '#FAD02C'
    elif severityStr == "2"or severityStr == "3": clr = '#F89700'
    elif severityStr == "4" or severityStr == "5":clr = '#FF2511'
    folium.CircleMarker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
      radius=float(data.iloc[i]['severity']*2),
      color= clr,
      fill=True,
      fill_color= clr
   ).add_to(m)
m


# # Step 5: Style Map

# In[5]:


# Access country borders data to add the map using a url to a geojson
political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)


# In[6]:


# make the borders pop with a red dash style
bordersStyle = {
    'color': 'red',
    'weight': 1,
    'dashArray': 4 ,
    'fillColor': 'gray',
    'fillOpacity': 0.1
}


# In[7]:


# Add the borders with their styling to the map 
folium.GeoJson(political_countries_url, name = "countries", style_function = lambda x: bordersStyle).add_to(m)
m


# # Step 6: Add A Marker

# In[8]:


# Add a marker to signal where there is a flood on the island
marker_location = [26.533319, -78.647118]
tooltip = "Flood Hazard Alert"
popup = "<b>HAZARD!</b>"

folium.Marker(
    marker_location, popup=popup, tooltip=tooltip, icon=folium.Icon(color="blue", icon="glyphicon-warning-sign")
).add_to(m)
m


# # Step 7: Export the Web Map

# In[13]:


# Set output directory where you want to store the link to the web map
output_directory = "C:\\Users\\madel\\Desktop"

# Check that you are accessing a real directory
print("this path is real:", os.path.isdir(output_directory))

# Define a filename for the map
html_name = "bahamas.html"

# Join the parts to create a path to save the map to
output_path = os.path.join(output_directory, html_name)


# In[14]:


# Save the map to the path defined earlier 
m.save(output_path)


# Adapted from: https://nagasudhir.blogspot.com/2021/08/create-bubble-map-from-excel-data-using.html https://www.python-graph-gallery.com/313-bubble-map-with-folium?utm_content=cmp-true#google_vignette
