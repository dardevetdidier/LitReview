from django.contrib import admin
from .models import Ticket, Review, UserFollows


# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "ticket",
        "user",
        "rating",
        "time_created",
    )
    empty_value_display = "Inconnu"


@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    pass


