from django import forms

from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'user',
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
        model = Review
        fields = [
            'ticket',
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
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }