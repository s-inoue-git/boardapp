from django.urls import path
from .views import hello_func, list_func, detail_func, BoardCreate, good_func

urlpatterns = [
    path('hello/', hello_func, name='hello'),
    path('list/', list_func, name='list'),
    path('detail/<int:pk>', detail_func, name='detail'),
    path('create', BoardCreate.as_view(), name='create'),
    path('good/<int:pk>', good_func, name='good'),
]

