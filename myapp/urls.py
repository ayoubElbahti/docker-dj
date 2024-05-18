from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('download_fb_video/', views.download_fb_video, name='download_fb_video'),
    path('download_ig_video/', views.download_ig_video, name='download_ig_video'),
    path('download_tik_video/<str:url>/', views.download_tik_video, name='download_tik_video'),
    path('download_yb_video/<path:url>/', views.download_yb_video, name='download_yb_video'),
    path('translate/<str:input_text>/<str:from_lg>/<str:to_lg>/', views.translate, name='translate'),
]
