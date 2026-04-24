

import streamlit as st

# Title and Header

st.title("Retail Business Dashboard")
st.header("Manager Input Section")


# Instruction

st.write("Please enter the monthly sales target and select the region.")


# Number input for sales target

monthly_sales = st.number_input("Enter Monthly Sales Target (in USD):",
                                 min_value=0,
                                 max_value=50000,
                                 value=5000)

# Dropdown for region selection

region = st.selectbox("Select Region:", ["North", "South", "East", "West"])

# Submit button
if st.button("Submit"):
    # Display entered values

    st.write(f"The sales target entered: ${monthly_sales}")
    st.write(f"The selected region: {region}")

    # Success message

    st.success("Dashboard updated successfully!")
