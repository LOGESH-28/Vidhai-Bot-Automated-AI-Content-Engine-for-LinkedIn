import requests

# Unga Token (Already filled)
access_token = "AQUcYXrNwyNjqEMH-H5XgUxRHpkvxaXrvi_-p1Q8ZbXUypcIBZ6H_UwF2FiPSdvUOwXXeV-gzVhCn2cM5JFR3ZIpcrNgbdCdOD2qs6O8Aq7kPVqLvg6nItIZQg6Ms0uKdi8pwu-tZwSwifK80uqu-RIZmVSRGizobHDCkNMkTb6ibpwzQqhont53mW8ojjI4IScREgzWGH1ZAuwCzi6UpFwDCDaFqKdzkRoKinHbjdP_ixfLZ7G3cSO1GDxqgbqZZuHfNJIurOFCZT67IeLCoGcCKhHNWafBnCYxVBMJQMGgjKVuA_pE1mIsov4z7ZaMp2TboikzbXRlHG8fVqdcRl1nvdnicA"

headers = {
    "Authorization": f"Bearer {access_token}"
}

# NEW Endpoint (OpenID Connect specific)
url = "https://api.linkedin.com/v2/userinfo"

try:
    print("⏳ Fetching User ID via OpenID...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        # In OpenID, the ID is stored in the 'sub' field
        user_id = data.get("sub")
        
        if user_id:
            final_urn = f"urn:li:person:{user_id}"
            print("\n✅ SUPER! Here is your LINKEDIN_USER_URN:\n")
            print(final_urn)
            print("\n(Idha copy panni vechukonga!)")
        else:
            print("❌ ID not found in response.")
            print(data)
    else:
        print("\n❌ Error fetching profile:")
        print(f"Status: {response.status_code}")
        print(response.json())

except Exception as e:
    print(f"Error: {e}")