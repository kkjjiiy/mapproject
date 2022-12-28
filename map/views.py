from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
import folium

def checkCarName(request):
    # request should be ajax and method should be GET.
	if request.is_ajax and request.method == "GET":
        #get the car name from the client side.

		CarName = request.GET.get("CarName", None)
        #check for the car name in the database.

		#all_entries = Car.objects.all().e
		if Car.objects.filter(CarName = CarName).exists():
			#if Car.objects.all():

        # if nick_name found return not valid new car
			return JsonResponse({"valid":False}, status = 200)

		else:
            # if nick_name not found, then user can create a new car.
			return JsonResponse({"valid":True}, status = 200)

		#return JsonResponse({}, status = 400)
# Create your views here.
def index(request):
    # lon = Car.objects.filter('Longitude')
    # la = Car.objects.filter('Latitude')
    data = Car.objects.all().values()
    num = Car.objects.count()
    # create map object
    m = folium.Map(location=[25.0139376,121.5421717], zoom_start = 20)
    # folium.Marker([25.014614, 121.542910]).add_to(m) #C1
    # folium.Marker([25.012674, 121.542057]).add_to(m) #Car_2
    # folium.Marker([25.0139376,121.5421717]).add_to(m)
    # folium.Marker([25.0134056,121.5409975]).add_to(m)
    for i in range(0,num):
        folium.Marker([data[i]['Longitude'], data[i]['Latitude']],tooltip="%s: %f, %f" % (data[i]['CarName'],data[i]['Longitude'],data[i]['Latitude'])).add_to(m)
    # get html representation of map object
    m = m._repr_html_()
    context = {
        'm' : m,
        #asablu
    }
    return render(request, 'index.html', context)

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
		#return JsonResponse({'first': 'CarName','second': 'TimeStamp', 'third': 'Latitude', 'forth':'Longitude','fifth': 'CarSpeed','sixth': 'Heading'})
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
	else:
		print("get unknown request: ", request)
		return JsonResponse({'status': 'Failed, try again.'})