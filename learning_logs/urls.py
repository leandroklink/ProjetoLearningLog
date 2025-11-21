from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topic/<topic_id>/', views.topic, name='topic'), #paths como essa tem <topic.id> como uma exigencia para entrar na página
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete-entry/<int:entry_id>/', views.delete_entry, name='delete_entry')
]
 