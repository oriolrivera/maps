from django.shortcuts import render_to_response
from django.template import RequestContext
from maps.app.models import UbicacionForm


#vista home
def home_view(request):
	form = UbicacionForm()
	ctx = {'form':form}
	return render_to_response('home/home.html',ctx,context_instance=RequestContext(request))



