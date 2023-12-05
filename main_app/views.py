from django.shortcuts import render
# Temporary date
friends = [
    {'name': 'Nemo',
     'breed': 'Clownfish',
     'age': 6,
     'habitat': 'Anenome'},
     {'name': 'Marlin',
     'breed': 'Clownfish',
     'age': 42,
     'habitat': 'Anenome'},
     {'name': 'Dory',
     'breed': 'Regal Blue Tang',
     'age': 38,
     'habitat': 'Coral Reef'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def friends_index(request):
    return render(request, 'friends/index.html', {'friends': friends})