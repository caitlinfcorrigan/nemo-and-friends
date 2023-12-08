from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('friends/', views.friends_index, name='index'),
    path('friends/<int:friend_id>/', views.friends_detail, name='detail'),
    path('friends/create/', views.FriendCreate.as_view(), name='friends_create'),
    path('friends/<int:pk>/update/', views.FriendUpdate.as_view(), name='friends_update'),
    path('friends/<int:pk>/delete/', views.FriendDelete.as_view(), name='friends_delete'),
    path('friends/<int:friend_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('decor/', views.DecorList.as_view(), name='decor_index'),
    path('decor/<int:pk>/', views.DecorDetail.as_view(), name='decor_detail'),
    path('decor/create/', views.DecorCreate.as_view(), name='decor_create'),
    path('decor/<int:pk>/update/', views.DecorUpdate.as_view(), name='decor_update'),
    path('decor/<int:pk>/delete/', views.DecorDelete.as_view(), name='decor_delete'),
]