# emailautofill.py

import streamlit as st
import datetime

st.title("Octopus Energy - Appointment Email Generator")

# Date input with format as DD/MM/YYYY
date = st.date_input("Appointment date", datetime.date.today())

# Time slot select box
time_slot = st.selectbox("Time slot", ["AD (8am - 5pm)", "AM (8am - 12pm)", "PM (1pm - 5pm)"])

# Appointment type select box
appointment_type = st.selectbox(
    "Appointment type",
    ["DF Mex", "Elec Mex", "Gas Mex", "Elec New Conn", "Gas New Conn", "DF new conn", "On-Site comms", "Other"]
)

# User's name input
your_name = st.text_input("Your name")

# Button to trigger email generation
generate = st.button("Generate email")

if generate and your_name:
    # Mapping for time slots
    time_mapping = {"AD": "8am - 5pm", "AM": "8am - 12pm", "PM": "1pm - 5pm"}
    time_key = time_slot.split(" ")[0]
    time_value = time_mapping.get(time_key, "a selected time")

    # Mapping for appointment types
    appointment_mapping = {
        "DF Mex": "gas and electric meter exchange",
        "Elec Mex": "electric meter exchange",
        "Gas Mex": "gas meter exchange",
        "Elec New Conn": "electric new connection",
        "Gas New Conn": "gas new connection",
        "DF new conn": "gas and electric new connection",
        "On-Site comms": "on-site commissioning appointment for your smart meters",
        "Other": "custom appointment"
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

    # Date formatted as DD/MM/YYYY
    formatted_date = date.strftime('%d/%m/%Y')

    # Generating email content
    email = f"""Hi,

Thank you for speaking with me and I'm glad we could get you booked in for a {appointment_desc}. As requested, we’ve booked your metering appointment for {formatted_date} between {time_value}.

Just in regards to your appointment, here’s some additional information, and if any of these cause any issues, then give us a call or email.

{additional}
- Our engineer will give 30 minutes notice before their arrival.
- We’ll need someone over the age of 18 in the house throughout your appointment, even if your meter is located externally. This is so we can complete our safety checks inside your house before and after the work is completed. The person present doesn’t necessarily need to be the owner/occupier of the property. It can be a friend, neighbour or a family member.
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

    # Display the generated email
    st.text_area("Generated Email", value=email, height=400)

