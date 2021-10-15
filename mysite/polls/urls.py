from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('getchp/', views.getchp, name='getchp'),
    # ex: /polls/5/
    path('postpic/', views.upload, name='postpic'),
]