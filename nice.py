from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests

from dataclasses import dataclass
from typing import List, Optional

geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'

def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as t23oiiuot:
    t23oiiuot.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    t23oiiuot.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    #t23oiiuot.set_window_size(resolution.width, resolution.height)
    url = "https://www.twitch.tv/brutalles"
    t23oiiuot.uc_open_with_reconnect(url, 4)
    t23oiiuot.sleep(4)
    if is_stream_online("brutalles"):
        url = "https://www.twitch.tv/brutalles"
        #t23oiiuot.uc_open_with_reconnect(url, 5)
        if t23oiiuot.is_element_present('button:contains("Accept")'):
            t23oiiuot.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            t23oiiuot2 = t23oiiuot.get_new_driver(undetectable=True)
            t23oiiuot2.uc_open_with_reconnect(url, 5)
            t23oiiuot.sleep(10)
            if t23oiiuot2.is_element_present('button:contains("Accept")'):
                t23oiiuot2.uc_click('button:contains("Accept")', reconnect_time=4)
            while is_stream_online("brutalles"):
                t23oiiuot.sleep(100)
            t23oiiuot.quit_extra_driver()
    t23oiiuot.sleep(1)

