from django.contrib import admin
from django.contrib.admin import ModelAdmin

from chat.models import *


@admin.register(ChatRoom)
class ChatRoomAdmin(ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(ModelAdmin):
    pass