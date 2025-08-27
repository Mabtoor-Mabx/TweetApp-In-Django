from django.contrib import admin
from .models import Tweet, Profile

# Register your models here.

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')
    search_fields = ('author__username', 'content')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

