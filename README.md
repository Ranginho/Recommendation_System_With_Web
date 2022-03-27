
# News Recommendation System

### Description:

This is a web application that is used as a news recommendation system(based on **flask**). This application scrapes news from several well-known web-pages(using **NewsApiClient**), it has several sections: headlines, articles, categories(business, technology, entertainment, science, sport and health). It also has a section named 'sources' where you can see web pages that are used for scraping. When you run an application, it scrapes articles and shows you articles from any category(random articles). If you click on any category, the application scrapes news according to category, saves them in the database(I used **sqlite** database because it is not a real application and I use **sqlalchemy** library for working with db). I calculate recommendations for each article using a **content-based filtering** algorithm(used **sklearn cosine_similarity and TfidfVectorizer**) and save it in the database. Then the program chooses 10 random articles from that category and it appears with recommendations in a webpage. If you click on any recommendation, it opens the original webpage with an article. It is envisaged that one article shouldn't appear twice in recommendations and also an article can't be a recommendation for itself. **The main purpose** of creating this project is to get an experience of working with recommendation systems and databases, for visualisation I used **html** and **css** pages that were already done by others. As a future plan I'm going to add some other types of recommendations(**user-based collaborative filtering, item-based collaborative filtering**...).

## How to install and run the project:

you need to install requirements.txt file and mysql, flask-sqlalchemy (simple pip install). I used dbbrowser for sql gui. When you install all these things, then you can run main.py file (python main.py from terminal) and enjoy the web app.
