from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Reviews
from .forms import ReviewsForm

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }

    return render(request, 'movies/index.html', context)

def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    review_form = ReviewsForm()
    context = {
        'movie':movie,
        'review_form':review_form,

    }
    return render(request, 'movies/detail.html', context)

def new(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            Review = form.save(commit=False)
            Review.movie_id = movie
            Review.user_id = request.user
            Review.save()
            return redirect('movies:detail', id)

def delete(request, movie_id, review_id):
    if request.method == 'POST':
        review = get_object_or_404(Reviews, id=review_id)
        review.delete()
    return redirect('movies:detail', movie_id)