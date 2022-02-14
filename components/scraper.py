"""
This module contains web scraping functionality.
"""

import requests
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

gs_xobx = 'https://www.gamestop.com/consoles-hardware/xbox-series-x%7Cs/consoles/products/microsoft-xbox-series-x/224744'
headers = {
    "authority": "www.gamestop.com",
    "method": "GET",
    "path":
    "/consoles-hardware/xbox-series-x%7Cs/consoles/products/microsoft-xbox-series-x/224744.html?=undefined&bt=true",
    "scheme": "https",
    "accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua":
    """Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98""",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
} # yapf: disable

request = requests.get(gs_xobx, timeout=10, headers=headers)

with open(f"./html_files/{timestamp}.html", "w") as file:
    file.write(request.text)