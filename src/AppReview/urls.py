from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('flux/', views.flux, name='flux'),
    path('add-ticket/', views.add_ticket, name='add-ticket')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
