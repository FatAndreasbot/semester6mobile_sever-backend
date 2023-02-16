from django.contrib import admin
from .models import Profile, Hostel, Room
from announcement_board.models import Post, Comment, Tags

# Register your models here.

admin.site.register(Profile)
admin.site.register(Hostel)
admin.site.register(Room)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tags)
