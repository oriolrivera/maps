#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('maps.app.views',
	url(r'^$', 'home_view', name="home"),
	url(r'^coords/save/$', 'coordSave_view', name="coordSave_vista"),

)