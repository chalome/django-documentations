from django.urls import path 
from .views import *

urlpatterns=[
    path("",IndexView.as_view(),name="index",),
    path("<int:pk>/",DetailView.as_view(),name="detail"),
    path("not_found/",not_found,name="not_found"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("<int:pk>/results/",ResultView.as_view(), name="results"),

]