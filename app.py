
import streamlit as st




st.title("Welcome to Streamlit!")


st.write("Hello, Streamlit!")
st.write(12345)
st.write({"Name": "Alice", 
          "Age": 30})

st.write("**Bold Text** and *Italic Text*")

st.markdown("This is <u>underlined text</u> in Streamlit.", 
            unsafe_allow_html=True)

st.markdown("This is <i>underlined text</i> in Streamlit.", unsafe_allow_html=True)
st.markdown("This is <b>underlined text</b> in Streamlit.", unsafe_allow_html=True)



