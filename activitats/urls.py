from django.conf.urls import url, include

from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'activitats'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'ensenyar/$', views.ensenyar, name='ensenyar'),

]