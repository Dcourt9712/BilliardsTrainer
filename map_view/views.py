from django.shortcuts import render, redirect, reverse
from django.conf import settings
# from django.contrib.gis.utils import GeoIP
from .mixins import Directions

'''
Get user info & ip stuff
'''
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

'''
Basic view for routing 
'''
def route(request):
  # g = GeoIP() 
  # lat,lng = g.lat_lon(get_client_ip(request))
  # print(f'\n  {lat}\n  {lng}\n')

  context = {"google_api_key": settings.API_KEY}
  return render(request, 'map_view/route.html', context)


'''
Basic view for displaying a map 
'''
def map(request):

	lat_a = request.GET.get("lat_a", None)
	long_a = request.GET.get("long_a", None)
	lat_b = request.GET.get("lat_b", None)
	long_b = request.GET.get("long_b", None)
	lat_c = request.GET.get("lat_c", None)
	long_c = request.GET.get("long_c", None)
	lat_d = request.GET.get("lat_d", None)
	long_d = request.GET.get("long_d", None)


	#only call API if all 4 addresses are added
	if lat_a and lat_b and lat_c and lat_d:
		directions = Directions(
			lat_a= lat_a,
			long_a=long_a,
			lat_b = lat_b,
			long_b=long_b,
			lat_c= lat_c,
			long_c=long_c,
			lat_d = lat_d,
			long_d=long_d
			)
	else:
		return redirect(reverse('map_view:route'))

	context = {
	"google_api_key": settings.API_KEY,
	"lat_a": lat_a,
	"long_a": long_a,
	"lat_b": lat_b,
	"long_b": long_b,
	"lat_c": lat_c,
	"long_c": long_c,
	"lat_d": lat_d,
	"long_d": long_d,
	"origin": f'{lat_a}, {long_a}',
	"destination": f'{lat_b}, {long_b}',
	"directions": directions,

	}
	return render(request, 'map_view/map.html', context)
