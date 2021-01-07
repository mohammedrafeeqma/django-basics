from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    #this is the path for index in  views.py in products app. name is only fot identity
    path('about',views.about)
]