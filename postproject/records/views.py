from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Post 
# or you can also import records.models import Post if you want to provide absolute path

#Importing ListView API so that we can pass it as inheritence model to the controller
class PostListView(ListView):
	model = Post

class PostDetailView(DetailView):
	model = Post

class CreatePostView(CreateView):
	model = Post
	fields = ["title", "slug", "content", "image"]

class UpdatePostView(UpdateView):
	model = Post
	fields = ["title", "slug", "content", "image"]
	template_name_suffix = '_update_form'
	#If ypou want to do custom template skip the _suffix

class DeletePostView(DeleteView):
	model = Post
	success_url = reverse_lazy('list_posts')
	#Use the label from the urls.py that you want to recall