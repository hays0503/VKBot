import os
import re
import subprocess

import requests

from listSource import listSource

"""!
    @package download 
"""


class downloadInspector():
    """!
        @brief Tools for download arts
        @brief Набор инструментов для скачивание артов
    """

    def delete_file_in_folder(self, patch):
        """!
            @brief Delete file
            @brief Удаляет файл
            @param [in] string patch
        """
        try:
            os.remove(patch)
        #        print("Delete file: " + patch)
        except Exception as e:
            print(e)

    def delete_danbooru_folder(self):
        """!
            @brief Delete danbooru folder
            @brief Удаление папки danbooru
        """
        folder = './gallery-dl/danbooru'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

    def list_file(self):
        """!
            @brief Get list file in danbooru folder
            @brief Взять список файлов из папки danbooru
            @return list files
        """
        directory = 'gallery-dl/danbooru/'
        files = os.listdir(directory)
        return files

    def downloadOne(self):
        """!
            @brief Download one file in one girl theme
            @brief Скачать один файл в тематике one girl
            @return [in] string patch
        """
        rc = requests.get(listSource.get_url_by_theme('one girl'))
        data = rc.text
        match = re.findall(r'/posts/\d\d\d\d\d\d\d', data)
        string_url = ("https://danbooru.donmai.us" + match[0])
        process_downloader = subprocess.Popen(
            "gallery-dl %s" % string_url, shell=True, stdout=subprocess.PIPE)
        out = process_downloader.stdout.readlines()
        reg_exp = "\./gallery-dl/danbooru/danbooru_\d\d\d\d\d\d\d_\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\.(png|jpg)"
        match_patch = re.search(reg_exp, str(out))
        return match_patch.group(0)

    def downloadPolls(self, value):
        """!
            @brief Download one file in the subject chosen in the voting
            @brief Скачать один файл в тематике выбраном в голосовании
            @param [in] string value // theme polls
            @return str patch (-1 if error)
        """
        rc = requests.get(listSource.get_url_by_theme(value))
        data = rc.text
        match = re.findall(r'/posts/\d\d\d\d\d\d\d', data)
        string_url = ("https://danbooru.donmai.us" + match[0])
        process_downloader = subprocess.Popen(
            "gallery-dl %s" % string_url, shell=True, stdout=subprocess.PIPE)
        out = process_downloader.stdout.readlines()
        print(out)
        regExp = "\./gallery-dl/danbooru/danbooru_\d\d\d\d\d\d\d_\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\.(png|jpg)"
        match_patch = re.search(regExp, str(out))
        if match_patch is not None:
            print(match_patch)
            print(str(match_patch.group(0) + "\n" + string_url))
            return_value = str(match_patch.group(0) + "\n" + string_url)
            return return_value
        else:
            return -1
