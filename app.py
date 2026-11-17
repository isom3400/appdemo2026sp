
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# Title and Description
# -------------------------------
st.title("📊 Business Sales Dashboard")
st.write("Analyze monthly sales data interactively!")


# -------------------------------
# Sample Data
# -------------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = np.random.randint(5000, 20000, size=12)
expenses = np.random.randint(3000, 15000, size=12)

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [4545, 6666, 77667, 45454, 454545, 3433,
             3434,44,433,223,222,222],
    "Expenses": np.random.randint(3000, 15000, size=12)
})


# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("Filters")
selected_months = st.sidebar.multiselect("Select Months", months,
                                         default=months)








