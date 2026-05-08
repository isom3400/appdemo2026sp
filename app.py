import pandas as pd
import streamlit as st

# Sample data
data = {'Product': ['A', 'B', 'C'], 
        'Sales': [1200, 850, 950], 
        'Customers': [300, 400, 350]}
df = pd.DataFrame(data)

# Show data with Streamlit elements
st.dataframe(df)                # Interactive table

st.data_editor(df)              # Editable table


