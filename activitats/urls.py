from django.conf.urls import url, include

from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'activitats'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'registre/$', views.registre, name='registre'),
    url(r'pantallaInici/$', views.pantallaInici, name='pantallaInici'),
    url(r'editaractivitat/(?P<id_activitat>\d+)/', views.editarActivita, name='editarActivitat'),
    url(r'ensenyar/$', views.ensenyar, name='ensenyar'),
    url(r'comentaris/$', views.comentaris, name='comentaris'),
    url(r'activitatsPropies/$', views.activitatsPropies, name='activitatsPropies'),
    url(r'api_Localitats/$', views.apiLocalitats, name='localitats'),
    url(r'activitatDetallada/(?P<id_activitat>\d+)/$', views.activitatDetallada, name='activitatDetallada'),
    url(r'inscriures/', views.inscriures, name='inscriures'),
    url(r'eliminaractivitat/', views.deleteActivitat, name='eliminaractivitat'),
    url(r'crearComentari/', views.crearComentari, name='crearComentari'),
    url(r'editarPerfil/', views.editarPerfil, name='editarPerfil'),
    url(r'activitatsincrit/', views.activitatsincrit, name='activitatsincrit'),
    url(r'filtrecategoria/', views.filtrecomentari, name='filtrecategoria'),
    url(r'coockies/', views.coockies, name='coockies'),
    url(r'privacitat/', views.privacitat, name='privacitat'),
    url(r'avislegal/', views.avislegal, name='avislegal'),

]

#escript que s'executi cada dai eliminan les activitats passades
#    url(r'filtrecategoria/<str:nomcategoria>/', views.filtrecomentari, name='filtrecategoria'), passar string
