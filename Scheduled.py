from apscheduler.schedulers.blocking import BlockingScheduler

from launch import launchInspector
from polls import pollsInspector

"""!
    @package scheduled
"""

"""!
    @mainpage mainpage
    My Personal Index Page
    @htmlinclude html/annotated.html
"""

class scheduledInspector():
    """!
        @brief Performs the scheduled action
        @brief Выполняет запланированные действие
    """
    sched = BlockingScheduler()
    # http://apscheduler.readthedocs.io/en/latest/modules/triggers/interval.html

    def timed_job(self):
        """!
            @brief Starts the creation of content by time
            @brief Запускает создание контента по времени
        """
        launch_inspector = launchInspector()
        launch_inspector.launch()


    def polls_job(self):
        """!
            @brief Starts the creation of polls by time
            @brief Запускает создание голосование по времени
        """
        public_page = '122263284'
        public_page_post = '-122263284'
        print("Begin create new polls")
        polls_inspector = pollsInspector()
        polls_inspector.create_new_polls(public_page, public_page_post)
        print("End create new polls")

    '''
        public_page = '77351320' #[R]kach
        public_page_post = '-77351320'
        create_new_polls(public_page,public_page_post)
        print("Num post: %i in groups 1" % time_post)
    
        public_page = '77599884' #TAP
        public_page_post = '-77599884'
        create_new_polls(public_page,public_page_post)
        print("Num post: %i in groups 2" % time_post)
    
        public_page = '47914447' #onime__tyan
        public_page_post = '-47914447'
        create_new_polls(public_page, public_page_post)
        print("Num post: %i in groups 3" % time_post)
    '''

    def test_timed_job(self):
        """!
            @brief Starts test the creation of content by time
            @brief Запускает тестовое создание контента по времени
        """
        public_page = '122263284'
        public_page_post = '-122263284'
        print("Create new post")
        launch_inspector = launchInspector()
        launch_inspector.launchTest(public_page, public_page_post)

    def main_point(self):
        """!
            @brief Main point
            @brief Главная точка
        """
        self.sched.add_job(self.timed_job, 'interval', hours=1)
        self.sched.add_job(self.polls_job, 'interval', hours=12)
        self.sched.add_job(self.test_timed_job, 'interval', minutes=5)
        self.sched.start()


if __name__ == '__main__':
    inspector = scheduledInspector()
    inspector.main_point()

