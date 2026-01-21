import requests

# Configuration
url = "https://www.linkedin.com/oauth/v2/accessToken"

# Unga Details
payload = {
    "grant_type": "authorization_code",
    "code": "AQTfQNx9ewfqEJl_h3Gg75i0jTFHf3JZiW86b8j707IxmWG3eKdbWImoLHcl_9n0EmeoFVZor1lJ_LvCC5HHmT4K2BCe3T8JRDadX6N8rt_bEvZG9MPEg-iNM8Q4USKvAO1dUE7q6wrqtWdmXthlkI887v2ZE-v9MyY9QDtx7NIpPMQgLzP7axvqDPSVJaAS6TMXm1Ad4WmGK9rX8Z0",
    "redirect_uri": "https://www.google.com",
    "client_id": "86xdubh9lqip47",
    "client_secret": "WPL_AP1.TWeABzZrKLyylhHF.FmgBpA=="  # <-- Inga unga Secret podunga!
}

# Requesting Token
try:
    response = requests.post(url, data=payload)
    data = response.json()
    
    if "access_token" in data:
        print("\n🎉 SUCCESS! Here is your Access Token:\n")
        print(data["access_token"])
        print("\n(Save this token immediately!)\n")
    else:
        print("\n❌ Error generating token:")
        print(data)
except Exception as e:
    print(f"Error: {e}")