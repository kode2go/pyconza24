import streamlit as st
import pandas as pd

# Read the CSV
df = pd.read_csv('talks.csv')

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
