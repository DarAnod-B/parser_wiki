import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote


def parser(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def parser_next_link():
    # Последняя нужная нам ссылка
    if url == unquote(
            'https://ru.wikipedia.org//w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=Zosterops+modestus&filefrom=А&subcatuntil=А#mw-pages') or url == 'https://ru.wikipedia.org//w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=Zosterops+modestus&filefrom=%D0%90&subcatuntil=%D0%90#mw-pages':
        return ''
    soup = parser(url)
    get_word(soup)
    result_a = soup.find_all('a', {'title': 'Категория:Животные по алфавиту'})
    for i in result_a:
        i = unquote(i)
        if i.get_text() == 'Следующая страница':
            link = unquote('https://ru.wikipedia.org/' + i.get('href'))
            # Нам нужна, только первая ссылка т.к. вторая её дублирует
            break
    return unquote(link)


def get_word(soup):
    result_div = soup.find_all('div', {'id': 'mw-pages'})
    for i in result_div:
        result_li = i.find_all('li')
        for j in result_li:
            wiki_word.append(j.text)


wiki_link = [
    'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=А&filefrom=А&subcatuntil=А#mw-subcategories']
wiki_word = []

for i in wiki_link:
    if i == '':
        break
    url = unquote(i)
    wiki_link.append(parser_next_link())

# Удаляем последний, пустой эллемент
del wiki_link[-1]

val_word = {}
alf = (
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
    'Ц',
    'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
    'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
for letter in alf:
    val_word[letter] = len(list(filter(lambda x: x[0] == letter, wiki_word)))

for i in val_word:
    print(i, ' - ', val_word[i])
