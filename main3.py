import requests
import streamlit as st

# Function to check if the IP is private using ip-api
def check_ip_with_ipapi(ip):
    try:
        # Make a request to the ip-api service with the client's IP
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        # Check the response status and message
        if data['status'] == 'fail' and 'private' in data.get('message', '').lower():
            return True  # The IP is private
        return False  # The IP is not private
    except requests.RequestException as e:
        return False  # If there's an error with the API request, assume the IP is public

# Streamlit App
st.title("Check Origin")

# Inputs for testing
client_ip = st.text_input("Client IP", placeholder="Enter client IP address")
referer = st.text_input("Referer", placeholder="Enter the referer URL")
user_agent = st.text_input("User-Agent", placeholder="Enter the user-agent")
accept_language = st.text_input("Accept-Language", placeholder="Enter the accepted language")

# Action button to perform checks
if st.button("Check Origin"):
    # Check if the Referer is correct
    if referer != "https://greytechno.github.io/":
        st.error("Referer is incorrect.")
    else:
        # Check if the IP is private using the ip-api service
        if not check_ip_with_ipapi(client_ip):
            st.error("The IP is not private.")
        else:
            # All checks passed
            st.success("Caller site is correct.")
            st.json({
                "status": "success",
                "message": "Caller site is correct.",
                "client_ip": client_ip,
                "user_agent": user_agent,
                "referer": referer,
                "accept_language": accept_language
            })
