from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
import folium
from .models import Car

# Create your views here.
def index(request):
    # lon = Car.objects.filter('Longitude')
    # la = Car.objects.filter('Latitude')
    data = Car.objects.all()
    num = Car.objects.count()
    # create map object
    # m = folium.Map(location=[25.0139376,121.5421717], zoom_start = 20)
    # folium.Marker([25.014614, 121.542910]).add_to(m) #C1
    # folium.Marker([25.012674, 121.542057]).add_to(m) #Car_2
    # folium.Marker([25.0139376,121.5421717]).add_to(m)
    # folium.Marker([25.0134056,121.5409975]).add_to(m)
    # for i in range(0,num):
    #     folium.Marker([data.values()[i]['Longitude'], data.values()[i]['Latitude']],tooltip="%s: %f, %f" % (data.values()[i]['CarName'],data.values()[i]['Longitude'],data.values()[i]['Latitude'])).add_to(m)
    # data.delete()
	# get html representation of map object
    # m = m._repr_html_()
    # context = {
    #     'm' : m,
    #     #asablu
    # }
    return render(request, 'index.html')
	# return render(request, 'index.html', context)
	

from .forms import PostForm
from .models import Car
import json
def post_create_view(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, 'post_create.html', context)

@csrf_exempt
def test_json_response_view(request: WSGIRequest):
	print('-----------------------------------')
	if request.method == 'GET':
		print("get GET request: ", request)
		data = list(Car.objects.all().values())
		return JsonResponse(data,safe=False)
	elif request.method == 'POST':
		# get json data
		data = json.loads(request.body)
		print("get POST request data: ", data)

		# save to db
		Car.objects.create(CarName=data['CarName'],TimeStamp=data['TimeStamp'], Latitude=data['Latitude'], Longitude=data['Longitude'],CarSpeed=data['CarSpeed'],Heading=data['Heading'])
		# check posts in db
		print('all posts in db: ', Car.objects.all())

		# send response to client
		return JsonResponse({'status': 'Car was added successfully.'})
	elif request.method == 'DELETE':
		data = Car.objects.all()
		data.delete()
		return JsonResponse({'status': 'DELETE.'})
	else:
		print("get unknown request: ", request)
		return JsonResponse({'status': 'Failed, try again.'})