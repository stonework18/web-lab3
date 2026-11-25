from django.shortcuts import render
from .models import Review

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
        'title': 'Список отзывов'
    }

    return render(request, 'reviews/index.html', context)
