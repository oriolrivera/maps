from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.utils.timesince import timesince
from maps.app.models import UbicacionForm, Ubicacion


#vista home
def home_view(request):
	form = UbicacionForm()
	ubicaciones = Ubicacion.objects.all().order_by('-fecha')
	ctx = {'form':form, 'ubicaciones':ubicaciones}
	return render_to_response('home/home.html',ctx,context_instance=RequestContext(request))

def coordSave_view(request):
	if request.is_ajax():
		form = UbicacionForm(request.POST)
		if form.is_valid():
			form.save()
			ubicaciones = Ubicacion.objects.all().order_by('-fecha')
			data = '<ul>'
			for ubicacion in ubicaciones:
				data += '<li>%s %s <small> - hace %s</li></small>' % (ubicacion.nombre, ubicacion.user, timesince(ubicacion.fecha))
			data += '</ul>'
			return HttpResponse(simplejson.dumps({'ok':True, 'msg':data}), mimetype='application/json')
		else:
			return HttpResponse(simplejson.dumps({'ok':False, 'msg':'Todos los campos son necesarios'}), mimetype='application/json')




