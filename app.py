import streamlit as st

# Add a title to your app
st.title("Class Attendance Calculator")

# Input for credit hours using number_input to restrict to numbers only
credit_hours = st.number_input(
    "Enter Course Credit Hours:",
    min_value=1,  # Minimum allowed value
    max_value=4,  # Maximum allowed value
    placeholder="2, 3, or 4",  # Placeholder text
    help="Enter credit hours (2, 3, or 4)"  # Help text
)

# Input for number of absences
absences = st.number_input(
    "Enter Number of Classes Absent:",
    min_value=0,  # Minimum allowed value
    help="Enter the number of classes you have missed."
)

# Calculate remaining classes based on credit hours
if credit_hours and absences >= 0:  # Check if inputs are provided
        if credit_hours == 4:    
        # Display results
            st.write(f"You can only afford {16-absences} more absences.")
            
        if credit_hours == 3:    
        # Display results
            st.write(f"You can only afford {12-absences} more absences.")

        if credit_hours == 2:    
        # Display results
            st.write(f"You can only afford {8-absences} more absences.")
        