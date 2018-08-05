import datetime
import time

import vk

from dataBD import databaseTools
from listSource import listSource

"""!
@package polls
"""


class pollsInspector():
    """!
    @brief Voting control
    @brief Управление голосованием
    """

    ##@brief Database toolst \n Инструменты для работой с базой данных
    database_tools = databaseTools()

    def polls_create(self, public_page, public_page_post, answers, signed):
        """!
        @brief Create voting in vk
        @brief Создание голосование в vk
        @param [in] str public_page
        @param [in] str PublicPagePost
        @param [in] str answers
        @param [in] str signed
        """
        token = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        session = vk.Session(
            access_token='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
        vk.api.access_token = token
        api = vk.API(session, v='3.0', lang='ru', timeout=10)

        result = api.polls.create(
            question="Контент недели",
            is_anonymous=signed,
            owner_id=public_page_post,
            add_answers=answers
        )
        #    print(result)
        return result

    def upload_polls(self, count, public_page, public_page_post, answers, signed):
        """!
        @brief Upload voting in vk
        @brief Загрузка голосование в vk
        @param [in] str public_page
        @param [in] str PublicPagePost
        @param [in] str answers
        @param [in] str signed
        """
        token = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        session = vk.Session(
            access_token='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
        vk.api.access_token = token
        api = vk.API(session, v='3.0', lang='ru', timeout=10)
        polls = self.polls_create(public_page, public_page_post, answers, 1)
        attach = "poll" + str(public_page_post) + "_" + str(polls['poll_id'])
        #    print(attach)
        wait = 60 * 60
        vol = wait * count
        times = (time.time() + vol)
        time.sleep(3)
        #    print("Times: ", times)
        var_times = datetime.datetime.today() + datetime.timedelta(hours=count)
        var_times = var_times - datetime.timedelta(minutes=var_times.minute)
        #    print(var_times.strftime("%A, %d. %B %Y %I:%M%p"))
        api.wall.post(from_group=1,
                      owner_id=public_page_post,
                      attachments=attach,
                      signed=signed,
                      # publish_date=int(time.mktime(var_times.timetuple())),
                      message="Выбираем контент на недёлю")
        count += 1
        return polls['poll_id']

    def getVoitedPolls(self, PublicPagePost, idpolls):
        """!
            @brief Taking voting results in vk
            @brief Взятие результатов голосования в vk
            @param [in] str PublicPagePost
            @param [in] str idpolls
            @return str WinItem
        """
        token = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        session = vk.Session(
            access_token='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
        vk.api.access_token = token
        api = vk.API(session, v='3.0', lang='ru', timeout=10)

        result = api.polls.getById(
            poll_id=idpolls,
            owner_id=PublicPagePost,
            is_board=0
        )

        max = 0
        poll_win_item = 0
        for i in range(len(result['answers'])):
            if result['answers'][i]['rate'] > max:
                max = result['answers'][i]['rate']
                poll_win_item = i
        WinItem = result['answers'][poll_win_item]
        return WinItem

    def create_new_polls(self, public_page, public_page_post):
        """!
            @brief Create a poll in vk
            @brief Создание голосование в vk
            @param [in] str public_page
            @param [in] str public_page_post
        """
        answers = listSource.get_json_list()
        polls = self.upload_polls(1, public_page, public_page_post, answers, 1)
        pollsInspector.database_tools.updatePollsInServer(polls, public_page_post)

    def whoWinInPolls(self, public_page_post):
        """!
            @brief Returns the winner of the voting in vk
            @brief Возвращает победителя голосования в vk
            @param [in] str public_page_post
            @return str
        """
        return_value = self.database_tools.getPollsByGroup(public_page_post)
        win_in_polls = self.getVoitedPolls(public_page_post, return_value)
        return win_in_polls['text']

    def test_read_polls(self):
        """!
            @brief Voting test in vk
            @brief Тест голосования в vk
        """
        public_page_post = '-122263284'
        print(self.whoWinInPolls(public_page_post))

#create_new_polls('122263284','-122263284')
#test_read_polls()
#whoWinInPolls('-122263284')
