from django.urls import path
from .views import *

app_name = 'contact'

urlpatterns = [
    path('api/lead/', ContactsListCreate.as_view()),
    path('', index, name='index'),
    path('films/', get_list_films, name='films'),
    path('<int:film_id>/like/', like, name='like'),
    path('liked_films/', LikedFilmList.as_view(), name='liked_films'),
    #path('news/', get_news, name='news'),
    path('switch_mode/', switch_mode, name='switch_mode')
]
