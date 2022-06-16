from django.contrib import admin
from chat.models import Room, Message

admin.site.register((Room, Message))