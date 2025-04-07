import ssl
import socket
import sys

def check_https(domain):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(3)
            s.connect((domain, 443))
        return True
    except:
        return False

def main(filename):
    with open(filename, "r") as file:
        domains = file.read().splitlines()

    for domain in domains:
        if check_https(domain):
            print(f"[✓] {domain} supports HTTPS")
        else:
            print(f"[✗] {domain} does NOT support HTTPS")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 cek_https.py <file>")
    else:
        main(sys.argv[1])
