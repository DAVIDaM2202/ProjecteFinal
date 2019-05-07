from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('activitats.urls', namespace='activitats')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

]
