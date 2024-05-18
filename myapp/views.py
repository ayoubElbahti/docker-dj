from django.shortcuts import render
from .services import Download
from django.http import HttpResponse

from django.http import JsonResponse


download = Download("https:hdgddf")

def translate(request,input_text,from_lg,to_lg):
    import requests
    print(input_text)
    print(from_lg)
    print(to_lg)
    headers = {
        'accept': '*/*',
        'accept-language': 'fr-FR,fr;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://translate.yandex.com',
        'priority': 'u=1, i',
        'referer': 'https://translate.yandex.com/',
        'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
        'x-retpath-y': 'https://translate.yandex.com',
    }

    params = {
        'id': '7118f46e.6648f0fb.60e117e4.74722d74657874-1-0',
        'srv': 'tr-text',
        'source_lang': from_lg,
        'target_lang': to_lg,
        'reason': 'auto',
        'format': 'text',
        'strategy': '0',
        'disable_cache': 'false',
        'ajax': '1',
        'yu': '1762712181716053538',
    }

    data = {
        'text': input_text,
        'options': '4',
    }

    response = requests.post('https://translate.yandex.net/api/v1/tr.json/translate', params=params, headers=headers, data=data)
    data = {
        'text': response.text,
        'options': '4',
    }
    responsee = JsonResponse(data)

    # Add custom headers to the response
    responsee['X-Custom-Header'] = 'Custom Value'

    return responsee


def download_fb_video(request):
    url = request.GET.get('url_param')
    download.url = str(url).replace("ẞ",'&') 
    #print(url)  
    # Create a dictionary representing your JSON data
    response = download.facebook()
    if response['status_code'] == 200:
        data = response
    else:
        data = {
            "message": response['message'],
            "status": "failed"
        }

    # Create a JsonResponse object with the JSON data
    response = JsonResponse(data)

    # Add custom headers to the response
    response['X-Custom-Header'] = 'Custom Value'

    return response

def download_ig_video(request):
    # Create a dictionary representing your JSON data
    #url = request.GET.get('url_param')
    response = download.instagram()
    data = {
        "message": response['message'],
        "status": "success"
    }

    # Create a JsonResponse object with the JSON data
    response = JsonResponse(data)

    # Add custom headers to the response
    response['X-Custom-Header'] = 'Custom Value'

    return response

def download_yb_video(request,url):
    # Create a dictionary representing your JSON data
    data = {
        "message": f'{download.youtube()} hh {url}',
        "status": "success"
    }

    # Create a JsonResponse object with the JSON data
    response = JsonResponse(data)

    # Add custom headers to the response
    response['X-Custom-Header'] = 'Custom Value'

    return response


def download_tik_video(request,url):
    # Create a dictionary representing your JSON data
    data = {
        "message": f'{download.tiktok()} hh {url}',
        "status": "success"
    }

    # Create a JsonResponse object with the JSON data
    response = JsonResponse(data)

    # Add custom headers to the response
    response['X-Custom-Header'] = 'Custom Value'

    return response





def hello_world(request):
    # Create a dictionary representing your JSON data
    data = {
        "message": "hello pages ",
        "status": "success"
    }

    # Create a JsonResponse object with the JSON data
    response = JsonResponse(data)

    # Add custom headers to the response
    response['X-Custom-Header'] = 'Custom Value'

    return response

def home_view(request):
    return HttpResponse("Hello!")
