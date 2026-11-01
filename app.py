
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Smart Waste Management",
    page_icon="♻️",
    layout="wide"
)

st.title("♻️ Smart Waste Management")
st.subheader("Solid Waste Segregation Inefficiency")
st.write("Explore waste data, pollution effects and waste segregation.")

# Project data
df = pd.DataFrame({
    "Area": ["Residential", "School", "Market", "Park", "Office"],
    "Dry Waste": [5, 4, 8, 2, 3],
    "Wet Waste": [3, 6, 6, 5, 2],
    "Mixed Waste": [2, 3, 4, 1, 2]
})

df["Total Waste"] = (
    df["Dry Waste"] +
    df["Wet Waste"] +
    df["Mixed Waste"]
)

# Summary
st.header("📊 Waste Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Waste", "56 kg")
c2.metric("Dry Waste", "22 kg")
c3.metric("Wet Waste", "22 kg")
c4.metric("Mixed Waste", "12 kg")

# Dropdown
st.header("Explore Waste Categories")

category = st.selectbox(
    "Select Waste Category",
    ["Dry Waste", "Wet Waste", "Mixed Waste"]
)

# Chart
fig = px.bar(
    df,
    x="Area",
    y=category,
    color="Area",
    title=f"{category} by Area",
    text=category
)

st.plotly_chart(fig, use_container_width=True)

# Pie chart
waste_data = pd.DataFrame({
    "Category": ["Dry Waste", "Wet Waste", "Mixed Waste"],
    "Amount": [22, 22, 12]
})

fig2 = px.pie(
    waste_data,
    names="Category",
    values="Amount",
    title="Overall Waste Composition",
    hole=0.4
)

st.plotly_chart(fig2, use_container_width=True)

# Data table
st.header("Waste Data Table")
st.dataframe(df, use_container_width=True)

# Side effects
st.header("🌍 Possible Environmental Effects")

st.write("""
- Plastic waste may pollute soil and water.
- Open waste burning can cause air pollution.
- Unmanaged waste can create unpleasant smells.
- Waste accumulation may attract insects and pests.
- Poor segregation makes recycling difficult.
""")

# Photos
st.header("📸 Waste Pollution Photos")

st.image(
    "https://images.unsplash.com/photo-1532996122724-e3c354a0b15?w=800",
    caption="Waste pollution"
)

st.image(
    "https://images.unsplash.com/photo-1605600659873-d808a13e4d9a?w=800",
    caption="Waste management"
)

st.image(
    "https://images.unsplash.com/photo-1618477461853-cf6ed80faba5?w=800",
    caption="Environmental pollution"
)

# Tips
st.header("♻️ Waste Segregation Tips")

st.write("""
- Keep dry and wet waste separate.
- Reuse items whenever possible.
- Recycle paper, plastic and metal.
- Put organic waste in a compost bin.
- Avoid throwing waste in public places.
""")

# Conclusion
st.success("""
Proper waste segregation can support cleaner surroundings
and better waste management.
""")

# Thank you
st.markdown("---")
st.title("💜 Thank You 💜")
st.subheader("Reduce • Reuse • Recycle")
st.write("Let's Keep Our Environment Clean and Green 🌍")
