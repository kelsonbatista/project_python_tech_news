from tech_news.database import find_news


# Requisito 10
def top_5_news():
    filter = sorted(
        find_news(),
        key=lambda x: (-x["comments_count"], x["title"])
    )[:5]
    # print(json.dumps(filter, indent=4))
    return [(item["title"], item["url"]) for item in filter]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
