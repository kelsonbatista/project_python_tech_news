import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    sleep(1)

    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    if response.status_code == 200:
        return response.text
    return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    titles = selector.css("h2 a::attr(href)").getall()
    if not titles:
        print(titles)
        return []
    return titles


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    page_url = selector.css(".next.page-numbers::attr(href)").get()
    return page_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


html_content = fetch("https://blog.betrybe.com/")
scrape_next_page_link(html_content)
