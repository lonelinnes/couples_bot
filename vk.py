import requests
import wget

def vk():
    access_token = 'e090dc28e090dc28e090dc287ce3b80561ee090e090dc288733d695d9b75a1c44ab4f54'
    url = f"https://api.vk.com/method/board.getComments?group_id=158830121&topic_id=37235959&access_token={access_token}&v=5.1999"
    response = requests.get(url)
    mass = response.json()['response']['items'][response.json()['response']['count']-1]
    result = []
    len_obj = len(mass['attachments'])

    for i in range(0, len_obj):
        result.append({'titile':mass['attachments'][i]['doc']['title'], 'url':mass['attachments'][i]['doc']['url']})
    for i in range(0, len_obj):
        url = result[i]['url']
        wget.download(url, f'pdf/pdf_v2{i}.pdf')

    return result
