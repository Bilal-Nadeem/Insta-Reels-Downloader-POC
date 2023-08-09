from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests

with open("insta-links.txt", "r") as f:
    urls = f.read().strip().split("\n")

with sync_playwright() as p:
    browser = p.chromium.launch()
    for i, url in enumerate(urls):
        try:
            page = browser.new_page()
            page.goto(url, timeout = 0)
            page.wait_for_selector("video")
            html = page.content()
            soup = BeautifulSoup(html, 'html.parser')
            src = soup.find('video')['src']
            src = src.replace('amp;', '')
            
            r = requests.get(src)

            with open(f"insta-vids/{i}.mp4", "wb") as f:
                f.write(r.content)

            print(f"[{i}] Sucessfully Downloaded")
        except:
            print(f"[{i}] Failed, skipping to next one.")    

        print('------------------------------------------------------------------------------------------------------------------')
            