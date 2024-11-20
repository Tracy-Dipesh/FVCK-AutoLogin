import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Cool ASCII Art Banner
def print_banner():
    banner = r"""
      ███████╗██╗   ██╗ ██████╗██╗  ██╗
      ██╔════╝██║   ██║██╔════╝██║ ██╔╝
      █████╗  ██║   ██║██║     █████╔╝ 
      ██╔══╝  ╚██╗ ██╔╝██║     ██╔═██╗ 
      ██╗       ╚████╔╝ ╚██████╗██║  ██╗
      ╚═         ╚═══╝   ╚═════╝╚═╝  ╚═╝
    """
    print(banner)
    print(">>> WELCOME TO THE F U C K TOOL <<<\n")

# Auto-Retry Function
def attempt_login(session, login_page_url, username, password, csrf_token, retries):
    for attempt in range(retries):
        print(f"[*] Attempt {attempt + 1} of {retries}...")
        payload = {
            "username": username,
            "password": password,
            "csrf": csrf_token
        }
        response = session.post(login_page_url, data=payload)

        if response.status_code == 200:
            if "Congratulations" in response.text:
                print("[+] Login Successful: Taile hack garis")
                return response  # Return the response object of the redirected page
            else:
                print("[-] Login Failed: Tero hack kam garena")
        else:
            print(f"[-] Unexpected Status Code: {response.status_code}")
    return None

# Save HTML to File
def save_html(response, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    print(f"[+] HTML content of the redirected page saved to: {output_path}")

# Main Code
print_banner()

# Prompt the user for the login page URL
login_page_url = input("Enter the URL of the login page: ")

session = requests.Session()
login_page = session.get(login_page_url)

if login_page.status_code == 200:
    # Parse the CSRF token
    soup = BeautifulSoup(login_page.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]

    # Get username and password inputs
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Ask for number of retries
    retries = int(input("Enter number of retries: "))

    # Log the timestamp of the login attempt
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[*] Login attempt started at: {login_time}\n")

    # Call the auto-retry function
    response = attempt_login(session, login_page_url, username, password, csrf_token, retries)

    if response:
        # Ask for the output file path
        output_path = input("Enter the path to save the HTML file (e.g., /path/to/output.html): ")

        # Save the HTML content of the redirected page
        save_html(response, output_path)
    else:
        print("[!] All attempts failed. Better luck next time!")
else:
    print(f"[-] Failed to fetch login page with status code: {login_page.status_code}")
