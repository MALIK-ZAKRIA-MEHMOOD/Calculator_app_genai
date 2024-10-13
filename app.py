import streamlit as st

# Functions for the calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit App Interface
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", step=1.0)
num2 = st.number_input("Enter second number", step=1.0)

# Dropdown for operation selection
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate result based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.write(f"The result is: {result}")
