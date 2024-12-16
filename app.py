import streamlit as st

# Add a title to your app
st.title("Course Attendance Calculator")

# Input for credit hours using number_input to restrict to numbers only
credit_hours = st.number_input(
    "Enter Course Credit Hours:",
    min_value=1,  # Minimum allowed value
    max_value=4,  # Maximum allowed value
    value=1,      # Default value
    placeholder="2, 3, or 4",  # Placeholder text
    help="Enter credit hours (2, 3, or 4)"  # Help text
)

# Input for number of absences
absences = st.number_input(
    "Enter Number of Classes Absent:",
    min_value=1,  # Minimum allowed value
    value=1,      # Default value
    help="Enter the number of classes you have missed."
)

# Calculate remaining classes based on credit hours
if credit_hours and absences >= 0:  # Check if inputs are provided
    absent = 0  # Initialize the absent variable
    
    if credit_hours == 4:    
        absent = 16-absences
        st.write(f"You can only afford {absent} more absents.")
            
    elif credit_hours == 3:    
        absent = 12-absences
        st.write(f"You can only afford {absent} more absents.")

    elif credit_hours == 2:    
        absent = 8-absences
        st.write(f"You can only afford {absent} more absents.")
    
    # Only show this if we have valid input and after showing absences
    if absent > 0:  # Optional: check if we have valid absences
        hours = absent * 24 
        st.write(f"That's {hours} hours to actually do something with your life.")
        