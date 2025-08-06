from django.shortcuts import render
from django.shortcuts import render
import os

def gallery_view(request):
    # 图片和视频的绝对路径
    image_dir = r'C:\Users\www76\PycharmProjects\PythonProject2\mysite\mysite\webapp\static\images'
    video_dir = r'C:\Users\www76\PycharmProjects\PythonProject2\mysite\mysite\webapp\static\viedos'

    # 获取所有图片文件（只取 .jpg）
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith('.jpg')]

    # 获取所有视频文件（支持多种格式）
    video_files = [f for f in os.listdir(video_dir) if f.lower().endswith(('.mp4', '.webm', '.ogg'))]

    context = {
        'images': image_files,
        'videos': video_files
    }

    return render(request, 'gallery.html', context)


# Create your views here.
