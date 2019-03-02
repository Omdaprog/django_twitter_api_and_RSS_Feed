from django.urls import path
from . import views

urlpatterns = [
    path('',views.my_tweet_list, name='tweet_list'),
    path('search/',views.tweet_search, name='tweet_search'),
    path('ytsrss/',views.YtsRssFeed, name='YTS_RSS')
]