import requests, json, base64, time, sys, os, random, string
from os import system

system("title " + "Rain's Ubisoft Account Generator")

lines = f" \n \n \n \n "
ticketv1 = ""
sessiond = ""
upname = ""
timerval = ""
timer = ""
count = 1

namecheck_av = ""
index = "20000000"

def generate_random_number():
    return str(random.randint(1000, 99999))

def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(12))

os.system("cls")
print("")

post_url = "https://public-ubiservices.ubi.com/v3/users/validatecreation"
post_url1 = "https://public-ubiservices.ubi.com/v1/users"
post_headers = {
    "Ubi-AppId": "e3d5ea9e-50bd-43b7-88bf-39794f4e3d40", ## iykyk
    "Ubi-Requestedplatformtype": "uplay",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "content-type": "application/json"
}

use_default = input("Do you want to use the auto-generated account information? (y/n): ").lower()

if use_default == "y":
    email = "rain0x06+" + generate_random_number() + "@gmail.com"
    password = "RainTMOwnsMe2#$"
    username = "RainTM.YTv" + generate_random_number()
else:
    email = input("Enter an email: ")
    password = input("\nEnter a password: ")
    username = input("\nEnter your desired username: ")

data = {
    "age": "18",
    "confirmedEmail": email,
    "country": "US",
    "dateofBirth": "1999-09-09T00:00:00.00000Z",
    "email": email,
    "firstName": "RainGenerated",
    "isDateOfBirthApprox": "false",
    "lastName": "RainGenerated",
    "legaloptinskey": "eyJ2dG91IjoiNC4wIiwidnBwIjoiNC4xIiwidnRvcyI6IjIuMSIsImx0b3UiOiJlbi1VUyIsImxwcCI6ImVuLVVTIiwibHRvcyI6ImVuLVVTIn0", ## change if in a different country
    "password": password,
    "preferredLanguage": "en",
    "username": username
}

def parse_response(response):
    try:
        return json.loads(response.content)
    except json.decoder.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        print(f"Response content: {response.content}")
        return None

# Validate account creation
post_response = requests.post(post_url, headers=post_headers, json=data)
data1 = parse_response(post_response)
print(f"\nResponse: {data1}\n")

input("Press enter to continue if successful. If an error code was printed, your desired username or email may already be used.")

# Create the account
post_response1 = requests.post(post_url1, headers=post_headers, json=data)
data2 = parse_response(post_response1)
print(f"Response: {data2}\n")
input("Press enter to continue if successful.")

def b64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"
headers = {
    "Ubi-AppId": "e3d5ea9e-50bd-43b7-88bf-39794f4e3d40",
    "Authorization": "Basic " + b64(email + ":" + password),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "content-type": "application/json"
}

resp = requests.post(url, headers=headers)
data = parse_response(resp)
try:
    ticketv1 = data['ticket']
    sessionid = data['sessionId']
    upname = data['nameOnPlatform']
except Exception:
    print(f"there may have been an error in your login, please relaunch the program and try again.\nOR you have been rate-limited, please wait ~5 minutes and try again.\n")

if ticketv1 =="":
    print("API TOOL will close in 3 seconds.")
    time.sleep(3)
    sys.exit("invalid ticket OR rate limit.")
else:
    os.system("cls")
    print(f"Logged into user \033[1;36;40m{upname}\033[0;37;40m")
    time.sleep(1)
    print("Extracting required information.")
    time.sleep(1)
    os.system("cls")
    print(f"Full data: {data}\n")
    os.system("pause")
    os.system("cls")
    print("Email:", email)
    print("Password:", password)
    input("Press enter to exit the script.")
