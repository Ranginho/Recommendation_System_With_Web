from app import app
from flask import render_template
from .request import businessArticles, entArticles, get_news_source, healthArticles, publishedArticles, randomArticles, scienceArticles, sportArticles, techArticles, topHeadlines
from app import request
from bs4 import BeautifulSoup
import urllib.request

@app.route('/')
def home():
    articles = publishedArticles()

    return  render_template('home.html', articles = articles)

@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    return  render_template('headlines.html', headlines = headlines)

@app.route('/articles')
def articles():
    random = randomArticles()

    return  render_template('articles.html', random = random)

@app.route('/sources')
def sources():
    newsSource = get_news_source()

    return  render_template('sources.html', newsSource = newsSource)

@app.route('/category/business')
def business():
    sources = businessArticles()

    return  render_template('business.html', sources = sources)

@app.route('/category/tech')
def tech():
    sources = techArticles()

    return  render_template('tech.html', sources = sources)

@app.route('/category/entertainment')
def entertainment():
    sources = entArticles()

    return  render_template('entertainment.html', sources = sources)

@app.route('/category/science')
def science():
    sources = scienceArticles()

    return  render_template('science.html', sources = sources)

@app.route('/category/sports')
def sports():
    sources = sportArticles()

    return  render_template('sport.html', sources = sources)

@app.route('/category/health')
def health():
    sources = healthArticles()

    return  render_template('health.html', sources = sources)

@app.route('/recommendation')
def recommendation_part():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print(request.curr_content)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sources = techArticles()


    
    
    return  render_template('tech.html', sources = sources)

@app.route('/category/recommendation1.html')
def recommendation1():
    return render_template('recommendation1.html')

@app.route('/category/recommendation2.html')
def recommendation2():
    return render_template('recommendation2.html')

@app.route('/category/recommendation3.html')
def recommendation3():
    return render_template('recommendation3.html')

@app.route('/category/recommendation4.html')
def recommendation4():
    return render_template('recommendation4.html')

@app.route('/category/recommendation5.html')
def recommendation5():
    return render_template('recommendation5.html')

@app.route('/category/recommendation6.html')
def recommendation6():
    return render_template('recommendation6.html')

@app.route('/category/recommendation7.html')
def recommendation7():
    return render_template('recommendation7.html')

@app.route('/category/recommendation8.html')
def recommendation8():
    return render_template('recommendation8.html')

@app.route('/category/recommendation9.html')
def recommendation9():
    return render_template('recommendation9.html')

@app.route('/category/recommendation10.html')
def recommendation10():
    return render_template('recommendation10.html')