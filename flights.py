import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Function to generate date range
def generate_date_range(start_date, end_date):
    date_range = []
    current_date = start_date
    while current_date <= end_date:
        date_range.append(current_date.strftime("%d-%m-%Y"))
        current_date += timedelta(days=1)
    return date_range

# Function to generate flight pattern
def generate_flight_pattern(flight_number, start_date, end_date):
    date_range = generate_date_range(start_date, end_date)
    pattern = f"{flight_number} | {' | '.join(date_range)}"
    return pattern

# Sample data
data = {
    'Flight Number': ['ABC123', 'XYZ456', '123XYZ'],
    'Start Date': ['12-01-2024', '15-01-2024', '10-01-2024'],
    'End Date': ['25-01-2024', '20-01-2024', '18-01-2024'],
    'Additional Info': ['Info1', 'Info2', 'Info3'],
}

df = pd.DataFrame(data)

# List of example flight numbers
flight_numbers = df['Flight Number'].tolist()

# Streamlit app
st.title("Flight Pattern Generator")

# Dropdown menu for flight number
flight_number = st.selectbox("Select Flight Number:", flight_numbers)

# Calendar-based date selection for start and end date
start_date = st.date_input("Select Start Date:")
end_date = st.date_input("Select End Date:")

# Button to generate pattern
if st.button("Generate Pattern"):
    if flight_number and start_date and end_date:
        pattern = generate_flight_pattern(flight_number, start_date, end_date)
        st.success(f"Flight Pattern: {pattern}")

        # Display string with flight information
        flight_info_str = f"Selected Flight: {flight_number} | Start Date: {start_date.strftime('%d-%m-%Y')} | End Date: {end_date.strftime('%d-%m-%Y')}"
        st.write(flight_info_str)

        # Display table with flight information
        st.write("Flight Information:")
        
        # Checkbox for each row
        selected_flight_number = st.text_input("Selected Flight Number:", value=flight_number, key="flight_code_input")
        for i, row in df.iterrows():
            checkbox = st.checkbox("", key=f"checkbox_{i}")
            if checkbox:
                selected_flight_number = row['Flight Number']
                st.write(f"Selected: {selected_flight_number} | {row['Start Date']} | {row['End Date']} | {row['Additional Info']}")
                st.text_input("Flight Code:", value=selected_flight_number, key="flight_code_input")
    else:
        st.warning("Please fill in all the required fields.")
