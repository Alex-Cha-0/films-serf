from django.urls import path
from chat.views import chat_room, create_message, index, room

app_name = 'chat'

# urlpatterns = [
#     path('<int:room_id>/', chat_room, name='chat_room'),
#     path('<int:room_id>/create/', create_message, name='create_message'),
# ]

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
