import sys
import os
import yaml
import urllib
import flask
import urllib3
from urllib.parse import urlparse
import socket
import ipaddress

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person:
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


#fixed issue 


def is_ip_safe(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return not (
            ip_obj.is_private or
            ip_obj.is_loopback or
            ip_obj.is_link_local or
            ip_obj.is_multicast or
            ip_obj.is_reserved
        )
    except ValueError:
        return False

def resolve_and_validate_url(url):
    parsed = urlparse(url)
    if not parsed.scheme.startswith("http"):
        raise ValueError("Only HTTP(S) allowed")

    hostname = parsed.hostname
    try:
        ip = socket.gethostbyname(hostname)
        if not is_ip_safe(ip):
            raise ValueError("Blocked unsafe destination IP")
        return url
    except Exception:
        raise ValueError("Invalid or unsafe URL")

def fetch_website(url):
    # Validate and resolve IP before sending request
    safe_url = resolve_and_validate_url(url)
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', safe_url, timeout=2.0)
        print(response.data.decode())
    except Exception as e:
        print(f"Request failed: {e}")




def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data

def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice  = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)

