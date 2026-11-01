
import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

st.set_page_config(
    page_title="Smart Waste Management",
    page_icon="♻️",
    layout="wide"
)

# Dark theme
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #10152f, #172554, #34205c);
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
div[data-testid="stMetric"] {
    background: #1e293b;
    padding: 15px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("♻️ Smart Waste Management")
st.subheader("Solid Waste Segregation Inefficiency")
st.write("Explore waste data, pollution effects and waste segregation.")

# Waste data
df = pd.DataFrame({
    "Area": [
        "Residential Area",
        "School Area",
        "Market Area",
        "Park Area",
        "Office Area"
    ],
    "Dry Waste": [5, 4, 8, 2, 3],
    "Wet Waste": [3, 6, 6, 5, 2],
    "Mixed Waste": [2, 3, 4, 1, 2],
    "Latitude": [22.3072, 22.3150, 22.2980, 22.3200, 22.3000],
    "Longitude": [73.1812, 73.1900, 73.1700, 73.1750, 73.1850]
})

df["Total Waste"] = (
    df["Dry Waste"] +
    df["Wet Waste"] +
    df["Mixed Waste"]
)

df["Mixed Waste (%)"] = (
    df["Mixed Waste"] / df["Total Waste"] * 100
).round(1)

# Waste Summary
st.header("📊 Waste Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Waste", "56 kg")
col2.metric("Dry Waste", "22 kg")
col3.metric("Wet Waste", "22 kg")
col4.metric("Mixed Waste", "12 kg")

# Dropdown
st.header("Explore Waste Categories")

category = st.selectbox(
    "Select Waste Category",
    ["Dry Waste", "Wet Waste", "Mixed Waste"]
)

# Category chart
st.subheader(f"{category} by Area")

fig = px.bar(
    df,
    x="Area",
    y=category,
    color="Area",
    text=category,
    title=f"{category} (kg)"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig, use_container_width=True)

# Pie chart
st.subheader("Waste Category Distribution")

waste_totals = pd.DataFrame({
    "Category": ["Dry Waste", "Wet Waste", "Mixed Waste"],
    "Amount": [22, 22, 12]
})

pie = px.pie(
    waste_totals,
    names="Category",
    values="Amount",
    hole=0.4
)

pie.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(pie, use_container_width=True)

# Waste table
st.header("📋 Waste Data Table")
st.dataframe(df, use_container_width=True)

# 3D Map
st.header("🗺️ 3D Area-wise Waste Analysis Map")

map_data = df.copy()

map_data["color"] = [
    [40, 120, 255],
    [40, 170, 90],
    [255, 160, 30],
    [30, 160, 130],
    [170, 90, 220]
]

map_data["height"] = map_data["Total Waste"] * 100

column_layer = pdk.Layer(
    "ColumnLayer",
    data=map_data,
    get_position=["Longitude", "Latitude"],
    get_elevation="height",
    elevation_scale=1,
    radius=100,
    get_fill_color="color",
    pickable=True
)

marker_layer = pdk.Layer(
    "ScatterplotLayer",
    data=map_data,
    get_position=["Longitude", "Latitude"],
    get_radius=150,
    get_fill_color="color",
    radius_min_pixels=8,
    radius_max_pixels=20,
    pickable=True
)

view_state = pdk.ViewState(
    latitude=22.3072,
    longitude=73.1812,
    zoom=12,
    pitch=50,
    bearing=-20
)

deck = pdk.Deck(
    layers=[column_layer, marker_layer],
    initial_view_state=view_state,
    tooltip={
        "html": """
        <b>{Area}</b><br/>
        Dry Waste: {Dry Waste} kg<br/>
        Wet Waste: {Wet Waste} kg<br/>
        Mixed Waste: {Mixed Waste} kg<br/>
        Total Waste: {Total Waste} kg<br/>
        Mixed Waste: {Mixed Waste (%) }%
        """
    }
)

st.pydeck_chart(deck)

# Environmental effects
st.header("🌍 Possible Environmental Effects")

effects = [
    "Plastic waste may pollute soil and water.",
    "Open waste burning can cause air pollution.",
    "Unmanaged waste can create unpleasant smells.",
    "Waste accumulation may attract insects and pests.",
    "Poor segregation makes recycling difficult."
]

for effect in effects:
    st.write("⚠️", effect)

# Photo Gallery
st.header("📸 Waste Pollution Photos")
st.write("Real photos showing waste pollution and its possible effects.")

photos = [
    (
        "Plastic Waste",
        "https://images.unsplash.com/photo-1532996122724-e3c354a0b15?w=800"
    ),
    (
        "Garbage Pollution",
        "https://images.unsplash.com/photo-1605600659873-d808a13e4d9a?w=800"
    ),
    (
        "Waste Collection",
        "https://images.unsplash.com/photo-1618477461853-cf6ed80faba5?w=800"
    ),
    (
        "Plastic Pollution",
        "https://images.unsplash.com/photo-1604187351574-c75ca79f5807?w=800"
    ),
    (
        "Environmental Pollution",
        "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=800"
    ),
    (
        "Waste Recycling",
        "https://images.unsplash.com/photo-1532996122724-e3c354a0b15?w=800"
    )
]

photo_cols = st.columns(3)

for i, (title, url) in enumerate(photos):
    with photo_cols[i % 3]:
        st.image(url, caption=title, use_container_width=True)

# Segregation Tips
st.header("♻️ Waste Segregation Tips")

tips = [
    "Keep dry and wet waste separate.",
    "Reuse items whenever possible.",
    "Recycle paper, plastic and metal.",
    "Put organic waste in a compost bin.",
    "Avoid throwing waste in public places."
]

for tip in tips:
    st.write("✅", tip)

st.info(
    "Proper waste segregation can support cleaner surroundings "
    "and better waste management."
)

st.markdown("---")

st.title(" 💜 Thank You 💜 ")

st.subheader("Reduce • Reuse • Recycle")

st.write("Let's Keep Our Environment Clean and Green 🌍")

st.markdown("### Created by Akshita Parmar")