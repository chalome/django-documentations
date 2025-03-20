from django.urls import path 
from .views import *

urlpatterns=[
    path("",index,name="index",),
    path("<int:question_id>/",detail,name="detail"),
    path("not_found/",not_found,name="not_found"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("<int:question_id>/results/",results, name="results"),

]