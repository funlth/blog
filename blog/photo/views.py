from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Photo, Category

def photo_list(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos, 'categories': categories})

def photo_category(request, category_id):
    category = Category.objects.get(id=category_id)
    photos = Photo.objects.filter(category=category)
    categories = Category.objects.all()
    context = {'category': category, 'photos': photos, 'categories': categories}
    return render(request, 'photo/photo_category.html', context)