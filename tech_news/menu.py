from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category
)


# Requisito 12
def analyzer_menu():
    MENU_OPTIONS = """
    Selecione uma das opções a seguir:
    0 - Popular o banco com notícias;
    1 - Buscar notícias por título;
    2 - Buscar notícias por data;
    3 - Buscar notícias por tag;
    4 - Buscar notícias por categoria;
    5 - Listar top 5 notícias;
    6 - Listar top 5 categorias;
    7 - Sair.
    """

    option = input(MENU_OPTIONS)

    if int(option) == 0:
        populate_news()
    if 1 <= int(option) <= 4:
        return menu_scrape(option)
    if 5 <= int(option) <= 6:
        return menu_search(option)
    if option == 7:
        return menu_exit()
    else:
        print("Opção inválida")


def populate_news():
    response = input("Digite quantas notícias serão buscadas:")
    get_tech_news(int(response))
    return


def menu_scrape(option):
    if option == "1":
        response = input("Digite o título:")
        print(search_by_title(response))
        return

    if option == "2":
        response = input("Digite a data no formato aaaa-mm-dd:")
        print(search_by_date(response))
        return

    if option == "3":
        response = input("Digite a tag:")
        print(search_by_tag(response))
        return
    if option == "4":
        response = input("Digite a categoria:")
        print(search_by_category(response))
        return


def menu_search(option):
    if option == "5":
        print(top_5_news())
        return

    if option == "6":
        print(top_5_categories())
        return


def menu_exit():
    print("Encerrando script")
    return False


analyzer_menu()
