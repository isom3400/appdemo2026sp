import math
import streamlit as st


# -------------------------------
# Calculation Functions
# -------------------------------
def calculate_basic(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"


def calculate_scientific(value, power, operation):
    if operation == "Square Root":
        return (
            math.sqrt(value)
            if value >= 0
            else "Error: Negative input for square root"
        )
    elif operation == "Power":
        return math.pow(value, power)
    elif operation == "Sin":
        return math.sin(math.radians(value))
    elif operation == "Cos":
        return math.cos(math.radians(value))
    elif operation == "Tan":
        return math.tan(math.radians(value))
    elif operation == "Log (base 10)":
        return (
            math.log10(value)
            if value > 0
            else "Error: Input must be greater than 0"
        )
    elif operation == "Ln (natural log)":
        return (
            math.log(value)
            if value > 0
            else "Error: Input must be greater than 0"
        )


# -------------------------------
# Basic Calculator UI
# -------------------------------
st.title("Basic Web Calculator")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)
operation = st.selectbox(
    "Choose operation", ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):
    result = calculate_basic(num1, num2, operation)
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"Result: {result}")

# -------------------------------
# Scientific Calculator UI
# -------------------------------
st.header("Scientific Functions")

operation_sci = st.selectbox(
    "Choose scientific operation",
    [
        "Square Root",
        "Power",
        "Sin",
        "Cos",
        "Tan",
        "Log (base 10)",
        "Ln (natural log)",
    ],
)

value = st.number_input("Enter value", value=0.0)
power = st.number_input("Enter power (if applicable)", value=2.0)

if st.button("Calculate Scientific"):
    result = calculate_scientific(value, power, operation_sci)
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"Result: {result}")

