from django.shortcuts import render,redirect
from .models import Tweet
from .twitter import my_user_tweets,search_tweets
from urlextract import URLExtract
import feedparser

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def my_tweet_list(request):
    
    tweets = Tweet.objects.order_by('-published_date')
    stuff_for_frontend = {'tweets': tweets}
    print('my_tweet_list is work')
    return render(request,'twitter/tweet_list.html', stuff_for_frontend)
    
def tweet_search(request):
    user=[]
    dataBase = []
    data = []
    tweepy = []
    if request.method == 'POST':
        tweets = search_tweets(request.POST.get('name'),request.POST.get('number'))
        print(request.POST.get('number'))
        print(user)
        for tweet in tweets:
            tweepy.append(tweet.full_text)
        dataBase = list(Tweet.objects.all().values('tweet_text'))
        
        for i in dataBase:
            for j in i :
                data.append(i[j])
        
        for T in tweepy :
            if T in data:
                user.append('Soory we cant find him')
                break
            else:
                user.append(T) 
                

        stuff_for_frontend = {"user":user}
        print(user)
        print ("user_tweets's func is work")
        return render(request,'twitter/tweets_search.html', stuff_for_frontend)
    else:
        print("the function search tweets didnt work")
        return render(request,'twitter/tweets_search.html',{"user":user})


def Divition(list):
    list = list.split('\t')
    list = ''.join(list)
    list = list.split('<br>')
    list = ''.join(list)
    list = list.split('</a>')
    list = ''.join(list)
    list = list.split('\n')
    return list


def YtsRssFeed(request):
    movies = {0:{"title":"" ,"description":"", "image_link":"","rating":"","genre":"","link":"","downloads":""},
              1:{"title":"" ,"description":"", "image_link":"","rating":"","genre":"","link":"","downloads":""},
              2:{"title":"" ,"description":"", "image_link":"","rating":"","genre":"","link":"","downloads":""},
              3:{"title":"" ,"description":"", "image_link":"","rating":"","genre":"","link":"","downloads":""},
              4:{"title":"" ,"description":"", "image_link":"","rating":"","genre":"","link":"","downloads":""},
              5:{"title":"" ,"description":"", "image_link":"","rating":"","genre":"","link":"","downloads":""},
              6:{"title":"" ,"description":"", "image_link":"","rating":"","genre":"","link":"","downloads":""}}
    feeds = feedparser.parse('https://yify.is/api/rss')
    for i in range(0,(len(feeds['entries']))):
        feed = feeds['entries'][i]['summary_detail']['value']
        feed = Divition(feed)
        extractor = URLExtract()

        image_link = extractor.find_urls(feed[1])
        image_link = ''.join(image_link)
        image_link = 'https://' + image_link
        movies[i]["image_link"]=image_link
        
        titles = feeds['entries'][i]['title']
        titles = ''.join(titles)
        movies[i]["title"]=titles
        
        description = feed[6]
        description = ''.join(description)
        movies[i]["description"]=description
        
        rating = feed[3]
        rating = ''.join(rating)
        movies[i]["rating"]=rating

        genre = feed[4]
        genre = ''.join(genre)
        movies[i]["genre"]=genre

        link = feeds['entries'][0]['link']
        link = ''.join(link)
        movies[i]["link"]=link

        downloads = feed[5]
        downloads = ''.join(downloads)
        movies[i]["downloads"]=downloads

    stuff_for_frontend = {'movies':movies}
    return render(request,'twitter/YTS_RSS.html',stuff_for_frontend)













