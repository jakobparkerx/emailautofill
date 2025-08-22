import streamlit as st
import datetime
import logging

logging.getLogger('streamlit').setLevel(logging.CRITICAL)

# Create two tabs
tab1, tab2 = st.tabs(["Appointment Email", "D-1 Email"])

# ---------------- Tab 1: Appointment Email ----------------
with tab1:
    st.title("Appointment Email Generator")

    TIME_SLOTS = ["AD (8am - 5pm)", "AM (8am - 12pm)", "PM (1pm - 5pm)"]
    APPOINTMENT_TYPES = [
        "DF Mex", "Elec Mex", "Gas Mex", "Elec New Conn",
        "Gas New Conn", "DF new conn", "On-Site comms"
    ]

    date_tab1 = st.date_input("Appointment date", datetime.date.today(), key="appt_date_tab1")
    formatted_date_tab1 = date_tab1.strftime('%d/%m/%Y')
    st.write(f"Selected date (formatted): {formatted_date_tab1}")

    time_slot_tab1 = st.selectbox("Time slot", TIME_SLOTS, key="time_slot_tab1")
    appointment_type_tab1 = st.selectbox("Appointment type", APPOINTMENT_TYPES, key="appt_type_tab1")
    your_name_tab1 = st.text_input("Your name", key="your_name_tab1")

    generate_tab1 = st.button("Generate Appointment Email", key="generate_tab1")

    if generate_tab1:
        if not your_name_tab1:
            st.error("Please enter your name.")
        else:
            time_mapping = {
                "AD": "8am - 5pm",
                "AM": "8am - 12pm",
                "PM": "1pm - 5pm"
            }
            time_value = time_mapping.get(time_slot_tab1[:2], "a selected time")

            appointment_mapping = {
                "DF Mex": "a gas and electric meter exchange",
                "Elec Mex": "an electric meter exchange",
                "Gas Mex": "a gas meter exchange",
                "Elec New Conn": "an electric new connection",
                "Gas New Conn": "a gas new connection",
                "DF new conn": "a gas and electric new connection",
                "On-Site comms": "an on-site commissioning appointment for your smart meters"
            }

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

            appointment_desc = appointment_mapping.get(appointment_type_tab1, "an appointment")
            additional = additional_info.get(appointment_type_tab1, "")

            email_tab1 = f"""Hi,

Thank you for speaking with me and I'm glad we could get you booked in for {appointment_desc}. As requested, we’ve booked your metering appointment for {formatted_date_tab1} between {time_value}.

Just in regards to your appointment, here’s some additional information, and if any of these cause any issues, then give us a call or email.

{additional}
- Our engineer will give 30 minutes notice before their arrival.
- We’ll need someone over the age of 18 in the house throughout your appointment, even if your meter is located externally. This is so we can complete our safety checks inside your house before and after the work is completed. The person present doesn’t necessarily need to be the owner/occupier of the property. It can be a friend, neighbour or a family member.
- The engineer will need somewhere close by to park.
- If there are any obstructions / if the engineer will need a ladder to reach your meters, please let us know. The maximum height our engineers can work at is 7.2ft.
- If you have a dog, please ensure that it is securely kept away from the area where our engineer will be working.

If you have any questions between now and your appointment, please email us at hello@octoes.com.

Kind regards,  
{your_name_tab1}

Customer Support Specialist
Octopus Energy Services
Feedback/Queries Email: hello@octoes.com
"""
            st.markdown(f"```markdown\n{email_tab1}\n```")

# ---------------- Tab 2: D-1 Email ----------------
with tab2:
    st.title("D-1 Email Generator")

    date_tab2 = st.date_input("Appointment date", datetime.date.today(), key="appt_date_tab2")
    formatted_date_tab2 = date_tab2.strftime('%d/%m/%Y')
    st.write(f"Selected date (formatted): {formatted_date_tab2}")

    time_range_tab2 = st.slider(
        "Select your engineer arrival time range",
        value=(datetime.time(9, 0), datetime.time(12, 0)),
        step=datetime.timedelta(minutes=15),
        format="HH:mm",
        key="time_range_tab2"
    )

    start_time_tab2, end_time_tab2 = time_range_tab2
    st.write(f"Selected: {start_time_tab2.strftime('%I:%M %p')} - {end_time_tab2.strftime('%I:%M %p')}")

    your_name_tab2 = st.text_input("Your name", key="your_name_tab2")

    generate_tab2 = st.button("Generate D-1 Email", key="generate_tab2")

    if generate_tab2:
        if not your_name_tab2:
            st.error("Please enter your name.")
        else:
            email_tab2 = f"""Hi,

I hope you are well today. I'm reaching out regarding the upcoming metering appointment, which we currently have booked with you for {formatted_date_tab2}. Our engineer has let us know that they plan to attend between {start_time_tab2.strftime('%I:%M %p')} and {end_time_tab2.strftime('%I:%M %p')}.

If you have any questions regarding this, please let me know!

Kind regards,  
{your_name_tab2}

Customer Support Specialist
Octopus Energy Services
Feedback/Queries Email: hello@octoes.com
"""
            st.markdown(f"```markdown\n{email_tab2}\n```")




















