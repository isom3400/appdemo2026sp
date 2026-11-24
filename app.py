import math
import streamlit as st

# Calculation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"

def log_base10(a):
    return math.log10(a) if a > 0 else "Error: Input must be greater than 0"

def natural_log(a):
    return math.log(a) if a > 0 else "Error: Input must be greater than 0"

# Title
st.title("Basic Web Calculator")

# Operation selection
operation = st.selectbox(
    "Choose operation", 
    ["Add", "Subtract", "Multiply", "Divide", "Log (base 10)", "Ln (natural log)"]
)

# Input fields (hide second input for single-argument logarithmic functions)
num1 = st.number_input("Enter first number", value=0.0)
if operation not in ["Log (base 10)", "Ln (natural log)"]:
    num2 = st.number_input("Enter second number", value=0.0)

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Log (base 10)":
        result = log_base10(num1)
    elif operation == "Ln (natural log)":
        result = natural_log(num1)

    st.success(f"Result: {result}")
