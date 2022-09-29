import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = len(selector.css(".comment-list li").getall())
    summary_original = selector.css(
        "div.entry-content > p:first-of-type *::text").getall()
    summary = "".join(summary_original).strip()
    tags = selector.css(".post-tags ul li a::text").getall()
    category = selector.css(".category-style span:nth_child(2)::text").get()

    news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category
    }
    # print(news)
    return news


# Requisito 5
def get_tech_news(amount):
    content = fetch("https://blog.betrybe.com/")
    all_news = []
    while scrape_next_page_link(content):
        all_news.extend(scrape_novidades(content))
        scrape_next_page_link(content)
    create_news(all_news)
