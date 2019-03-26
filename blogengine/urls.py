
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]

from django.conf import settings
if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
