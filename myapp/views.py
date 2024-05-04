from django.shortcuts import render
from .services import Download
from django.http import HttpResponse

from django.http import JsonResponse


download = Download("https:hdgddf")


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