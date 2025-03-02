import requests
import time
def fall_noti():
    """
    Updates a Blynk virtual pin by toggling its value between 0 and 1 once.

    :param auth_token: Your Blynk authentication token (str).
    :param virtual_pin: The virtual pin number to update (int).
    """
    auth_token = 'M8_byPTDfTw-9nLb80nOMJRcCmcaHycJ'  # Replace with your Blynk Auth Token
    virtual_pin = 0  # Replace with your virtual pin number
    blynk_url = f"https://blynk.cloud/external/api/update?token={auth_token}&V{virtual_pin}="
    drop_value = 1  # Value to set

    try:
        # Send the HTTP request
        response = requests.get(blynk_url + str(drop_value))

        # Check response
        if response.status_code == 200:
            print(f"Virtual Pin V{virtual_pin} ('drop') successfully set to {drop_value}")
        else:
            print(f"Error: Unable to update V{virtual_pin}. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        time.sleep(1)
        response = requests.get(blynk_url + str(~drop_value))

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
