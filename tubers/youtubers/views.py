from django.shortcuts import get_object_or_404, redirect, render
from .models import Youtuber
# Create your views here.


def youtubers(request):
    ytubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    data={
        'ytubers':ytubers,
        'city_search' : city_search, 
        'camera_search' : camera_search,         
        'category_search' : category_search,
    }
    return render(request, 'youtubers/youtubers.html', data )


def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber'  : tuber,
    }
    return render(request, 'youtubers/youtuber_detail.html',data)


def search(request):
    ytubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            ytubers = ytubers.filter(description__icontains=keyword)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            ytubers = ytubers.filter(city__iexact=city)
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            ytubers = ytubers.filter(camera_type__iexact=camera_type)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            ytubers = ytubers.filter(category__iexact=category)
    data ={
        'ytubers' : ytubers,
        'city_search' : city_search, 
        'camera_search' : camera_search,         
        'category_search' : category_search,    
         }
    return render(request, 'youtubers/search.html',data)



def set_youtubers(request):
    
        if request.method == 'POST' :
            name=request.POST['name']
            price=request.POST['price']
            
            description=request.POST['description']
            city=request.POST['city']
            age=request.POST['age']
            height=request.POST['height']
            crew=request.POST['crew']
            camera_type=request.POST['camera_type']
            subs_count=request.POST['subs_count']
            category=request.POST['category']
            ytuber = Youtuber(name=name, price=price, description=description, city=city, age=age, height=height, crew=crew, camera_type=camera_type, subs_count=subs_count, category=category)
            ytuber.save()
            return redirect('home')
    
        pass



