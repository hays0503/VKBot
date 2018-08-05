import requests
from bs4 import BeautifulSoup

"""!
@package infobypost
"""


class infoByPost():
    """!
    @brief Parser information about the post
    @brief Парсер информации о посте
    """

    def characters(self, url):
        """!
        @brief Character names parser
        @brief Парсер имен персонажей
        @param [in] str url
        @return str
        """
        rc = requests.get(url)
        data = rc.text
        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find(class_='character-tag-list')
        last_links.decompose()
        artist_name_list = soup.find(class_='character-tag-list')
        artist_name_list_items = artist_name_list.find_all('a')
        return_value = 'Characters:\n'
        for artist_name in artist_name_list_items:
            if artist_name.contents[0] != '?':
                return_value += artist_name.contents[0] + '\n'
        return return_value

    def autor(self, url):
        """!
        @brief Parser of the author's name (s)
        @brief Парсер имени(ов) автора
        @param [in] str url
        @return str
        """
        rc = requests.get(url)
        data = rc.text
        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find(class_='artist-tag-list')
        last_links.decompose()
        artist_name_list = soup.find(class_='artist-tag-list')
        artist_name_list_items = artist_name_list.find_all('a')
        return_value = 'Autor: '
        for artist_name in artist_name_list_items:
            if artist_name.contents[0] != '?':
                return_value += artist_name.contents[0] + '\n'
        return return_value

    def souse(self, url):
        """!
        @brief Art Source Parser
        @brief Парсер источника арта
        @param [in] str url
        @return str
        """
        rc = requests.get(url)
        data = rc.text
        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find_all('section', id='post-information')
        artist_name_list = last_links[0].contents[3]
        href = artist_name_list.find_all('li')
        url = None
        for item in href:
            str = item.contents[0]
            if str == "Source: ":
                url = item.contents[1].attrs['href']
        return_value = 'souse: ' + url
        return return_value

    def info(self, url):
        """!
        @brief Compiling all information about the post
        @brief Компиляция всего информации об посте
        @param [in] str url
        @return str
        """
        _autor = self.autor(url)
        _characters = self.characters(url)
        _souse = self.souse(url)
        print(_autor + _characters + _souse)
        return _autor + _characters + _souse
