from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
import folium

# Create your views here.
def index(request):
    # create map object
    m = folium.Map(location=[25.0139376,121.5421717], zoom_start = 20)
    folium.Marker([25.0139376,121.5421717]).add_to(m)
    folium.Marker([25.0134056,121.5409975]).add_to(m)
    folium.Marker([25.014614, 121.542910]).add_to(m)
    folium.Marker([25.012674, 121.542057]).add_to(m)
    # get html representation of map object
    m = m._repr_html_()
    context = {
        'm' : m,
        #asablu
    }
    return render(request, 'index.html', context)

from .form import PostForm
from .models import Car
def post_create_view(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, '/post_create.html', context)