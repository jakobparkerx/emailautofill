# emailautofill.py
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="Email Generator", layout="centered")
st.title("Appointment Email Generator")

# --- User Inputs ---
appointment_date = st.date_input(
    "Select appointment date", 
    datetime.date(2025, 5, 6),
    format="DD/MM/YYYY"
time_slot = st.selectbox("Time Slot", ["AD (8am-5pm)", "AM (8am-12pm)", "PM (1pm-5pm)"])
appointment_type = st.selectbox(
    "Appointment Type",
    [
        "DF Mex",
        "Elec Mex",
        "Gas Mex",
        "Elec New Conn",
        "Gas New Conn",
        "DF new conn",
        "On-Site comms",
        "Other"
    ]
)
sender_name = st.text_input("Your Name (Sender)")


def get_appointment_description(apt_type):
    return {
        "DF Mex": "gas and electric meter exchange",
        "Elec Mex": "electric meter exchange",
        "Gas Mex": "gas meter exchange",
        "Elec New Conn": "electric new connection",
        "Gas New Conn": "gas new connection",
        "DF new conn": "gas and electric new connection",
        "On-Site comms": "on-site commissioning appointment for your smart meters",
        "Other": "custom appointment",
    }.get(apt_type, "an appointment")

def get_time_slot_text(slot):
    mapping = {
        "AD (8am-5pm)": "8am - 5pm",
        "AM (8am-12pm)": "8am - 12pm",
        "PM (1pm-5pm)": "1pm - 5pm"
    }
    return mapping.get(slot, "a selected time")

def get_additional_info(apt_type):
    info_map = {
        "DF Mex": "- Most jobs take around 2 hours, which is an hour for each meter (if you only have an electricity meter it will take around an hour). Your electricity and gas will need to be switched off for up to an hour during this period.",
        "Elec Mex": "- Most jobs take around 1 hour. Your electricity will need to be switched off for up to an hour during this period.",
        "Gas Mex": "- Most jobs take around 1 hour. Your gas will need to be switched off for up to an hour during this period.",
        "Elec New Conn": "- Most jobs take around 1 hour.\n- You will need an electrician to attend after our engineer to connect the meter to the rest of the property.",
        "Gas New Conn": "- Most jobs take around 1 hour.\n- You will need a gas safety engineer to attend after our engineer to uncap the gas.",
        "DF new conn": "- Most jobs take around 2 hours, which is an hour for each meter.\n- You will need an electrician and a gas safety engineer to attend after our engineer to connect the electric meter to the rest of the property and to uncap the gas.",
        "On-Site comms": "",
        "Other": ""
    }
    return info_map.get(apt_type, "")

def sanitize_for_js(text):
    text = text.replace("\\", "\\\\")
    text = text.replace("`", "\\`")
    return text

# --- Generate Email ---
if st.button("Generate Email") and sender_name:
    apt_desc = get_appointment_description(appointment_type)
    slot_text = get_time_slot_text(time_slot)
    formatted_date = appointment_date.strftime("%A, %B %d, %Y")
    additional_info = get_additional_info(appointment_type)

    email_template = f"""Hi,

Thank you for speaking with me and I'm glad we could get you booked in for a {apt_desc}. As requested, we’ve booked your metering appointment for {formatted_date} between {slot_text}.

Just in regards to your appointment, here’s some additional information, and if any of these cause any issues, then give us a call or email.

{additional_info}
- Our engineer will give 30 minutes notice before their arrival.
- We’ll need someone over the age of 18 in the house throughout your appointment, even if your meter is located externally. This is so we can complete our safety checks inside your house before and after the work is completed. The person present doesn’t necessarily need to be the owner/occupier of the property. It can be a friend, neighbour or a family member.
- The engineer will need somewhere close by to park.
- If there are any obstructions / if the engineer will need a ladder to reach your meters, please let us know. The maximum height our engineers can work at is 7.2ft.
- If you have a dog, please ensure that it is securely kept away from the area where our engineer will be working.

If you have any questions between now and your appointment, please email us at hello@octoes.com.

Kind regards,
{sender_name}

Field Team Support Specialist
Octopus Energy Services
Feedback/Queries Email: hello@octoes.com"""

    # Display text area
    st.subheader("Generated Email")
    st.text_area("Email Body", email_template, height=500)

    # Copy-to-clipboard button
    safe_email = sanitize_for_js(email_template)

    copy_code = f"""
    <script>
    function copyToClipboard(text) {{
      navigator.clipboard.writeText(text).then(function() {{
        alert('Email copied to clipboard!');
      }}, function(err) {{
        alert('Failed to copy text: ', err);
      }});
    }}
    </script>

    <button onclick="copyToClipboard(`{safe_email}`)" style="
        background-color:#4CAF50;
        border:none;
        color:white;
        padding:10px 24px;
        text-align:center;
        text-decoration:none;
        display:inline-block;
        font-size:16px;
        border-radius:8px;
        cursor:pointer;
    ">
    📋 Copy Email to Clipboard
    </button>
    """

    components.html(copy_code, height=100)
