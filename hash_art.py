import hashlib

from dataBD import databaseTools

"""!
@package hesh_art
"""


class heahArt():
    """!
    @brief Hashing content
    @brief Хеширование контента
    """

    ### @brief Database toolst \n Инструменты для работой с базой данных
    dbTools = databaseTools()

    def read_hesh(self, patch):
        """!
            @brief Taking a hash sum
            @brief Взятие хеш суммы
            @param [in] string patch
            @return str hesh
        """
        try:
            hasher = hashlib.md5()
            with open(patch, 'rb') as afile:
                buf = afile.read()
                hasher.update(buf)
            #        print(hasher.hexdigest())
            return hasher.hexdigest()
        except Exception as e:
            print(e)

    def equivalent_post(self, public_page_post, patch):
        """!
        @brief Ищет совпадение с прошлым постом если совпадение найденно возвращает -3 если нет то 0
        @param [in] string public_page_post
        @param [in] string patch
        @return int
        """
        heshFile = self.read_hesh(patch)
        if self.dbTools.getCollisionByGroup(heshFile, public_page_post) == 1:
            return -3
        return 0

    def update_hesh_last_post(self, PublicPagePost, patchFile, url='none', name='none'):
        """!
        @brief Updates the hash sum and also applies the inf on post
        @brief Обновляет хеш сумму а также занносит инф о посте
        @param [in] string public_page_post
        @param [in] string patch
        @param [in] string url
        @param [in] string name
        """
        hesh = self.read_hesh(patchFile)
        # rewriteHeshLastPost(PublicPagePost, hesh)
        heahArt.dbTools.addHeshInServer(hesh, PublicPagePost, url, name)

    def test(self):
        """!
        @brief Functional test data hashing
        @brief Тест функционала хеширование данных
        """
        patchFile = 'Sakuya.png'
        patchFile1 = 'Sakuya1.png'
        # hesh = readHesh(patchFile)
        # print(hesh)
        PublicPagePost = '-122263284'
        # rewriteHeshLastPost(PublicPagePost, hesh)
        result = self.equivalent_post(PublicPagePost, patchFile)
        print(result)
        if result == 0:
            self.update_hesh_last_post(PublicPagePost, patchFile)
