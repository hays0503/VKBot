import json

"""!
    @package listSource
"""

class listSource():
    """!
        @brief List source witch url and theme
        @brief Список источников с ссылками и темами
    """

    ## @brief Source url and theme
    dict_source = {

        'touhou':
            "https://danbooru.donmai.us/posts?tags=rating%3Asafe+touhou",
        'kantai collection':
            "https://danbooru.donmai.us/posts?tags=rating%3Asafe+kantai_collection",
        'girls und panzer':
            "https://danbooru.donmai.us/posts?tags=rating%3Asafe+girls_und_panzer",
        '1girl':
            "https://danbooru.donmai.us/posts?tags=rating%3As+1girl",
        'multiple girls':
            "https://danbooru.donmai.us/posts?tags=rating%3Asafe+multiple_girls",
        'long hair':
            "https://danbooru.donmai.us/posts?tags=rating%3Asafe+long_hair"
    }

    @staticmethod
    def get_json_list():
        """!
        @brief Return json list
        @brief Возвращает json список
        @return json
        """
        list_obj = list(listSource.dict_source.keys())
        json_out = json.dumps(list_obj)
        return json_out

    @staticmethod
    def get_url_by_theme(theme):
        """!
        @brief Return value by key
        @brief Возвращает значение по ключу
        @arg str Theme
        @return value
        """
        return listSource.dict_source.get(theme)
