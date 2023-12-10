import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

st.title("Visualization of Uber Trips")

data = pd.read_csv('UberDatasetFiltered.csv')
# START_DATE,END_DATE,CATEGORY,START,STOP,MILES,PURPOSE,START_STATE,STOP_STATE,START_LOC,STOP_LOC,START_LAT,START_LONG,STOP_LAT,STOP_LONG
data.columns = ['START_DATE', 'END_DATE', 'CATEGORY', 'START', 'STOP', 'MILES', 'PURPOSE', 'START_STATE', 'STOP_STATE', 'START_LOC', 'STOP_LOC', 'LAT', 'LON', 'STOP_LAT', 'STOP_LONG']


pages = ['New York City', 'Texas', 'North Carolina']

page_select = st.sidebar.selectbox('Select a location', pages)

# Data Filters
# Purpose
purpose = st.sidebar.multiselect('Select a purpose', data['PURPOSE'].unique())

# Category
category = st.sidebar.multiselect('Select a category', data['CATEGORY'].unique())

# Subheader
st.subheader('Map of Trips')

if page_select == 'New York City':
    st.subheader('New York City')
    filt_data = data[data['START_STATE'] == 'New York']

    # Purpose Filter
    if purpose:
        filt_data = filt_data[filt_data['PURPOSE'].isin(purpose)]
    
    # Category Filter
    if category:
        filt_data = filt_data[filt_data['CATEGORY'].isin(category)]

    map_center = [40.7128, -74.0060]
    
    map = folium.Map(location=map_center, zoom_start=10)


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

st.subheader('Time Popularity')

# Display heatmap of the most popular times
copy = filt_data.copy()
copy['START_DATE'] = pd.to_datetime(copy['START_DATE'])
copy['DAY'] = copy['START_DATE'].dt.day_name()
copy['HOUR'] = copy['START_DATE'].dt.hour

# Create a new dataframe with the start and end times
times = copy[['DAY', 'HOUR']].copy()

# Create a heatmap of the times using matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
fig = plt.figure(figsize=(12, 6))
sns.heatmap(times.groupby(['DAY', 'HOUR']).size().unstack(), cmap='Reds')
st.pyplot(fig)

# Create a Dendrogram of the trip reasons
st.subheader('Dendrogram of Trip Reasons (Does Not Get Filtered)')

# embed image

st.image('Dendrogram.png', width=1200)


