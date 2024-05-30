from django.urls import path
from .views import (all_posts,posts_by_category,post_detail,post_created,post_ubdare,post_delete,category_created, category_ubdate,category_delete,
                    user_login,user_logout,user_register,profile,create_comment)

urlpatterns = [
    path('',all_posts,name='index'),
    path('category/<int:category_id>/',posts_by_category,name='bolim'),
    path('detail/<int:pk>/',post_detail,name='post_detail'),
    path('add/',post_created,name='post_created'),
    path('update/<int:pk>/',post_ubdare,name='post_update'),
    path('delete/<int:pk>/',post_delete,name='post_delete'),
    path('add_category/',category_created,name='category_created'),
    path('category_update/<int:pk>/',category_ubdate,name='category_ubdate'),
    path('delete_category/<int:pk>/',category_delete,name='category_delete'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',user_register,name='register'),
    path('profile/<str:username>/',profile,name='profile'),
    path('add_comment/<int:post_id>/',create_comment,name="create_comment"),
]