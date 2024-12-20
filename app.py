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
        
        # Calculate maximum absences allowed
        # For attendance to stay above 75%, we need: (attended_classes - x)/(total_classes) >= 0.75
        # Where x is the number of classes that can be missed
        # Solving for x: x <= attended_classes - (0.75 * total_classes)
        max_absences = attended_classes - (0.75 * total_classes)
        
        # Display results
        st.write(f"Current Attendance: {current_percentage:.2f}%")
        
        if max_absences > 0:
            st.write(f"You can afford to miss {int(max_absences)} more classes while staying above 75%")
        else:
            if current_percentage >= 75:
                st.warning("You cannot afford to miss any more classes to maintain 75% attendance")
            else:
                st.error("Your attendance is already below 75%!")
                # Calculate classes needed to reach 75%
                classes_needed = int((0.75 * total_classes) - attended_classes)
                st.write(f"You need to attend {classes_needed} more classes to reach 75% attendance")