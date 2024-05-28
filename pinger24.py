import requests
import time

def ping_website(url):
    try:
        response = requests.get(url)
        print(f"Pinged {url}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error pinging {url}: {e}")

def start_pinging():
    website_url = 'https://aioo-3a2a.onrender.com/'  # Replace with the URL you want to ping
    while True:
        ping_website(website_url)
        time.sleep(40)

if __name__ == '__main__':
    start_pinging()
