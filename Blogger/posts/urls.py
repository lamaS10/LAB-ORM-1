
from django.urls import path
from . import views



app_name = "posts"


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('add/', views.add_post_view, name='add_post_view'),
    path('detail/<int:post_id>/', views.detail_view, name='detail_view'),
    path('update/<int:post_id>/', views.update_post_view, name='update_post_view'),
    path('delete/<int:post_id>/', views.delete_post_view, name='delete_post_view'),




 ]