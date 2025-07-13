# !pip install fake-useragent

import requests
import json
from fake_useragent import UserAgent # optional usage

#endpoints 
XENDPOINT_CREATE_NEW_EMAIL = "https://api.internal.temp-mail.io/api/v3/email/new"
XENDPOINT_READ_MESSAGES = "https://api.internal.temp-mail.io/api/v3/email/[email]/messages"
XENDPOINT_DOMAIN_LIST = "https://api.internal.temp-mail.io/api/v4/domains"

def create_custom_email(name, domain, log_status, ua):
    url = XENDPOINT_CREATE_NEW_EMAIL

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "application-name": "web",
        "application-version": "4.0.0",
        "content-type": "application/json",
        "User-Agent": ua
    }

    payload = {
        "name": name,
        "domain": domain
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if "email" in data:
            if (log_status):
                if response.status_code == 200:
                    print(f"Status Code {response.status_code} | Email Created ✅")
                    print(f"Requested With | {ua}")
                    print("Response JSON |", response.json())
            return data["email"]
        else:
            print("Failed to create custom email:", data)
            return None
    except requests.RequestException as e:
        print("Error occurred:", e)
        return None

def create_random_email(header_length, log_status, ua):
    emailCharCount = header_length
    url = XENDPOINT_CREATE_NEW_EMAIL

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
    url = XENDPOINT_READ_MESSAGES.replace("[email]", email)

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

def fetch_domain_list(ua):
    url = XENDPOINT_DOMAIN_LIST
    try:
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "application-name": "web",
            "application-version": "4.0.0",
            "User-Agent": ua
        }  

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        domain_names = [domain['name'] for domain in data.get('domains', [])]
        return domain_names
    except requests.exceptions.RequestException as e:
        print(f"Error fetching domains: {e}")
        return []

# Usage:
email_created = create_random_email(header_length=1, log_status=False, ua=UserAgent().random)
print("Created email:", email_created)

messages = read_email(email_created, log_status=False, ua=UserAgent().random)
print("Fetched messages:", messages)

domains = fetch_domain_list(ua=UserAgent().random)
print("Domains Available [v4]:",domains)

custom_email_created = create_custom_email(name="jake", domain="something.com", log_status=True, ua=UserAgent().random)
print("Created custom email:", custom_email_created)