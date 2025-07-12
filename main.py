import requests
import json
from fake_useragent import UserAgent

def create_email(header_length, log_status, ua):
    emailCharCount = header_length
    url = "https://api.internal.temp-mail.io/api/v3/email/new"

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "application-name": "web",
        "application-version": "4.0.0",
        "content-type": "application/json",
        "User-Agent": ua
    }

    payload = {
        "min_name_length": emailCharCount,
        "max_name_length": emailCharCount
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if (log_status):
      if response.status_code == 200:
        print(f"Status Code {response.status_code} | Email Created ✅")
        print(f"Requested With | {ua}")
        print("Response JSON |", response.json())
    
    email = response.json().get('email', '')
    return email

def read_email(email, log_status, ua):
    url = f"https://api.internal.temp-mail.io/api/v3/email/{email}/messages"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "application-name": "web",
        "application-version": "4.0.0",
        "User-Agent": ua
    }

    response = requests.get(url, headers=headers)
    if log_status:
        if response.status_code == 200:
            print(f"Status Code {response.status_code} | Messages fetched ✅")
            print(f"Requested With | {ua}")
            print("Response JSON |", response.json())

    return response.json() if response.status_code == 200 else None

# Example usage:
#email_created = create_email(header_length=1, log_status=False, ua=UserAgent().random)
print("Created email:", email_created)

messages = read_email(email_created, log_status=False, ua=UserAgent().random)
print("Fetched messages:", messages)



