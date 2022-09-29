from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    filter = search_news({"title": {"$regex": f"{title.lower()}"}})
    return [(item["title"], item["url"]) for item in filter]


# Requisito 7
def search_by_date(date):
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        filter = search_news(
            {"timestamp": {"$regex": f"{new_date}"}}
        )
        return [(item["title"], item["url"]) for item in filter]
    except ValueError:
        raise ValueError("Data inválida")


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
