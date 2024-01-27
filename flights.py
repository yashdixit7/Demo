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

# List of available flight numbers
flight_numbers = df['Flight Number'].tolist()

# Streamlit app
st.title("Flight Pattern Generator")

# Calendar-based date selection for start and end date
start_date = st.date_input("Select Start Date:")
end_date = st.date_input("Select End Date:")

# Dropdown menu for flight number
selected_flight_numbers = st.multiselect("Select Flight Numbers:", flight_numbers, default=flight_numbers)

# Button to generate pattern
if st.button("Generate Pattern"):
    if selected_flight_numbers and start_date and end_date:
        for flight_number in selected_flight_numbers:
            pattern = generate_flight_pattern(flight_number, start_date, end_date)
            st.success(f"Flight Pattern for {flight_number}: {pattern}")
    else:
        st.warning("Please fill in all the required fields.")

# Display table with flight information
st.write("All Available Flight Information:")
for i, row in df.iterrows():
    st.checkbox("", value=(row['Flight Number'] in selected_flight_numbers), key=f"checkbox_{i}")
    st.write(f"Flight: {row['Flight Number']} | Start Date: {row['Start Date']} | End Date: {row['End Date']} | Additional Info: {row['Additional Info']}")
