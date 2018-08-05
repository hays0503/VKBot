import time

from polls import pollsInspector

"""!
    @package Crete_new_polls
"""


class testPolls:
    """!
        @brief     Test creater polls
        @brief     Тестирование создания голосования
    """

    """!
    @msc polls_job

    Start_Job,Timer,End_Job;
    Start_Job->Timer [ label = "testPolls.polls_job()()" ];
    Timer->End_Job   [ label = "end" ];

    @endmsc
    """

    def polls_job(self):
        """!
        @brief  Создание голосование и остановка процедуры на час.
        @param  None
        @return None
        """
        public_page = '122263284'
        public_page_post = '-122263284'
        print("Begin create new polls")
        pollsInspector.create_new_polls(public_page, public_page_post)
        print("End create new polls")
        time.sleep(3600)
        return None


"""!
    @test Точка запуска    
"""
testPolls.polls_job()
