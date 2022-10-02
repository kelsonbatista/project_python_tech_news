from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category
)
import sys


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
 7 - Sair."""

    option = input(MENU_OPTIONS)
    selection = ["1", "2", "3", "4", "5", "6", "7"]

    if option == "0":
        populate_news()
    elif option in selection:
        try:
            print(menu_scrape(option))
        except Exception as err:
            sys.stderr.write(err)
    else:
        sys.stderr.write("Opção inválida\n")


def populate_news():
    response = input("Digite quantas notícias serão buscadas:")
    get_tech_news(response.isdigit())
    return


def menu_scrape(option):
    if option == "1":
        response = input("Digite o título:")
        return search_by_title(response)
    elif option == "2":
        response = input("Digite a data no formato aaaa-mm-dd:")
        return search_by_date(response)
    elif option == "3":
        response = input("Digite a tag:")
        return search_by_tag(response)
    elif option == "4":
        response = input("Digite a categoria:")
        return search_by_category(response)
    else:
        menu_search(option)


def menu_search(option):
    if option == "5":
        return top_5_news()
    elif option == "6":
        return top_5_categories()
    elif option == "7":
        print("Encerrando script\n")
