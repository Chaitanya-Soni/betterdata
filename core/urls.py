from django.contrib import admin
from django.urls import path ,include
from .views import *
from rest_framework.routers import DefaultRouter

#from .views import posts ,postsDetail
urlpatterns = [
    path('proj/', Projectlist.as_view()),
    path('proj/<int:id>', Projectdetail.as_view()),
    path('real_data/<int:id>', RealdataDetail.as_view()),
    path('proj/<int:idp>/real_data/',Realdatalist.as_view()),
    path('model_data/<int:id>', ModelDetail.as_view()),
    path('proj/<int:idp>/model_data/',modellist.as_view()),
    path('model_data/<int:id1>/synthetic/<int:id2>', SyntheticDataDetail.as_view()),
    path('model_data/<int:id1>/synthetic/', SyntheticDatalist.as_view()),
]