import asyncio
import json

import jsonpickle
import requests

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from kinopoisk_dev import KinopoiskDev, MovieParams, MovieField
from kinopoisk_dev.model import Movie, MovieDocsResponseDto

from userprofile.models import Account
from .models import Contact, Post, UserPostRelation
from .serializers import LeadSerializer
from rest_framework import generics

TOKEN = "PPKSD1X-3GVMPYM-J3W2ZMT-0TQN1JT"


class ContactsListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = LeadSerializer


async def get_random_async() -> Movie:
    """
    Асинхронный запрос.
    Получить рандомный фильм
    :return: Информация о фильме
    """
    kp = KinopoiskDev(token=TOKEN)
    return await kp.arandom()


async def get_movies_async(film_name) -> MovieDocsResponseDto:
    """
    Асинхронный запрос.
    Получить информацию о фильмы с использованием параметров
    :return: Список фильмов
    """

    kp = KinopoiskDev(token=TOKEN)
    item = await kp.afind_many_movie(
        params=[
            MovieParams(keys=MovieField.LIMIT, value=10),
            MovieParams(keys=MovieField.NAME, value=film_name),
        ]
    )
    return item


def index(request):
    data = {"data": asyncio.run(get_random_async())}
    request.session['data_film'] = data['data'].json()
    # request.session['data_film'] = jsonpickle.encode(data['data'])
    # print(data['data'].json())
    return render(request, "contacts/index.html", context=data)


def like(request, film_id):
    data = request.session['data_film']
    post = Post.objects.create(
        film_id=film_id,
        user=User.objects.get(id=request.user.id),
        j_field=json.loads(data)
    )
    post.save()
    user = User.objects.get(id=request.user.id)
    post_relation = UserPostRelation(
        user=user,
        post=post,
        like=True
    )
    post.postLike()
    post_relation.save()
    return redirect(f'contact:index')


def get_list_films(request):
    params = request.POST.get("film-params")
    data = {"films": asyncio.run(get_movies_async(params))}
    return render(request, "contacts/films.html", context=data)


class LikedFilmList(ListView):
    model = Post
    template_name = 'contacts/liked_films.html'
    context_object_name = 'post'
    queryset = Post.objects.all().order_by('-createdDate')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['most_like_post'] = Post.objects.order_by('-post_like').first()
    #     # context['title'] = 'Главная'
    #     try:
    #         user = User.objects.get(id=self.request.user.id)
    #         context['like'] = user.posts.filter(userpostrelation__like=True)
    #
    #     except Exception:
    #         pass
    #
    #     return context


def switch_mode(request):
    page = request.META.get('HTTP_REFERER')
    user = Account.objects.get(user=request.user.id)
    if request.POST.get('darkmode'):
        user.darkmode = True
    else:
        user.darkmode = False
    user.save()
    return redirect(f'{page}')
