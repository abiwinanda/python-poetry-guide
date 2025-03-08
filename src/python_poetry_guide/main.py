import requests

def get_public_ip():
    try:
        response = requests.get("https://ifconfig.me", timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes
        print("Your public IP is:", response.text)
    except requests.RequestException as e:
        print("Error fetching IP:", e)

def main():
    get_public_ip()

if __name__ == "__main__":
    get_public_ip()
