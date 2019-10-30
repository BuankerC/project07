# Project 07

##### accounts에 따라 모델을 만들지 않은 상태에서 회원가입한 모든 유저정보를 불러올때 

```python
from django.contrib.auth import get_user_model

def index(request):
    User = get_user_model() # import해서 User라는 모델을 만들어줌
    real_users = User.objects.all()
    context = {
        'real_users':real_users,
    }
    return render(request, 'accounts/index.html',context)
```

##### 유저목록에서 username을 클릭 했을때 user가 좋아요 누른 영화와 작성한 댓글(평점) 가져올때

```python
def detail(request, id):
    User = get_user_model()
    user = get_object_or_404(User, id=id)
    context = {
        'user':user
    }
    return render(request, 'accounts/detail.html', context)
```

```html
{% extends 'base.html' %}
{% block body %}

  <h1>{{user.username}}가 좋아하는 영화</h1>
  {% for like_movie in user.like_movies.all %}
    <h5>{{like_movie.title}}</h5>
  {% endfor %}

  <h1>{{user.username}}가 달았던 댓글</h1>
  {% for review in user.reviews_set.all %}
    <h5>영화제목:{{review.movie_id.title}} : {{review.content}} : {{review.score}}</h5>
  {% endfor %}
{% endblock %}
```

##### 좋아요 기능 구현하기

```html
{% extends 'base.html' %}
{% block body %}
<div class="jumbotron jumbotron-fluid">
    <div class="container">
      <h1 class="display-4">{{movie.title}}</h1>
      <p class="lead">관객수 : {{movie.audience}}</p>
      <p class="lead">상세 설명 : {{movie.description}}</p>
    </div>
    {% if user.is_authenticated %}
    <form action="{% url 'movies:like' movie.id %}" method="POST">
      {% csrf_token %}
      {% if user in movie.like_movies_user.all %}
      <input type="submit" value="좋아요 취소">
      {% else %}
      <input type="submit" value="좋아요">
      {% endif %}
    </form>
```

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Reviews
from .forms import ReviewsForm

def like(request, id):
    movie = get_object_or_404(Movie, id=id)
    user = request.user
    if request.method == 'POST':
        if user in movie.like_movies_user.all():
            movie.like_movies_user.remove(user)
        else:
            movie.like_movies_user.add(user)
        return redirect('movies:detail', id)    
    else:
        pass
```

