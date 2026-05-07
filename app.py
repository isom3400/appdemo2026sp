# Step 1: Install Streamlit (run in terminal: pip install streamlit)

# Step 2: Import Necessary Libraries
import streamlit as st
import pandas as pd

# Step 3: Load Superstore Dataset
df = pd.read_csv('superstore_dataset.csv')

# Step 4: Convert 'order_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'])  # Convert to datetime if not already

# Step 5: Create a Selectbox for Year Selection
year = st.selectbox(
    'Select the year',
    ('2019', '2020', '2021', '2022')
)

