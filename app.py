import streamlit as st

st.title("Welcome to Streamlit!")

st.header("Section 1: Introduction")
st.write("Hello, Streamlit!")
st.write(12345)
st.write({"Name": "Alice", "Age": 30})

st.write(['list1', 
          'list2'])

st.header("Section 2: MarkDown")
st.write("**Bold Text** and *Italic Text*")




Choose IPYNB Output Option:


Show


Hide

import streamlit as st


st.title()
st.title("Welcome to Streamlit!")


st.write()
st.write("Hello, Streamlit!")
st.write(12345)
st.write({"Name": "Alice", "Age": 30})


May also use Markdown
st.write("**Bold Text** and *Italic Text*")


st.header()
st.header("Section 1: Introduction")


st.number_input()
age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)





