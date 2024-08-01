from django.contrib import admin
from .models import Room_Name,ChatMessage
# Register your models here.

@admin.register(Room_Name)
class Room_NameAdmin(admin.ModelAdmin):
     list_display=['id','room_name','created_at']

@admin.register(ChatMessage)
class ChatAdmin(admin.ModelAdmin):
     list_display=['id','content','timeStamp','group']