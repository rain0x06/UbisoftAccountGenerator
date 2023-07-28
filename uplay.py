import requests, json, base64, os, random, string, time, sys, datetime
from os import system

system("title " + "Rain's Ubisoft Account Tool")

ticketv1 = ""
sessionid = ""
upname = ""

def parse_response(response):
    try:
        return response.json()
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        print(f"Response content: {response.content}")
        return None

def generate_random_number():
    return str(random.randint(1000, 99999))

def generate_random_username():
    return "RainTM.YTv" + generate_random_number() ## replace with whatever random username you want

def generate_random_email():
    return "fdkalv+" + generate_random_number() + "@gmail.com" ## replace with whatever email you want to own the account

def b64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def create_account(email, password, username):
    os.system("cls")
    post_url = "https://public-ubiservices.ubi.com/v3/users/validatecreation"
    post_url1 = "https://public-ubiservices.ubi.com/v1/users"
    post_headers = {
        "Ubi-AppId": "e3d5ea9e-50bd-43b7-88bf-39794f4e3d40", #iykyk
        "Ubi-Requestedplatformtype": "uplay",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "content-type": "application/json"
    }
    
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    generated_account_info = f"Generated Account at {current_datetime} | {email} | {password} | {username}"

    data = {
        "age": "21",
        "confirmedEmail": email,
        "country": "US",
        "dateofBirth": "2001-09-11T00:00:00.00000Z",
        "email": email,
        "firstName": "RainGenerated",
        "isDateOfBirthApprox": "false",
        "lastName": "RainGenerated",
        "legaloptinskey": "eyJ2dG91IjoiNC4wIiwidnBwIjoiNC4xIiwidnRvcyI6IjIuMSIsImx0b3UiOiJlbi1VUyIsImxwcCI6ImVuLVVTIiwibHRvcyI6ImVuLVVTIn0", # may need to change if in diff country
        "password": password,
        "preferredLanguage": "en",
        "username": username
    }

    try:
        post_response = requests.post(post_url, headers=post_headers, json=data)
        post_response.raise_for_status()
        data1 = parse_response(post_response)
        print(f"Response: {data1}\n")
    except requests.RequestException as e:
        print(f"An error occurred during account creation: {e}")
        print(f"\nResponse: {data2}\n")
        return None

    try:
        post_response1 = requests.post(post_url1, headers=post_headers, json=data)
        post_response1.raise_for_status()
        data2 = parse_response(post_response1)
        print(f"Response: {data2}\n")
    except Exception as e:
        print(f"An error occurred during account creation: {e}")
        print(f"\nResponse: {data2}\n")
        return None
    
    print("Email:", email)
    print("Password:", password)
    
    with open("generated_accounts.txt", "a") as file:
        file.write(generated_account_info + "\n")
    
    print("\nAccount information written to file, copy if needed.")
    
    print("Choose an option:")
    print("1. Login to generated account")
    print("2. Go back to main menu")
    
    choice = input("\nChoice: ")

    if choice == '1':
        login_account(email, password)
    else:
        os.system("cls")
    

def login_account(email, password):
    os.system("cls")

    url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"
    headers = {
        "Ubi-AppId": "e3d5ea9e-50bd-43b7-88bf-39794f4e3d40",
        "Authorization": "Basic " + base64.b64encode((email + ":" + password).encode()).decode(),
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
        print("There may have been an error in your login, please relaunch the program and try again.\nOR you have been rate-limited, please wait ~5 minutes and try again.")
        return

    if ticketv1 == "":
        print("Script will close in 3 seconds.")
        time.sleep(3)
        sys.exit("Invalid ticket OR rate limit.")
    else:
        os.system("cls")
        print(f"Logged into account with username \033[1;36;40m{upname}\033[0;37;40m\n")
        time.sleep(1)
        print(data)
        os.system("pause")

if __name__ == "__main__":
    while True:
        os.system("cls")

        print("Choose an option:")
        print("1. Generate a new account")
        print("2. Login to an existing account")
        print("3. Exit the script")

        choice = input("\nChoice: ")

        if choice == '1':
            # make a new acc
            os.system("cls")
            use_default = input("Do you want to use auto-generated account information as your login? (y/n): ").lower()

            if use_default == "y":
                email = generate_random_email()
                password = "RainTM27!"
                username = generate_random_username()
            else:
                email = input("\nEnter an email: ")
                password = input("Enter a password: ")
                username = input("Enter your desired username: ")

            create_account(email, password, username)
        elif choice == '2':
            # login to existing acc
            email = input("Enter your Ubisoft Email: ")
            password = input("Enter your Ubisoft Password: ")
            login_account(email, password)
        elif choice == '3':
            os.system("cls")
            print("Exiting the script. Goodbye!")
            break  # exit
        else:
            os.system("cls")
            print("Invalid choice. Please select a valid option (1, 2, or 3).")
