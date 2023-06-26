import os

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import SharedFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = UploadForm()
    return render(request, 'sharefile/upload.html', {'form': form})

def file_list(request):
    shared_files = SharedFile.objects.all()
    return render(request, 'sharefile/file_list.html', {'files': shared_files})

# 下载功能
def download_file(request, file_id):
    # 获取共享文件对象
    shared_file = get_object_or_404(SharedFile, id=file_id)
    # 获取文件路径
    file_path = shared_file.file.path

    # 打开文件并返回HttpResponse对象
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404