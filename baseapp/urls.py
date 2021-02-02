from django.urls import path
from .views import home, result, mess, newsfeed

urlpatterns = [
    path('', home, name="home"),
    path('result/<email>/', result, name="result"),
    path('mess/<email>/', mess, name="mess"),
    path('newsfeed/', newsfeed, name="newsfeed")
]
