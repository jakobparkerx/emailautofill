import streamlit as st
import html

def transform_elec(b4: str) -> str:
    b10 = "FF1122331C234F0000-CCDDEE00"
    first_part, second_part = b10.split("-", 1)
    cleaned_b4 = b4[-9:].replace("-", "")
    return first_part + cleaned_b4 + second_part

def transform_gas(b4: str) -> str:
    b10 = "FF1122334411020000-CCDDEE00"
    first_part, second_part = b10.split("-", 1)
    cleaned_b4 = b4[-9:].replace("-", "")
    return first_part + cleaned_b4 + second_part

# Apply consistent modern font
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
                     Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("EDMI Install Code Generator")

# Two columns: Elec and Gas
col1, col2 = st.columns(2)

# --- Column 1: Electric ---
with col1:
    st.subheader("Electric")
    b4_input_elec = st.text_input("Enter Elec GUID", key="elec")

    if st.button("Create Electric Install Code"):
        result_elec = transform_elec(b4_input_elec)
        escaped_result_elec = html.escape(result_elec)

        st.markdown(f"""
        <div style="
            background-color: #f8f9fa;
            padding: 16px;
            border-radius: 10px;
            border: 1px solid #ccc;
            font-family: inherit;
            font-size: 18px;
            color: #333;
            word-break: break-word;
            margin-top: 20px;
        ">
            {escaped_result_elec}
        </div>
        """, unsafe_allow_html=True)

# --- Column 2: Gas ---
with col2:
    st.subheader("Gas")
    b4_input_gas = st.text_input("Enter Gas GUID", key="gas")

    if st.button("Create Gas Install Code"):
        result_gas = transform_gas(b4_input_gas)
        escaped_result_gas = html.escape(result_gas)

        st.markdown(f"""
        <div style="
            background-color: #f8f9fa;
            padding: 16px;
            border-radius: 10px;
            border: 1px solid #ccc;
            font-family: inherit;
            font-size: 18px;
            color: #333;
            word-break: break-word;
            margin-top: 20px;
        ">
            {escaped_result_gas}
        </div>
        """, unsafe_allow_html=True)
