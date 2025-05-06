import streamlit as st
import datetime

# Add a header to the app
st.title("Email Autofill for Appointment Confirmation")

# Streamlit widgets for user input
name = st.text_input("Enter the name")
appointment_date = st.date_input(
    "Select appointment date", 
    datetime.date(2025, 5, 6),
    format="DD/MM/YYYY"
)
appointment_type = st.selectbox(
    "Select the appointment type",
    ["DF Mex", "Elec Mex", "Gas Mex", "Elec New Conn", "Gas New Conn", "DF new conn", "On-Site comms", "Other"]
)
time_slot = st.selectbox(
    "Select the time slot",
    ["AD", "AM", "PM"]
)

# Formatting the appointment date
appointment_date_str = appointment_date.strftime("%d/%m/%Y")

# Define the email template
email_body = f"""
Hi {name},

Thank you for speaking with me and I'm glad we could get you booked in for a {appointment_type} appointment. 
As requested, we’ve booked your metering appointment for {appointment_date_str} between {time_slot}.

Just in regards to your appointment, here’s some additional information, and if any of these cause any issues, then give us a call or email.

"""

# Add specific information based on the appointment type
if appointment_type == "DF Mex":
    email_body += "- Most jobs take around 2 hours, which is an hour for each meter (if you only have an electricity meter it will take around an hour). Your electricity and gas will need to be switched off for up to an hour during this period.\n"
elif appointment_type == "Elec Mex":
    email_body += "- Most jobs take around 1 hour. Your electricity will need to be switched off for up to an hour during this period.\n"
elif appointment_type == "Gas Mex":
    email_body += "- Most jobs take around 1 hour. Your gas will need to be switched off for up to an hour during this period.\n"
elif appointment_type == "Elec New Conn":
    email_body += "- Most jobs take around 1 hour.\n- You will need an electrician to attend after our engineer to connect the meter to the rest of the property.\n"
elif appointment_type == "Gas New Conn":
    email_body += "- Most jobs take around 1 hour.\n- You will need a gas safety engineer to attend after our engineer to uncap the gas.\n"
elif appointment_type == "DF new conn":
    email_body += "- Most jobs take around 2 hours, which is an hour for each meter.\n- You will need an electrician and a gas safety engineer to attend after our engineer to connect the electric meter to the rest of the property and to uncap the gas.\n"
elif appointment_type == "On-Site comms":
    email_body += "\n"
else:
    email_body += "- Custom appointment details.\n"

email_body += """
- Our engineer will give 30 minutes notice before their arrival.
- We’ll need someone over the age of 18 in the house throughout your appointment, even if your meter is located externally. This is so we can complete our safety checks inside your house before and after the work is completed. The person present doesn’t necessarily need to be the owner/occupier of the property. It can be a friend, neighbour or a family member.
- The engineer will need somewhere close by to park.
- If there are any obstructions / if the engineer will need a ladder to reach your meters, please let us know. The maximum height our engineers can work at is 7.2ft.
- If you have a dog, please ensure that it is securely kept away from the area where our engineer will be working.

If you have any questions between now and your appointment, please email us at hello@octoes.com.

Kind regards,
{name}

Field Team Support Specialist
Octopus Energy Services
Feedback/Queries Email: hello@octoes.com
"""

# Display the generated email template
st.subheader("Generated Email")
st.text_area("Copy this email", value=email_body, height=300)

# Optional: Add a copy-to-clipboard button
st.download_button(
    label="Copy to clipboard",
    data=email_body,
    file_name="email_template.txt",
    mime="text/plain"
)


