from vk.exceptions import VkAPIError

from download import downloadInspector
from hash_art import heahArt
from infobypost import infoByPost
from polls import pollsInspector
from upload import uploadInspector


class launchInspector():
    """!
        @brief Planning work
        @brief Планирование работы
    """

    upload_inspector = uploadInspector()
    download_inspector = downloadInspector()
    polls_inspector = pollsInspector()
    info_by_post = infoByPost()
    heah_art = heahArt()

    def launch(self):
        """!
            @brief Running Content Creation
            @brief Запуск создание контента
        """
        patch = self.download_inspector.downloadOne()
        #    print(out)
        #    print("Download end..")
        self.mainGroups(patch)
        self.download_inspector.delete_file_in_folder(patch)

    def launchTest(self, public_page, public_page_post):
        """!
            @brief Test run content creation
            @brief Тестовый запуск создание контента
            @param [in] str public_page
            @param [in] str public_page_post
        """
        return_value = self.polls_inspector.whoWinInPolls(public_page_post)
        if return_value in (-1, -2):
            print("ErrorPolls: Not found file or empty file")
            return return_value
        out = self.download_inspector.downloadPolls(return_value)
        if out in (-1, -2):
            print("ErrorDownload: some failure")
            return return_value
        substr = out.split('\n')
        stringURL = self.info_by_post.info(substr[1]) + "\n" + substr[1] + "\n" + return_value
        # substr[0] = patch to file
        self.testGroups(substr[0], public_page, public_page_post, stringURL)
        self.download_inspector.delete_file_in_folder(substr[0])

    def mainGroups(self, patch):
        """!
            @brief Upload content to groups
            @brief Загрузка контента в группы
            @param [in] str patch // to file
        """
        time_post = 1
        public_page = '77351320'
        public_page_post = '-77351320'
        try:
            self.upload_inspector.upload(patch, time_post, public_page, public_page_post, 1)
        #        print("Num post: %i in groups 1" % time_post)
        except VkAPIError:
            print("Exceptions in %i : " % time_post, VkAPIError.message)
        public_page = '77599884'
        public_page_post = '-77599884'
        try:
            self.upload_inspector.upload(patch, time_post, public_page, public_page_post, 1)
        #       print("Num post: %i in groups 2" % time_post)
        except VkAPIError:
            print("Exceptions in %i : " % time_post, VkAPIError.message)
        public_page = '47914447'
        public_page_post = '-47914447'
        try:
            self.upload_inspector.upload(patch, time_post, public_page, public_page_post, 0)
        #       print("Num post: %i in groups 3" % time_post)
        except VkAPIError:
            print("Exceptions in %i : " % time_post, VkAPIError.message)
        # delete_file_in_folder(directory + files[0])

    def testGroups(self, patch, public_page, public_page_post, messages=''):
        """!
            @brief Upload content to test group
            @brief Загрузка контента в тестовую групу
            @param [in] str patch // to file
            @param [in] str public_page //destination address
            @param [in] str public_page_post // destination address (negative for group)
            @param [in] str messages // attach string messages
        """
        time_post = 0  # now
        result = self.heah_art.equivalent_post(public_page_post, patch)
        print(result)
        if result == 0:
            arr = messages.split('\n')
            try:
                self.upload_inspector.upload(patch,
                                             time_post,
                                             public_page,
                                             public_page_post,
                                             1,
                                             messages)
                self.heah_art.update_hesh_last_post(public_page_post,
                                                    patch,
                                                    arr[0], arr[1])
            except VkAPIError:
                print("Exceptions in %i : " % time_post, VkAPIError.message)
        else:
            print('Error:Post equivalent')