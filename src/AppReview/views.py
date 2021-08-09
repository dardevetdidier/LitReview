from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render

from AppReview.models import Review
from .forms import TicketForm


def index(request):
    return render(request, 'AppReview/index.html')


def flux(request):
    reviews = Review.objects.all()
    return render(request, 'AppReview/flux.html', {"reviews": reviews})


def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = TicketForm(initial={"user": request.user})

    return render(request, 'AppReview/add_ticket.html', {"form": form})

