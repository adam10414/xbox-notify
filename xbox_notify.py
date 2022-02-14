"""Main script to notify if/when we buy an Xbox."""

from components.scraper import get_gs_xb_page

gs_request = get_gs_xb_page()

with open("./html_files/baseline.html", "w") as file:
    file.write(gs_request.text)