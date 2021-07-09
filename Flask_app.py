from flask import Flask, render_template, send_from_directory
import requests
import os
from gnewsclient import gnewsclient
import time
app = Flask(__name__)

@app.route("/world")
def world():
    
##    client = gnewsclient.NewsClient(language='english', location='india', topic='world'
##                                ,max_results=30)
##
##    news_list = client.get_news()

    news_requests = "https://newsapi.org/v2/top-headlines?country=in&apiKey=44e68d37c8e74d019b80410a1456df39&pageSize=30"
    news_response = requests.get(news_requests)
    news = news_response.json()
    current_time = time.ctime()

    article = []
    links = []
    description =[]
    #des = []
    for item in news['articles']:
        article.append(item['title'])
        links.append(item['url'])
        description.append(item['description'])

    return render_template('news.html', articals = article,des = description, link = links ,time = current_time, starting_heading = "Get Latest News  From Every Corner of the World",
                           next_heading =  "Get updated with currect situation in the world. Stay connected with us")






@app.route("/")
def nation():
    news_requests = "https://newsapi.org/v2/top-headlines?country=in&apiKey=44e68d37c8e74d019b80410a1456df39&pageSize=30"
    
    news_response = requests.get(news_requests)
    news = news_response.json()
    current_time = time.ctime()

    article = []
    links = []
    description =[]
    #des = []
    for item in news['articles']:
        article.append(item['title'])
        links.append(item['url'])
        description.append(item['description'])


    return render_template('news.html', articals = article,des = description, link = links ,time = current_time, starting_heading = " Get Latest News and Updates with NewsDairy",
                           next_heading = " Get updated with currect situation in the world. Stay connected with us")


@app.route("/buisness")
def business():
    news_requests = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=44e68d37c8e74d019b80410a1456df39&pageSize=30"
    news_response = requests.get(news_requests)
    news = news_response.json()
    current_time = time.ctime()

    article = []
    links = []
    description =[]
    #des = []
    for item in news['articles']:
        article.append(item['title'])
        links.append(item['url'])
        description.append(item['description'])

    return render_template('news.html', articals = article, des = description,link = links ,time = current_time, starting_heading = " Get Latest Buisness News With NewsDairy",
                           next_heading = " Get updated with business news and what is going in the market")


@app.route("/technology")
def technology():
    news_requests = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=44e68d37c8e74d019b80410a1456df39&pageSize=30"
    news_response = requests.get(news_requests)
    news = news_response.json()
    current_time = time.ctime()

    article = []
    links = []
    description =[]
    #des = []
    for item in news['articles']:
        article.append(item['title'])
        links.append(item['url'])
        description.append(item['description'])


    return render_template('news.html', articals = article,des = description, link = links ,time = current_time, startin_heading = " Get Latest Technology News With NewsDairy",
                           next_heading = 'Get Updated with latest technology')

@app.route("/entertainments")
def entertainments():
    news_requests = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=44e68d37c8e74d019b80410a1456df39&pageSize=30"
    news_response = requests.get(news_requests)
    news = news_response.json()
    current_time = time.ctime()

    article = []
    links = []
    description =[]
    #des = []
    for item in news['articles']:
        article.append(item['title'])
        links.append(item['url'])
        description.append(item['description'])


    return render_template('news.html', articals = article,des = description, link = links ,time = current_time, starting_heading = " Get Latest Entertainments News With NewsDairy",
                           next_heading = "Get Updated with latest movies and entertainment industry news ")


@app.route("/sports")
def sports():
    news_requests = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=44e68d37c8e74d019b80410a1456df39&pageSize=30"
    news_response = requests.get(news_requests)
    news = news_response.json()
    current_time = time.ctime()

    article = []
    links = []
    description =[]
    #des = []
    for item in news['articles']:
        article.append(item['title'])
        links.append(item['url'])
        description.append(item['description'])


    return render_template('news.html', articals = article, des = description,link = links ,time = current_time, starting_heading = " Get Latest Sports News With NewsDairy",
                           next_heading = "Get updated with criket, football and other sports news")


@app.route("/science")
def science():
    news_requests = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=44e68d37c8e74d019b80410a1456df39&pageSize=30"
    news_response = requests.get(news_requests)
    news = news_response.json()
    current_time = time.ctime()

    article = []
    links = []
    description =[]
    #des = []
    for item in news['articles']:
        article.append(item['title'])
        links.append(item['url'])
        description.append(item['description'])


    return render_template('news.html', articals = article,des = description, link = links ,time = current_time,starting_heading = " Get Latest Scientific News With NewsDairy",
                           next_heading = "Get updated with latest research and studies")


@app.route("/health")
def health():
    news_requests = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=44e68d37c8e74d019b80410a1456df39&pageSize=30"
    news_response = requests.get(news_requests)
    news = news_response.json()
    current_time = time.ctime()

    article = []
    links = []
    description =[]
    #des = []
    for item in news['articles']:
        article.append(item['title'])
        links.append(item['url'])
        description.append(item['description'])


    return render_template('news.html', articals = article,des = description, link = links ,time = current_time, starting_heading = " Get Latest News Related to Health With NewsDairy",
                           next_heading="Get updated with coronavirus and its precautions. Stay Home and Stay Safe")




app.run(debug=True)


