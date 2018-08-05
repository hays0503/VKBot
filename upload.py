import datetime
import json
import time

import requests
import vk

"""!
    @package upload
"""


class uploadInspector():
    """!
        @brief A set of tools for downloading content to VK
        @brief Набор инструментов для загрузки контента в VK
    """

    def upload(self, url, count, public_page, public_page_post, signed, messages=''):
        """!
            @brief Upload content in VK
            @brief Загружает контент в VK
            @param [in] str url // patch to file
            @param [in] str count // timer post
            @param [in] str public_page //destination address
            @param [in] str public_page_post // destination address (negative for group)
            @param [in] str signed // signed or no
            @param [in] str messages // attach string messages
        """
        token = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        session = vk.Session(
            access_token='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
        vk.api.access_token = token
        api = vk.API(session, v='3.0', lang='ru', timeout=10)
        result = api.photos.getWallUploadServer(group_id=public_page)
        upload_url = result['upload_url']
        try:
            img = {'photo': ('img32.jpg', open(url, 'rb'))}
            response = requests.post(upload_url, files=img)
            # print("Response.text", response.text)
            print("Load post in grops")
            result = json.loads(response.text)
            attach = api.photos.saveWallPhoto(photo=result['photo'],
                                              hash=result['hash'],
                                              server=result['server'],
                                              group_id=public_page)
            Temp = attach[0]['id']
            wait = 60 * 60
            vol = wait * count
            times = (time.time() + vol)
            time.sleep(3)
            #    print("Times: ", times)
            var_times = datetime.datetime.today() + datetime.timedelta(hours=count)
            var_times = var_times - datetime.timedelta(minutes=var_times.minute)
            print(var_times.strftime("%A, %d. %B %Y %I:%M%p"))
            print("Messages %s", messages)
            if count != 0:
                api.wall.post(from_group=1,
                              owner_id=public_page_post,
                              attachments=Temp,
                              signed=signed,
                              publish_date=int(time.mktime(var_times.timetuple())))
            #                 message=str(var_times.strftime("%A, %d. %B %Y %I:%M%p")))
            else:
                api.wall.post(from_group=1,
                              owner_id=public_page_post,
                              attachments=Temp,
                              signed=signed,
                              message=messages
                              )
            # count += 1
        except Exception as e:
            print(e)
            return
