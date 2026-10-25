import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

st.set_page_config(layout="wide")
st.title("🏙️ Karachi 3D District Population Density Model")
st.write(
    "This interactive 3D map uses PyDeck columns to visualize localized density metrics across urban zones."
)

# 1. Generate geospatial mock data centered around Karachi coordinates
chart_data = pd.DataFrame(  {
        "District": [
            "Saddar (Downtown)",
            "Clifton / DHA",
            "Orangi Town",
            "Gulshan-e-Iqbal",
            "Nazimabad",
            "Malir",
        ],
        "latitude": [24.8605, 24.8138, 24.9525, 24.9180, 24.9128, 24.8920],
        "longitude": [67.0261, 67.0481, 66.9650, 67.0971, 67.0315, 67.1950],
        # Density metric scales the height of the 3D columns
        "Density_Metric": [4500, 2100, 5800, 3900, 4800, 1800],
    })

# 2. Define the initial 3D viewport over the city
view_state = pdk.ViewState(
    latitude=24.8850,
    longitude=67.0600,
    zoom=11,
    pitch=55,  # Tilts the camera angle to see the 3D depth
    bearing=-15,  # Rotates the camera slightly north-west
)

# 3. Create the 3D Column Layer
column_layer = pdk.Layer(
    "ColumnLayer",
    data=chart_data,
    get_position=["longitude", "latitude"],
    get_elevation="Density_Metric",
    elevation_scale=1.5,  # Stretches columns to make differences obvious
    radius=450,  # Width of each 3D pillar in meters
    get_fill_color="[Density_Metric * 0.04, 80, 200, 220]",  # Dynamic color mapping
    pickable=True,
    auto_highlight=True,
)

# 4. Render the interactive chart layout
st.pydeck_chart(
    pdk.Deck(
        layers=[column_layer],
        initial_view_state=view_state,
        tooltip={"text": "{District}\nRelative Density Index: {Density_Metric}"},
    )
)
