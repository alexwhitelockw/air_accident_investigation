from random import randint
import requests
from time import sleep

from functions.report_downloader import load_json, load_viewed_links, save_viewed_link, sanitise_title, download_pdf


if __name__ == "__main__":
    
    report_link_data = load_json("data/source_data/report_links/air_accident_reports.json")
    viewed_link_data = load_viewed_links("data/source_data/viewed_links/viewed_links.txt")

    for link_data in report_link_data:
        report_title = link_data.get("title")
        pdf_link = link_data.get("pdf_link")
        report_title = sanitise_title(report_title)

        pdf_file_name = f"{report_title}.pdf"

        if pdf_link not in viewed_link_data:
            sleep(randint(1, 10))
            save_viewed_link("data/source_data/viewed_links/viewed_links.txt", pdf_link)
            download_pdf(f"data/source_data/report_content/{pdf_file_name}", pdf_link)
