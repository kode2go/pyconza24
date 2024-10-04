import streamlit as st
import pandas as pd

# Read the CSV
df = pd.read_csv('talks.csv')

# Sidebar menu for navigation
page = st.sidebar.selectbox(
    "Select a Page",
    ("Talks", "Just Streamlit")
)

# Page 1: Talks
if page == "Talks":
    # Title and description for Talks page
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

# Page 2: Just Streamlit
elif page == "Just Streamlit":
    # Title and content for the Just Streamlit page
    st.title("Just Streamlit")
    st.write("""
    ### Learn More About Streamlit
    Streamlit is an open-source app framework used for building data-driven apps quickly and easily. 
    You can use it to create machine learning apps, dashboards, and more in pure Python.
    
    - It's incredibly easy to set up.
    - It allows for interactive widgets like sliders, buttons, and inputs.
    - You can deploy Streamlit apps easily in the cloud.
    """)
    
    st.write("Check out the [Streamlit Documentation](https://docs.streamlit.io/) to get started.")
    
    # Example Streamlit interactive widget
    st.write("Here is an interactive example:")
    user_input = st.text_input("Type something here:")
    st.write(f"You typed: {user_input}")
