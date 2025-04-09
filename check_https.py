import requests
import sys

def check_url(domain):
    result = {
        "domain": domain,
        "http": False,
        "https": False,
        "redirects": False
    }

    try:
        r_http = requests.get(f"http://{domain}", timeout=5, allow_redirects=True)
        result["http"] = True

        if r_http.url.startswith("https://"):
            result["redirects"] = True
    except requests.RequestException:
        pass

    try:
        r_https = requests.get(f"https://{domain}", timeout=5)
        result["https"] = True
    except requests.RequestException:
        pass

    return result

def main(filename):
    with open(filename, "r") as file:
        domains = file.read().splitlines()

    redirected = []
    only_http = []
    only_https = []
    both = []
    none = []

    for domain in domains:
        status = check_url(domain)
        http = status["http"]
        https = status["https"]
        redirects = status["redirects"]

        if redirects:
            redirected.append(domain)
            print(f"[↪️] {domain} redirect dari HTTP ke HTTPS")
        elif http and https:
            both.append(domain)
            print(f"[✓✓] {domain} mendukung HTTP & HTTPS")
        elif http:
            only_http.append(domain)
            print(f"[→] {domain} hanya HTTP")
        elif https:
            only_https.append(domain)
            print(f"[🔒] {domain} hanya HTTPS")
        else:
            none.append(domain)
            print(f"[✗] {domain} tidak bisa diakses")

    with open("redirected_to_https.txt", "w") as f:
        f.write("\n".join(redirected))
    with open("only_http.txt", "w") as f:
        f.write("\n".join(only_http))
    with open("only_https.txt", "w") as f:
        f.write("\n".join(only_https))
    with open("both_http_https.txt", "w") as f:
        f.write("\n".join(both))
    with open("none.txt", "w") as f:
        f.write("\n".join(none))

    print("\n✅ Semua hasil sudah disimpan ke file!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_url.py <file>")
    else:
        main(sys.argv[1])
