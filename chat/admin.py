from django.contrib import admin

# Register your models here.
from chat.models import Chatroom, Chat

admin.site.register(Chatroom)
admin.site.register(Chat)