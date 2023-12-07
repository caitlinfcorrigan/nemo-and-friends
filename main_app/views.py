from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Friend
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'friends/detail.html', { 'friend': friend, 'feeding_form': feeding_form })

def add_feeding(request, friend_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.friend_id = friend_id
        new_feeding.save()
    return redirect('detail', friend_id=friend_id)

class FriendCreate(CreateView):
    model = Friend
    fields = '__all__'

class FriendUpdate(UpdateView):
    model = Friend
    fields = ['breed', 'age', 'habitat']

class FriendDelete(DeleteView):
    model = Friend
    success_url = '/friends'