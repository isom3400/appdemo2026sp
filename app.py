

import streamlit as st
from streamlit_option_menu import option_menu

st.title('Hello, Students!')
st.write('This is your Python Programming course.')

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu 📁",
        options = ["Home", "About", "Contact"],
        icons = ["house-fill",      # Home icon
                 "info-circle",     # Info icon
                 "envelope-at"],    # Mail icon
        menu_icon = "cast",         # Sidebar/Cast icon
        default_index = 0,
    )
    selected2 = option_menu(
        menu_title2 = "Main Menu 📁",
        options2 = ["Home", "About", "Contact"],
        icons2 = ["house-fill",      # Home icon
                 "info-circle",     # Info icon
                 "envelope-at"],    # Mail icon
        menu_icon2 = "cast",         # Sidebar/Cast icon
        default_index = 0,
    )

if selected == "Home":
    st.title(f"Welcome to the {selected} page.")

if selected == "About":
    st.title(f"Welcome to the {selected} page.")

if selected == "Contact":
    st.title(f"Welcome to the {selected} page.")

