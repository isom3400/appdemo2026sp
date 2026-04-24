

import math
import streamlit as st

st.header("Scientific Functions")

# Use columns to make the layout more compact
col1, col2 = st.columns(2)

with col1:
    operation_sci = st.selectbox("Operation", 
                                 ["Square Root", "Power", "Sin", "Cos", "Tan"])
with col2:
    value = st.number_input("Value", value=0.0)

# Only show the power input if "Power" is selected
power = None
if operation_sci == "Power":
    power = st.number_input("Enter exponent", value=2.0)

if st.button("Calculate", type="primary"):
    try:
        if operation_sci == "Square Root":
            if value < 0:
                st.error("Cannot calculate square root of a negative number.")
            else:
                result = math.sqrt(value)
        elif operation_sci == "Power":
            result = math.pow(value, power)
        elif operation_sci == "Sin":
            result = math.sin(math.radians(value))
        elif operation_sci == "Cos":
            result = math.cos(math.radians(value))
        elif operation_sci == "Tan":
            # Check for tan(90) or tan(270) etc.
            if (value - 90) % 180 == 0:
                st.error("Undefined (Vertical Asymptote)")
            else:
                result = math.tan(math.radians(value))
        
        # Display result if no error occurred
        if 'result' in locals():
            st.metric(label="Result", value=f"{result:,.3f}")
            
    except Exception as e:
        st.error(f"Error: {e}")
        
