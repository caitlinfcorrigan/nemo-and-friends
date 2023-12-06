from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Friend

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def friends_index(request):
    friends = Friend.objects.all()
    return render(request, 'friends/index.html', {'friends': friends})

def friends_detail(request, friend_id):
    friend = Friend.objects.get(id=friend_id)
    return render(request, 'friends/detail.html', { 'friend': friend})

class FriendCreate(CreateView):
    model = Friend
    fields = '__all__'

class FriendUpdate(UpdateView):
    model = Friend
    fields = ['breed', 'age', 'habitat']

class FriendDelete(DeleteView):
    model = Friend
    success_url = '/friends'