from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('sanaa',views.sanaa,name='sanaa'),
    path('<str:name>',views.greet,name='greet')
]