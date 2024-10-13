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
st.title("🧮 Simple Calculator")

# Input fields for numbers with better structure
st.markdown("### Enter Your Numbers:")
num1 = st.number_input("Enter first number", step=1.0, format="%.2f")
num2 = st.number_input("Enter second number", step=1.0, format="%.2f")

# Dropdown for operation selection
st.markdown("### Choose an Operation:")
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Button to trigger calculation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"**The result of addition is:** {result:.2f}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"**The result of subtraction is:** {result:.2f}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"**The result of multiplication is:** {result:.2f}")
    elif operation == "Divide":
        result = divide(num1, num2)
        if isinstance(result, str):  # Error handling for division by zero
            st.error(result)
        else:
            st.success(f"**The result of division is:** {result:.2f}")
else:
    st.info("Enter the numbers and select an operation to calculate.")

# Adding some footer styling
st.markdown("---")
st.markdown("### Designed by [MALIK ZAKRIA MEHMOOD](https://https://github.com/MALIK-ZAKRIA-MEHMOOD.com)")
