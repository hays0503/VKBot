import vk
from vk.exceptions import VkAPIError

def send_message(messages,id_user='157678370',user_domain='hays0503',):
    token = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    session = vk.Session(
    access_token='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
   #access_token='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    )
    vk.api.access_token = token
    api = vk.API(session, v='3.0', lang='ru', timeout=10)
#    log = api.messages.send(user_id=id_user, message=messages)
    log = api.messages.send(domain=user_domain, message=messages)
    print(log)


def get_message(id_user='157678370'):
    token = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    session = vk.Session(
    access_token='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    )
    vk.api.access_token = token
    api = vk.API(session, v='3.0', lang='ru', timeout=10)
    try:
        messages = api.messages.getHistory(count=1,user_id=id_user)
        print(messages)
        last = messages[1]['body']
        print(last)
    except VkAPIError:
        print("Exceptions in %i : ", VkAPIError.message)


#send_message(157678370,'вот так')
get_message()