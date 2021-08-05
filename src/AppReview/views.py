from django.shortcuts import render


def index(request):
    return render(request, 'AppReview/index.html')

# Create your views here.
