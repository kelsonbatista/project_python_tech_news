from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    filter = search_news({"title": {"$regex": f"{title.lower()}"}})
    return [(item["title"], item["url"]) for item in filter]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    filter = search_news({"tags": {"$regex": f"{tag.lower().capitalize()}"}})
    return [(item["title"], item["url"]) for item in filter]


# Requisito 9
def search_by_category(category):
    filter = search_news(
        {"category": {"$regex": f"{category.lower().capitalize()}"}}
    )
    return [(item["title"], item["url"]) for item in filter]
