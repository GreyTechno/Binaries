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

# Fetch the client's public IP
def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        return response.json().get("ip", "Unknown IP")
    except requests.RequestException:
        return "Unknown IP"

# Streamlit App
st.title("Check Origin")

# Automatically get the public IP
client_ip = get_public_ip()

# Simulated request headers
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
referer = "https://greytechno.github.io/"
accept_language = "en-US,en;q=0.9"

# Display client details
st.subheader("Client Details")
st.write(f"Client IP: {client_ip}")
st.write(f"Referer: {referer}")
st.write(f"User-Agent: {user_agent}")
st.write(f"Accept-Language: {accept_language}")

# Perform checks automatically
st.subheader("Validation Results")
if referer != "https://greytechno.github.io/":
    st.error("Referer is incorrect.")
else:
    if not check_ip_with_ipapi(client_ip):
        st.error("The IP is not private.")
    else:
        st.success("Caller site is correct.")
        st.json({
            "status": "success",
            "message": "Caller site is correct.",
            "client_ip": client_ip,
            "user_agent": user_agent,
            "referer": referer,
            "accept_language": accept_language
        })
