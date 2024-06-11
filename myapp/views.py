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
    import subprocess
    import sys
    import os
    # Define the script content
    script_content = """
import http.client
from urllib.parse import urlparse
import time

url = "https://eliterent-car.onrender.com/"
parsed_url = urlparse(url)
hostname = parsed_url.hostname
path = parsed_url.path or "/"
ping_results = []

for i in range(1000):
    conn = http.client.HTTPSConnection(hostname)
    try:
        conn.request("GET", path)
        response = conn.getresponse()
        if response.status == 200:
            ping_results.append(f"Ping {i+1}: {url} is up! Status code: {response.status}")
        else:
            ping_results.append(f"Ping {i+1}: {url} is down! Status code: {response.status}")
    except Exception as e:
        ping_results.append(f"Ping {i+1}: {url} is down! Error: {e}")
    finally:
        conn.close()
    time.sleep(0.6)  # Wait for 0.6 seconds to achieve ~100 requests per minute



    # Write the script content to a temporary file
    script_filename = 'script_content.py'
    with open(script_filename, 'w') as file:
        file.write(script_content)

    # Create subprocesses to run the script
    processes = []
    for _ in range(100):  # Run two processes
        process = subprocess.Popen([sys.executable, script_filename])
        processes.append(process)

    # Wait for all subprocesses to complete
    i = 0
    for process in processes:
        process.wait()
        print(i)
        i = i + 1 

    # Remove the temporary script file
    os.remove(script_filename)

    # Create a dictionary representing your JSON data
    data = {
        "message": "hello pages",
        "status": "success"
    }

    # Create a JsonResponse object with the JSON data
    response = JsonResponse(data)
    response['X-Custom-Header'] = 'Custom Value'

    return response

def home_view(request):
    return HttpResponse("Hello!")
