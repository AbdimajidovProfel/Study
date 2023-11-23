from django.contrib import admin
from .models import *


class RoomAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created", "category"]
    list_display_links = ['title', 'content']
    search_fields = ['title', 'content']


admin.site.register(Category)
admin.site.register(Message)
admin.site.register(RoomModel, RoomAdmin)
