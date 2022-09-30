from tech_news.database import find_news
# import json


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
    categories = [item["category"] for item in find_news()]
    categories = sorted(list(
        {(cat, categories.count(cat)) for cat in categories}),
        key=lambda x: (-x[1], x[0]))
    categories_top = [cat[0] for cat in categories]
    return categories_top[:5]
