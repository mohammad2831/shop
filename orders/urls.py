from django.urls import path
from . import views


app_name='orders'

urlpatterns=[
    path('cards', views.CardsView.as_view(), name='cards')
]