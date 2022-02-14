"""Main script to notify if/when we buy an Xbox."""
import os
from datetime import datetime

from components.scraper import get_gs_xb_page

gs_request = get_gs_xb_page()

with open("./html_files/current.html", "w") as file:
    file.write(gs_request.text)

with open("./html_files/baseline.html", "r") as file:
    baseline = file.read()

if baseline == gs_request.text:
    print(f"Files are the same. {datetime.now()}")

else:
    print("Files are different.")