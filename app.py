import streamlit as st
import re

# Add a title to your app
st.title("Course Attendance Calculator")

# Add a text area for pasting attendance information
attendance_info = st.text_area(
    "Paste your attendance information:",
    height=200,
    placeholder="""Example format:
Course : XYZ
Course Code : XYZ
Number of classes Conducted : X
Number of classes Attended : X
Academic Term : X
Attendance Percentage: X%""")

if attendance_info:
    # Extract information using regular expressions
    classes_conducted = re.search(r'Number of classes Conducted\s*:\s*(\d+)', attendance_info)
    classes_attended = re.search(r'Number of classes Attended\s*:\s*(\d+)', attendance_info)
    
    if classes_conducted and classes_attended:
        total_classes = int(classes_conducted.group(1))
        attended_classes = int(classes_attended.group(1))
        
        # Calculate current attendance percentage
        current_percentage = (attended_classes / total_classes) * 100
        
        # Calculate how many more classes can be missed while staying above 75%
        min_classes_needed = total_classes * 0.75  # 75% of total classes
        allowed_absences = attended_classes - min_classes_needed
        
        # Display results
        st.write(f"Current Attendance: {current_percentage:.2f}%")
        
        if allowed_absences > 0:
            st.write(f"You can afford to miss {int(allowed_absences)} more classes while staying above 75%")
        else:
            st.write("Warning: You cannot afford to miss any more classes to maintain 75% attendance")
            if current_percentage < 75:
                st.error("Your attendance is already below 75%!")