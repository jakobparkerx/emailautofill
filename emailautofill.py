# emailautofill.py

import streamlit as st
import datetime
import logging

logging.getLogger('streamlit').setLevel(logging.CRITICAL)

# Constants for time slots and appointment types
TIME_SLOTS = ["AD (8am - 5pm)", "AM (8am - 12pm)", "PM (1pm - 5pm)"]
APPOINTMENT_TYPES = [
    "DF Mex", "Elec Mex", "Gas Mex", "Elec New Conn", 
    "Gas New Conn", "DF new conn", "On-Site comms"
]

st.title("Appointment Email Generator")

# Date input with default value
date = st.date_input("Appointment date", datetime.date.today())

# Format the date as DD/MM/YYYY for display purposes
formatted_date = date.strftime('%d/%m/%Y')

# Display the formatted date
st.write(f"Selected date (formatted): {formatted_date}")

# Time slot select box
time_slot = st.selectbox("Time slot", TIME_SLOTS)

# Appointment type select box
appointment_type = st.selectbox("Appointment type", APPOINTMENT_TYPES)

# User's name input
your_name = st.text_input("Your name")

# Button to trigger email generation
generate = st.button("Generate email")

if generate:
    if not your_name:
        st.error("Please enter your name.")
    else:
        # Mapping for time slots
        time_mapping = {
            "AD": "8am - 5pm",
            "AM": "8am - 12pm",
            "PM": "1pm - 5pm"
        }
        time_value = time_mapping.get(time_slot[:2], "a selected time")  # Extract first 2 chars as key

        # Mapping for appointment types
        appointment_mapping = {
            "DF Mex": "a gas and electric meter exchange",
            "Elec Mex": "an electric meter exchange",
            "Gas Mex": "a gas meter exchange",
            "Elec New Conn": "an electric new connection",
            "Gas New Conn": "a gas new connection",
            "DF new conn": "a gas and electric new connection",
            "On-Site comms": "an on-site commissioning appointment for your smart meters"
        }

        # Additional info based on appointment type
        additional_info = {
            "DF Mex": "- Most jobs take around 2 hours (1 hour per meter). Your electricity and gas will need to be switched off for up to an hour.",
            "Elec Mex": "- Most jobs take around 1 hour. Your electricity will need to be switched off for up to an hour.",
            "Gas Mex": "- Most jobs take around 1 hour. Your gas will need to be switched off for up to an hour.",
            "Elec New Conn": "- Most jobs take around 1 hour.\n- You will need an electrician to connect the meter to the property after our engineer attends.",
            "Gas New Conn": "- Most jobs take around 1 hour.\n- You will need a gas safety engineer to uncap the gas after our engineer attends.",
            "DF new conn": "- Most jobs take around 2 hours (1 hour per meter).\n- You will need both an electrician and a gas safety engineer to connect/un-cap after our engineer attends.",
            "On-Site comms": "",
            "Other": ""
        }

        # Fetching appointment type and additional info
        appointment_desc = appointment_mapping.get(appointment_type, "an appointment")
        additional = additional_info.get(appointment_type, "")

        # Generating email content
        email = f"""Hi,

Thank you for speaking with me and I'm glad we could get you booked in for {appointment_desc}. As requested, we’ve booked your metering appointment for {formatted_date} between {time_value}.

Just in regards to your appointment, here’s some additional information, and if any of these cause any issues, then give us a call or email.

{additional}
- Our engineer will give 30 minutes notice before their arrival.
- We’ll need someone over the age of 18 in the house throughout your appointment, even if your meter is located externally. This is so we can complete our safety checks inside your house before we leave.
- The engineer will need somewhere close by to park.
- If there are any obstructions / if the engineer will need a ladder to reach your meters, please let us know. The maximum height our engineers can work at is 7.2ft.
- If you have a dog, please ensure that it is securely kept away from the area where our engineer will be working.

If you have any questions between now and your appointment, please email us at hello@octoes.com.

Kind regards,  
{your_name}

Field Team Support Specialist  
Octopus Energy Services  
Feedback/Queries Email: hello@octoes.com
"""

        # Display the generated email in a text area with error handling
        try:
            st.text_area("Generated Email", value=email, height=400, key="email_text_area")
        except NameError as e:
            # Log the error for debugging purposes
            st.error("An unexpected error occurred. Please try again later.")
            with open("error.log", "a") as log_file:
                log_file.write(f"Error: {str(e)}\n")

# Add a "Copy to Clipboard" button using JavaScript
st.markdown(
    """
    <button onclick="copyToClipboard()">Copy to Clipboard</button>
    <script>
    function copyToClipboard() {
        const textArea = document.querySelector('textarea[data-testid="stTextArea"]');
        if (textArea) {
            textArea.select();
            document.execCommand('copy');
            alert('Text copied to clipboard!');
        }
    }
    </script>
    """, 
    unsafe_allow_html=True
)
