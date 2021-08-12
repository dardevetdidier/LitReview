from itertools import chain

from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db.models import CharField, Value

from AppReview.models import Review, Ticket
from .forms import TicketForm, ReviewForm, RegisterForm, LoginForm


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('flux'))
    else:
        login_form = LoginForm()
    return render(request, 'AppReview/index.html', {'login_form': login_form})


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            register_form.save()

        return HttpResponseRedirect(request.path)
    else:
        register_form = RegisterForm()
    return render(request, 'AppReview/register.html', {'register_form': register_form})

# A mettre dans models :______________________

def get_reviews(request):
    """returns a queryset of reviews"""
    return Review.objects.all()


def get_tickets(request):
    """returns a queryset of tickets"""
    return Ticket.objects.all()

# ___________________________________


def flux(request):
    reviews = get_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = get_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'AppReview/flux.html', {'posts': posts})


def add_ticket(request):
    if request.method == 'POST':
        print(request.user)
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            print(ticket_form.cleaned_data)
            ticket_form.save()
        return HttpResponseRedirect(request.path)
    else:
        ticket_form = TicketForm(initial={"user": request.user})

    return render(request, 'AppReview/add_ticket.html', {"ticket_form": ticket_form})


def add_review(request):
    print(f"methode = {request.method}")
    if request.method == 'POST':
        print(f"methode = {request.method}")
        ticket_form = TicketForm(request.POST, request.FILES, "ticket_form")
        review_form = ReviewForm(request.POST, request.FILES, "review_form")
        if ticket_form.is_valid() and review_form.is_valid():
            print("valide")
            ticket_form.save()
            review_form.save()
        return HttpResponseRedirect(request.path)
    else:
        ticket_form = TicketForm(initial={"user": request.user})
        review_form = ReviewForm(initial={"user": request.user})

    return render(request, 'AppReview/add_review.html', {"review_form": review_form,
                                                         "ticket_form": ticket_form})


def display_ticket(request):
    return render(request, 'AppReview/ticket_snippet.html', {})


def display_review(request):
    return render(request, 'AppReview/review_snippet.html', {})
