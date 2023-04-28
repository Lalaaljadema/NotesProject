from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('new', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path("<int:pk>/delete", views.delete, name='delete'),
    path('signup/', views.signup, name="signup"),
    path('signin',views.signin, name='signin'),
    path('profile/<str:pk>',views.profile, name='profile'),
    path("like-notes", views.like_notes, name="like_notes"),
    path("<int:pk>/edit", views.edit, name='edit'),
]
