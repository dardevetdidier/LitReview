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
    path('modify-ticket/<str:pk>/', views.modify_ticket, name='modify-ticket'),
    path('delete-review/<str:pk>/', views.delete_review, name='delete-review'),
    path('delete-ticket/<str:pk>/', views.delete_ticket, name='delete-ticket'),
    path('posts/', views.user_posts, name='posts'),
    path('subscriptions/', views.subscription, name='subscription'),
    path('unsubscribe/<str:pk>/', views.unsubscribe, name='unsubscribe'),
]
