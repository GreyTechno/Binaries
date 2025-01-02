import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="https://greytechno.github.io")

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

@app.route("/check", methods=["GET"])
def check_origin():
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    referer = request.headers.get('Referer')
    accept_language = request.headers.get('Accept-Language')

    # Check if the Referer is correct
    if referer != "https://greytechno.github.io/":
        return jsonify({"status": "fail"}), 400
    
    # Check if the IP is private using the ip-api service
    if not check_ip_with_ipapi(client_ip):
        return jsonify({"status": "fail"})
    
    # All checks passed
    return jsonify({
        "status": "success",
        "message": "Caller site is correct.",
        "client_ip": client_ip,
        "user_agent": user_agent,
        "referer": referer,
        "accept_language": accept_language
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
