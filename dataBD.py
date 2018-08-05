import psycopg2

"""!
    @package dataBD
"""


class databaseTools():
    """!
    @brief Database tools work witch postgres
    @brief Инструменты базы данных работают с postgres
    """

    def clearHashDatabase(self):
        """!
        @brief Clearing the hash sum database
        @brief Отчистра базы данных хеш сумм
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()

        cur.execute("""
                        DELETE FROM public."DatabaseHash"
                    """)
        conn.commit()
        print("Clear HashDatabase")

    def deleteColumnByIdAndHesh(self, hashsum, id_public):
        """!
        @brief Deleting one line by group id and hash sum
        @brief Удаление одной строки по id группы и хеш суммы
        @param [in] string heshsum
        @param [in] string id_public

        deleteColumnByIdAndHesh('c3394a1be2006049a27e77d44ba50a27', '122263284')
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()

        cur.execute("""
                        DELETE FROM public."DatabaseHash" WHERE "Hash"=%s AND id_public=%s""",
                    (hashsum, id_public))
        conn.commit()

    def addHeshInServer(self, hashsum, id_public, url='none', name='none'):
        """!
        @brief Add one hash sum by group and
        @brief Добавление одной строки по id группы
        @param [in] string heshsum
        @param [in] string id_public
        @param [in] string url
        @param [in] string name

        addHeshInServer('c3394a1be2006049a27e77d44ba50a27',
        '122263284',
        'https://danbooru.donmai.us/posts/3195667',
        'touhou',
        )
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO public."DatabaseHash"("Name", "Hash", "Url", id_public)
                    VALUES (%s, %s, %s, %s)""",
                    (name, hashsum, url, id_public))
        conn.commit()

    def getTableByGroup(self, id_public):
        """!
            @brief Get(print console) table by id_public
            @brief Взятие(вывод в консоль) таблицы по id_public
            @param [in] str id_public

            getTableByGroup('122263284')
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()
        cur.execute("""
                    SELECT * from public.\"DatabaseHash\" WHERE id_public='%s'
                    """ % id_public)
        rows = cur.fetchall()
        for item in rows:
            print(item)

    def getCollisionByGroup(self, hashsum, id_public):
        """!
            @brief Finding collisions on id_public and hash sum
            @brief Нахождение колиизи по id_public и хеш сумме
            @param [in] string heshsum
            @param [in] string id_public
            @return Return 0 if Not collision or return 1
            getCollisionByGroup('csrhserhbe2006049a27e77d44ba50a27', '122263284')
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()
        cur.execute("""
                    SELECT * from public.\"DatabaseHash\" WHERE id_public='%s' and "Hash"='%s'
                    """ % (id_public, hashsum))
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Not collision")
            return 0
        else:
            print("Collision")
            for item in rows:
                print(item)
            return 1

    def clearPollsDatabase(self):
        """!
            @brief Clearing the voting database
            @brief Очистка базы данных голосований
            clearPollsDatabase()
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()

        cur.execute("""
                        DELETE FROM public."DatabasePolls"
                    """)
        conn.commit()
        print("Clear PollsDatabase")

    def deleteColumnById(self, id_public):
        """!
            @brief Deleting a row in the voting database by id_public
            @brief Удаление строки в базе данных голосования по id_public
            @param [in] string id_public

            deleteColumnById('122263284')
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()

        cur.execute("""
                        DELETE FROM public."DatabasePolls" WHERE id_public=%s""" % id_public
                    )
        conn.commit()

    def addPollsInServer(self, id_polls, id_public, answer='none'):
        """!
            @brief Add id_polls in the voting database by id_public
            @brief Добавление id_polls в базе данных голосования по id_public
            @param [in] string id_polls
            @param [in] string id_public
            @param [in] string answer

            addPollsInServer('163516151',
                            '122263284',
                            'none') # option arg
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO public."DatabasePolls"("Polls_id", "Public_id", "Answer")
                    VALUES (%s, %s, %s)""",
                    (id_polls, id_public, answer))
        conn.commit()

    def updatePollsInServer(self, id_polls, id_public, answer='none'):
        """!
            @brief Updating id_polls in the voting database by id_public
            @brief Обновление id_polls в базе данных голосования по id_public
            @param [in] string id_polls
            @param [in] string id_public
            @param [in] string answer

            updatePollsInServer('163516151',
                                '122263284',
                                'none') # option arg
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()
        cur.execute("""
                    UPDATE public."DatabasePolls" SET "Polls_id"=%s, "Answer"=%s WHERE "Public_id"=%s
                    """,
                    (id_polls, answer, id_public))
        conn.commit()

    def getPollsByGroup(self, id_public):
        """!
            @brief Get id_polls by id_public
            @brief Взятие id_polls по id_public
            @param [in] string id_public
            @return string id_polls
            getPollsByGroup('122263284')
        """
        conn = psycopg2.connect(
            "dbname='dbname'"
            " user='user'"
            " host='host'"
            " password='password'")
        cur = conn.cursor()
        cur.execute("""
                    SELECT * from public.\"DatabasePolls\" WHERE "Public_id"='%s'
                    """ % id_public)
        rows = cur.fetchall()
        return rows[0][0]
