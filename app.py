

import streamlit as st
from streamlit_option_menu import option_menu

st.title('Hello, Students!')
st.write('This is your Python Programming course.')

with st.sidebar:
    # First Menu
    selected = option_menu(
        menu_title = "Main Menu 📁",
        options = ["Home", "About", "Contact"],
        icons = ["house-fill", "info-circle", "envelope-at"],
        menu_icon = "cast",
        default_index = 0,
    )
    
    # Second Menu (Fixed parameter names)
    selected2 = option_menu(
        menu_title = "Secondary Menu 🛠️", # Use 'menu_title', not 'menu_title2'
        options = ["Settings", "Help", "Logout"], # Use 'options', not 'options2'
        icons = ["gear", "question-circle", "door-open"], 
        menu_icon = "tools",
        default_index = 0,
    )

if selected == "Home":
    st.title(f"Welcome to the {selected} page.")

if selected == "About":
    st.title(f"Welcome to the {selected} page.")

if selected == "Contact":
    st.title(f"Welcome to the {selected} page.")

