from django.contrib import admin
from django.contrib.admin import ModelAdmin

from contacts.models import *


@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    pass


@admin.register(UserPostRelation)
class UserPostRelationAdmin(ModelAdmin):
    pass
