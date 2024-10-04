import streamlit as st
import pandas as pd

# Read the CSV
df = pd.read_csv('talks.csv')

# Add a title and a short description
st.title("PyConZA 2024 Talks")
st.write("""
### Welcome to the PyConZA 2024 Schedule
Explore the various talks and sessions happening at PyConZA. Navigate through different categories of presentations including Talks, Keynotes, Tutorials, and more.
""")

# Create separate tabs for different categories
tab_names = ["Talk", "Remote Talk", "Keynote", "Tutorial", "Open Space", "Sponsor Talk"]
tabs = st.tabs(tab_names)

# Iterate through each tab and display the relevant data
for i, tab in enumerate(tabs):
    with tab:
        category = tab_names[i]
        st.write(f"## {category}")
        filtered_df = df[df['Category'] == category]
        st.dataframe(filtered_df)
