from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'doctor'

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^profile/(?P<pk>[0-9]+)/$', views.profile, name='profile'),
                  url(r'^doctor_certification/(?P<pk>[0-9]+)$', views.doctor_certification, name='doctor_certification'),
                  url(r'^individual_certification/(?P<pk>[0-9]+)$', views.individual_certification, name='individual_certification'),
                  #url(r'^enterprise_certification/(?P<pk>[0-9]+)$', views.enterprise_certification, name='enterprise_certification'),
                  url(r'^doctor_form/(?P<pk>[0-9]+)$', views.doctor_form, name='doctor_form'),
                  url(r'^for_user/(?P<pk>[0-9]+)$', views.for_user, name='for_user'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
