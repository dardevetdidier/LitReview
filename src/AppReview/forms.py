from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Ticket, Review, UserFollows


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': "Nom d'utilisateur..."}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': "Email..."}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': "Nom d'utilisateur..."}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                   'type': 'password',
                                                   'placeholder': 'Mot de passe'})
        }


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'image',
        ]
        labels = {
            'title': 'Titre',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Titre - Auteur'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Votre message...'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-sm'})
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        CHOICES = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
        model = Review
        fields = [
            'headline',
            'rating',
            'body',
        ]
        labels = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire',
        }
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.RadioSelect(choices=CHOICES, attrs={'class': 'form-check-inline radio-button'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = UserFollows

        fields = [

            'user'
        ]

        labels = {

            'user': ''
        }

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': "Nom d\'utilisateur",
                                           })
        }