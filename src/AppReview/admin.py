from django.contrib import admin
from .models import Ticket, Review, UserFollows


# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "user",
        "time_created",
        "reply",
    )
    empty_value_display = "Inconnu"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "ticket",
        "user",
        "rating",
        "time_created",
    )
    empty_value_display = "Inconnu"


@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'followed_user'
    )
    empty_value_display = "Inconnu"


