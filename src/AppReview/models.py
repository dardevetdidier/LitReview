from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    reply = models.BooleanField(default=False)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ticket de {self.user} - {self.title}"


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Critique"
        ordering = ["-time_created"]

    def __str__(self):
        return self.ticket.title

    @property
    def stars_checked(self):
        """
        A list used to display the number of checked rating stars

        :return list: A list of n elements (n=rating) used to display checked rating stars
        """
        stars_checked = list(range(self.rating))
        return stars_checked

    def stars_unchecked(self):
        """
        A list used to display the number of unchecked rating stars

        :return list: A list of n elements (n = 5 - rating)
        """
        remain = 5 - self.rating
        stars_unchecked = list(range(remain))
        return stars_unchecked


class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by',
                                      null=True, blank=True)

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user')
        verbose_name_plural = "UsersFollows"


def get_reviews(request):
    """returns a queryset of all reviews"""
    return Review.objects.all()


def get_tickets(request):
    """returns a queryset of all tickets"""
    return Ticket.objects.all()
