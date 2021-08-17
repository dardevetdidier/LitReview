from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('flux/', views.flux, name='flux'),
    path('add-ticket/', views.add_ticket, name='add-ticket'),
    path('add-review/', views.add_review, name='add-review'),
    path('reply-ticket/<str:pk>/', views.reply_ticket, name='reply-ticket'),
    path('modify-review/<str:pk>/', views.modify_review, name='modify-review'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
