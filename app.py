
import streamlit as st




option = st.selectbox("Choose your favorite color:",
                      ["Red", 
                       "Blue", 
                       "Green",
                      "Yellow",
                      "Brown"])

if option == "Brown":
    st.write(f"You selected: {option}")
elif option == "Red":
    st.header(f"You selected: {option}")




