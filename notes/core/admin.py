from django.contrib import admin

from .models import Note, Profile, LikeNotes

admin.site.register(Note)
admin.site.register(Profile)
admin.site.register(LikeNotes)
