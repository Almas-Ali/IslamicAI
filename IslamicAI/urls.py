from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    # path('quran/', include('quran.urls')),
    # path('hadis/', include('hadis.urls')),
]
