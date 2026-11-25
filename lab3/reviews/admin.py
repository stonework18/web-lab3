from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'author', 'rating', 'created_at') 
    # список, который виден
    list_display_links = ('id', 'product_name') 
    # список для ссылок
    search_fields = ('product_name', 'author', 'text') 
    # поиск полей работает по ним

admin.site.register(Review)