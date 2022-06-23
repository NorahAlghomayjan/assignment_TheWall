from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('post',views.post),
    path('comment/<int:postId>',views.comment), #comment on post
    path('deleteMsg/<int:postId>',views.deleteMsg),
    path('deleteComment/<int:comId>',views.deleteComment),
]