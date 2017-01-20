from django.conf.urls import url, include  # add include
from . import views  # add this to inherit views from source "."= source

urlpatterns = [
	url(r'^$', views.index),  # add $ to get all wildcards in regex and dot notation OOP the loc of index function add a comma!
	url(r'^surveyPost$', views.surveyPost),
	url(r'^result$', views.result),
	url(r'^en/(?P<id>\d+)$', views.show),

]  # this is a list to add the closing ]
