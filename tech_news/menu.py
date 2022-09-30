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

    while (True):
        user_input = input(MENU_OPTIONS)

        try:
            if user_input == 0:
                response = input("Digite quantas notícias serão buscadas:")
                get_tech_news(int(response))
                return
            elif user_input == 1:
                response = input("Digite o título:")
                print(search_by_title(response))
                return
            elif user_input == 2:
                response = input("Digite a data no formato aaaa-mm-dd:")
                print(search_by_date(response))
                return
            elif user_input == 3:
                response = input("Digite a tag:")
                print(search_by_tag(response))
                return
            elif user_input == 4:
                response = input("Digite a categoria:")
                print(search_by_category(response))
                return
            elif user_input == 5:
                print(top_5_news())
                return
            elif user_input == 6:
                print(top_5_categories())
                return
            elif user_input == 7:
                print("Encerrando script")
                return False
        except ValueError:
            print("Opção inválida")
