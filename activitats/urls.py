from django.conf.urls import url, include

from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'activitats'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'registre/$', views.registre, name='registre'),
    url(r'pantallaInici/$', views.pantallaInici, name='pantallaInici'),
    url(r'^editaractivitat/(?P<id_activitat>\d+)/', views.editarActivita, name='editarActivitat'),
    url(r'ensenyar/$', views.ensenyar, name='ensenyar'),
    url(r'activitatsPropies/$', views.activitatsPropies, name='activitatsPropies'),
    url(r'api_Localitats/$', views.apiLocalitats, name='localitats'),
    url(r'activitatDetallada/(?P<id_activitat>\d+)/$', views.activitatDetallada, name='activitatDetallada'),
    url(r'inscriures/', views.inscriures, name='inscriures'),

]