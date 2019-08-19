from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.prediction, name='prediction'),
    url(r'^$', views.image_upload, name = 'image_upload'),
]

