import streamlit as st
import pandas as pd

# Add a title to the sidebar
st.sidebar.title("PyConZA 2024")

# Sidebar menu for navigation
page = st.sidebar.selectbox(
    "Select a Page",
    ("Talks", "Just Streamlit")
)

# Read the CSV
df = pd.read_csv('talks.csv')

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
    # Title for the Just Streamlit page
    st.title("Just Streamlit")

    # Create tabs for different sections
    tab_names = ["Title","Intro", "Proof of Concept", "Deployment", "Limitations"]
    tabs = st.tabs(tab_names)

    with tabs[0]:
        st.write("# Just Streamlit")
    with tabs[1]:
        st.write("## Intro")
        st.markdown("""
        - Streamlit is an open-source Python framework for building interactive web apps quickly. 
        - No front-end expertise needed — just write Python scripts. 
        - Ideal for rapid prototyping and turning ideas or data scripts into shareable apps in minutes. 
        - Live app updating on save. 
        - Built-in widgets for inputs and visualization.
        """)
    
         # Add the image
        st.image("st01.png", caption="Streamlit Workflow", use_column_width=True)

    # Proof of Concept Tab
    with tabs[2]:
        st.write("## Proof of Concept")
        st.markdown("""
        - Fast Development: Build a fully interactive app with only a few lines of code.
        - No Web Dev Required: No HTML, CSS, or JavaScript — focus on Python. 
        - Perfect for Data Science or Static Apps: Easily display plots, tables, models, and more. 
        - Deploy Easily: One-click deployment with Streamlit Cloud or Docker.
        """)
    
         # Add the image
        st.image("st02.png", caption="Simple App", use_column_width=True)

    # Deployment Tab
    with tabs[3]:
        st.write("## Deployment")
        st.markdown("""
        - Deploy Direct from GitHub: Push your app to GitHub, and it automatically deploys on Streamlit Cloud
        - Managed Scaling: No server configuration — Streamlit Cloud handles traffic and scaling. 
        - Real-Time Collaboration: Share apps instantly with colleagues or the public via a shareable URL. 
        - Can install locally as well: “pip install streamlit” etc…
        """)

    # Limitations Tab
    with tabs[4]:
        st.write("## Limitations")
        st.markdown("""
        - Not designed for developing large scale, feature-rich web apps where user management, scalability, and backend logic are crucial. 
        - Not designed for complex routing, user authentication, sessions, databases, and scalable deployment. 
        - There are experimental features to get some of these working though.
        """)
