from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
import bs4


def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService("/opt/chromedriver")

    options.binary_location = '/opt/chrome/chrome'
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")

    chrome = webdriver.Chrome(options=options, service=service)
    #url = "https://news.google.com/rss/articles/CBMiYmh0dHBzOi8vd3d3LnBvbGl0aWZhY3QuY29tL2FydGljbGUvMjAyNC9qdW4vMjUvY29tcGFyaW5nLWVjb25vbWljLXBlcmZvcm1hbmNlLWZvci1ibGFjay1hbWVyaWNhbnMv0gEA?oc=5"
    if 'url' in event:
        url = event['url']
        chrome.get(url)

        html = chrome.page_source
        soup = bs4.BeautifulSoup(html)

        text_data = []
        for tag in soup.find_all('p'):
            text_data.append(tag.text)
        return text_data
    else:
        url = "https://www.example.com"
        chrome.get(url)
        return chrome.find_element(by=By.XPATH, value="//html").text
