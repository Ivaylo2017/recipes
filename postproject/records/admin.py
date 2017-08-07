from django.contrib import admin
from records.models import Post

admin.site.register(Post) # makes Django create an HTML template for the Post similar to the users
