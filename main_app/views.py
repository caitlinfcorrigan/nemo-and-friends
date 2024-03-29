from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Friend, Decor
from .forms import FeedingForm

# Create your views here.def home(request):
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def friends_index(request):
    friends = Friend.objects.all()
    return render(request, 'friends/index.html', {'friends': friends})

def friends_detail(request, friend_id):
    # Get the friend from the Friend model
    friend = Friend.objects.get(id=friend_id)
    # Bring in the FeedingForm (from forms.py)
    feeding_form = FeedingForm()
    # Select their associated decor
    id_list = friend.decor.all().values_list('id')
    # Get the list of decor not associated with the friend
    decor_friend_doesnt_have = Decor.objects.exclude(id__in=id_list)
    # Render the template using the above variables as inputs
    return render(request, 'friends/detail.html', { 'friend': friend, 'feeding_form': feeding_form, 'decor': decor_friend_doesnt_have })

# POST endpoint for FeedingForm on the friend detail page
def add_feeding(request, friend_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.friend_id = friend_id
        new_feeding.save()
    return redirect('detail', friend_id=friend_id)

# Handle Add decor button on friend detail page
def assoc_decor(request, friend_id, decor_id):
   Friend.objects.get(id=friend_id).decor.add(decor_id)
   return redirect('detail', friend_id=friend_id)

# Handle Delete decor button on friend detail page
def unassoc_decor(request, friend_id, decor_id):
   Friend.objects.get(id=friend_id).decor.remove(decor_id)
   return redirect('detail', friend_id=friend_id)

class DecorList(ListView):
  model = Decor

class DecorDetail(DetailView):
  model = Decor

class DecorCreate(CreateView):
  model = Decor
  fields = '__all__'

class DecorUpdate(UpdateView):
  model = Decor
  fields = ['name', 'color']

class DecorDelete(DeleteView):
  model = Decor
  success_url = '/decor'

class FriendCreate(CreateView):
    model = Friend
    fields = ['name', 'breed', 'age', 'habitat']

class FriendUpdate(UpdateView):
    model = Friend
    fields = ['breed', 'age', 'habitat']

class FriendDelete(DeleteView):
    model = Friend
    success_url = '/friends'