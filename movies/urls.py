from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/reviews/new/', views.new, name='new'),
    path('<int:movie_id>/reviews/<int:review_id>/delete', views.delete, name='delete'),
]
