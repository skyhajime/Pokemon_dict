from django.contrib import admin
from .models import Item, Image
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass