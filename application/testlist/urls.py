from django.conf.urls import url
from testlist import views

urlpatterns = [
	url(r'^$', views.home),
	# url(r'^food/$', views.food_list),
	# url(r'^food/(?P<pk>[0-9]+)/$', views.food_detail),
]