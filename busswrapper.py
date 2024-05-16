import requests
from rich import print_json

s = requests.Session()
s.headers = {"Content-Type": "application/json"}


def register(domain, tld, ip):
    resp = s.post(
        "https://api.buss.lol/domain", json={"domain": domain, "tld": tld, "ip": ip}
    )

    return resp.json()


def update(key, ip):
    resp = s.put("https://api.buss.lol/domain/" + key, json={"ip": ip})

    return resp.json()


def get(domain):
    domain, tld = domain.split(".")

    resp = s.get("https://api.buss.lol/domain/" + domain + "/" + tld)

    return resp.json()


def get_all():
    resp = s.get("https://api.buss.lol/domains")

    return resp.json()


while True:
    print("1. Register")
    print("2. Update")
    print("3. Get")
    print("4. Get all")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        domain = input("Enter domain: ")
        tld = input("Enter tld: ")
        ip = input("Enter ip: ")
        resp = register(domain, tld, ip)
        print_json(data=resp)
    elif choice == "2":
        key = input("Enter key: ")
        ip = input("Enter ip: ")
        resp = update(key, ip)
        print_json(data=resp)
    elif choice == "3":
        domain = input("Enter domain: ")
        resp = get(domain)
        print_json(data=resp)
    elif choice == "4":
        resp = get_all()
        print_json(data=resp)
    elif choice == "5":
        break

    else:
        print("Invalid choice")
