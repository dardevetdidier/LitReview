from itertools import chain

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db.models import CharField, Value
from django.contrib import messages
from django.utils import timezone

from AppReview.models import Review, Ticket, get_reviews, get_tickets
from .forms import TicketForm, ReviewForm, RegisterForm, LoginForm


def index(request):
    login_form = LoginForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('flux'))
        else:
            messages.info(request, "Erreur dans le nom d'utilisateur et/ou le mot de passe")

    return render(request, 'AppReview/index.html', {'login_form': login_form})


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = register_form.cleaned_data.get('username')
            messages.success(request, f'Compte créé avec Succès pour {user}')

            return HttpResponseRedirect(request.path)
    else:
        register_form = RegisterForm()
    return render(request, 'AppReview/register.html', {'register_form': register_form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='index')
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


@login_required(login_url='index')
def add_ticket(request):
    if request.method == 'POST':
        print(request.user)
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            print(ticket_form.cleaned_data)
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
        return HttpResponseRedirect(request.path)
    else:
        ticket_form = TicketForm(initial={"user": request.user})

    return render(request, 'AppReview/add_ticket.html', {"ticket_form": ticket_form})


@login_required(login_url='index')
def add_review(request):
    stars = []
    ticket_form = TicketForm()

    # Use add_ticket function
    add_ticket(request)
    if request.method == 'POST':

        print(f"methode = {request.method}")

        review_form = ReviewForm(request.POST)

        ticket = Ticket.objects.last()

        if review_form.is_valid():
            # print(review_form.cleaned_data)
            # print("review_form valide")
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

        return HttpResponseRedirect(reverse('flux'))

    else:
        review_form = ReviewForm()

    return render(request, 'AppReview/add_review.html', {"review_form": review_form,
                                                         "ticket_form": ticket_form,
                                                         })


@login_required(login_url='index')
def reply_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    # print(ticket)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            reply = review_form.save(commit=False)
            reply.user = request.user
            reply.ticket = ticket
            reply.save()
        return HttpResponseRedirect(reverse('flux'))

    else:
        review_form = ReviewForm()

    return render(request, 'AppReview/reply_ticket.html', {"reply_form": review_form})


@login_required(login_url='index')
def modify_review(request, pk):
    review = Review.objects.get(id=pk)
    modify_review_form = ReviewForm(instance=review)

    if request.method == 'POST':
        modify_review_form = ReviewForm(request.POST, instance=review)
        if modify_review_form.is_valid():
            modify = modify_review_form.save(commit=False)
            modify.time_created = timezone.now()
            modify.save()
        return HttpResponseRedirect(reverse('flux'))

    return render(request, 'AppReview/modify_review.html', {'modify_review_form': modify_review_form,
                                                            'review': review})


@login_required(login_url='index')
def modify_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    modify_ticket_form = TicketForm(instance=ticket)

    if request.method == 'POST':
        modify_ticket_form = TicketForm(request.POST, instance=ticket)
        if modify_ticket_form.is_valid():
            modify = modify_ticket_form.save(commit=False)
            ticket.time_created = timezone.now()
            modify.save()
        return HttpResponseRedirect(reverse('flux'))

    return render(request, 'AppReview/modify_ticket.html', {'modify_ticket_form': modify_ticket_form,
                                                            'ticket': ticket})


@login_required(login_url='index')
def delete_review(request, pk):
    print(request)
    review = Review.objects.get(id=pk)
    if request.method == 'POST':
        review.delete()
        return HttpResponseRedirect(reverse('flux'))

    return render(request, 'AppReview/delete_review.html', {'review': review})


@login_required(login_url='index')
def delete_ticket(request, pk):
    pass

