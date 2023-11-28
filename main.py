import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

st.title("Geo-Visualization of Uber Trips")

data = pd.read_csv('/Users/lukekerwin/Library/CloudStorage/OneDrive-ThePennsylvaniaStateUniversity/School/DS 330/DS-330-Project/UberDatasetFiltered.csv')
# START_DATE,END_DATE,CATEGORY,START,STOP,MILES,PURPOSE,START_STATE,STOP_STATE,START_LOC,STOP_LOC,START_LAT,START_LONG,STOP_LAT,STOP_LONG
data.columns = ['START_DATE', 'END_DATE', 'CATEGORY', 'START', 'STOP', 'MILES', 'PURPOSE', 'START_STATE', 'STOP_STATE', 'START_LOC', 'STOP_LOC', 'LAT', 'LON', 'STOP_LAT', 'STOP_LONG']


pages = ['New York City', 'Texas', 'North Carolina']

page_select = st.sidebar.selectbox('Select a location', pages)

# Data Filters
# Purpose
purpose = st.sidebar.multiselect('Select a purpose', data['PURPOSE'].unique())

# Category
category = st.sidebar.multiselect('Select a category', data['CATEGORY'].unique())


if page_select == 'New York City':
    st.subheader('New York City')
    filt_data = data[data['START_STATE'] == 'New York']

    # Purpose Filter
    if purpose:
        filt_data = filt_data[filt_data['PURPOSE'].isin(purpose)]
    
    # Category Filter
    if category:
        filt_data = filt_data[filt_data['CATEGORY'].isin(category)]

    map_center = [filt_data['LAT'].mean(), filt_data['LON'].mean()]
    
    map = folium.Map(location=map_center, zoom_start=10)
    marker_cluster = MarkerCluster().add_to(map)
    for index, row in filt_data.iterrows():
        folium.Marker([row['LAT'], row['LON']], popup=row['PURPOSE']).add_to(marker_cluster)
    st_folium(map, width=1200, height=600)


if page_select == 'Texas':
    st.subheader('Texas')
    filt_data = data[data['START_STATE'] == 'Texas']

    # Purpose Filter
    if purpose:
        filt_data = filt_data[filt_data['PURPOSE'].isin(purpose)]
    
    # Category Filter
    if category:
        filt_data = filt_data[filt_data['CATEGORY'].isin(category)]

    map_center = [filt_data['LAT'].mean(), filt_data['LON'].mean()]

    map = folium.Map(location=map_center, zoom_start=8)
    marker_cluster = MarkerCluster().add_to(map)
    for index, row in filt_data.iterrows():
        folium.Marker([row['LAT'], row['LON']], popup=row['PURPOSE']).add_to(marker_cluster)
    st_folium(map, width=1200, height=600)

if page_select == 'North Carolina':
    st.subheader('North Carolina')
    filt_data = data[data['START_STATE'] == 'North Carolina']

    # Purpose Filter
    if purpose:
        filt_data = filt_data[filt_data['PURPOSE'].isin(purpose)]
    
    # Category Filter
    if category:
        filt_data = filt_data[filt_data['CATEGORY'].isin(category)]

    map_center = [filt_data['LAT'].mean(), filt_data['LON'].mean()]

    map = folium.Map(location=map_center, zoom_start=10)
    marker_cluster = MarkerCluster().add_to(map)
    for index, row in filt_data.iterrows():
        folium.Marker([row['LAT'], row['LON']], popup=row['PURPOSE']).add_to(marker_cluster)
    st_folium(map, width=1200, height=600)