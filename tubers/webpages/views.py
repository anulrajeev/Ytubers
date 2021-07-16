from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber
# Create your views here.



def home(request):
    sliders = Slider.objects.all()
    team=Team.objects.all()
    featured_ytuber=Youtuber.objects.order_by('created_date').filter(is_featured=True)
    ytubers=Youtuber.objects.order_by('created_date')
    data = {
        'sliders' : sliders,
        'team' : team,
        'featured_ytuber':featured_ytuber,
        'ytubers':ytubers,
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    team_members=Team.objects.all() 
    data={
        'team_members': team_members,
    }
    return render(request, 'webpages/about.html', data)


def services(request):
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    data={
            'city_search' : city_search,        
            'camera_search' : camera_search,
            'category_search' : category_search,        
    }
    return render(request, 'webpages/services.html', data)

def contact(request):
    return render(request, 'webpages/contact.html')
