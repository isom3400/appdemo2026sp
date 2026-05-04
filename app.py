# Step 1: Install Streamlit (run in terminal: pip install streamlit)

# Step 2: Import Necessary Libraries
import streamlit as st
import numpy as np
import pandas as pd

# Step 3: Generate Random Sales Data
sales_data = np.random.rand(100) * 1000

# Step 4: Create a DataFrame
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = np.random.rand(5) * 1000
customers = np.random.randint(1, 100, size=5)

df = pd.DataFrame({
    'Product': products,
    'Sales': sales,
    'Customers': customers
})


# Step 5: Visualize Sales Data

# Display DataFrame using st.dataframe
st.markdown("### Product Sales and Customer Data")
st.dataframe(df)  # Interactive table with sorting and resizing
