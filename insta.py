import json
import requests

def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "5a730666cemsh29497c9e53ca025p1d228ejsn6f0d13041775",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    rest=json.loads(response.text)
    if 'error' in rest:
        return 'Buni yuklash mavjud emas !'
    else:
        dict={}
        if rest['Type']=='Post-Image':
            dict['type']='image'
            dict['media']=rest['media']
            return dict
        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Bad'


