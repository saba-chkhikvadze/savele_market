from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('create-post/', views.create_post, name='create_post'),
    path('make-offer/<str:pk>', views.make_offer, name='make_offer'),
    path('my-offers/<str:pk>', views.view_offer, name='view_offers'),
    path('edit-post/<str:pk>', views.edit_post, name='edit_post'),
    path('post-deleted/<str:pk>', views.delete_post, name='post_deleted'),
    path('about/', views.about, name='about'),
]
