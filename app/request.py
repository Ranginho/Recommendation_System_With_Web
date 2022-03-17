from .models import Articles
from .models import Sources
from newsapi import NewsApiClient
from .config import Config
import urllib.request,json
import json
from app.database import Helpers

api_key=None
base_url=None
base_url_for_everything=None
base_url_top_headlines=None
base_source_list=None

def publishedArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    get_articles = newsapi.get_everything(sources= 'cnn, reuters, cnbc, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_articles = get_articles['articles']

    articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(all_articles)):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)
    
    return  contents

def topHeadlines():
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    top_headlines = newsapi.get_top_headlines(sources= 'cnn, reuters, cnbc, techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_headlines = top_headlines['articles']

    articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(all_headlines)):
        headline = all_headlines[i]

        source.append(headline['source'])
        title.append(headline['title'])
        desc.append(headline['description'])
        author.append(headline['author'])
        img.append(headline['urlToImage'])
        p_date.append(headline['publishedAt'])
        url.append(headline['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)

    return  contents

def randomArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    random_articles = newsapi.get_everything(sources= 'the-verge, gizmodo, the-next-web, recode, ars-technica')

    all_articles = random_articles['articles']

    articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(all_articles)):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)

    return  contents

def businessArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    business_articles = newsapi.get_top_headlines(category='business')

    all_articles = business_articles['articles']

    business_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(all_articles)):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        business_articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)

    return  contents

def techArticles():
    '''
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    tech_articles = newsapi.get_top_headlines(category='technology')

    all_articles = tech_articles['articles']

    tech_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    contents = []
    for i in range(len(all_articles)):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        #url.append('/recommendation')
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)
        
        tech_articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)
        
        #print("requests.py-dan: ", *curr_content)
    #global curr_content
    #curr_content = desc
    #read_data()
    #with open("out.json", "w") as out_f:
    #    json.dump(list(contents), out_f)
    '''

    newsapi = NewsApiClient(api_key= Config.API_KEY)
    tech_articles = newsapi.get_top_headlines(category='technology')
    
    all_articles = tech_articles['articles']
    data_dict = {}

    for i in range(len(all_articles)):
        article = all_articles[i]
        
        data_dict['article_name'] = article['title']
        data_dict['article_description'] = article['description'] if article['description'] is not None else 'N\A'
        data_dict['article_image_path'] = article['urlToImage'] if article['urlToImage'] is not None else 'N\A'
        data_dict['link_to_article'] = article['url'] if article['url'] is not None else 'N\A'
        data_dict['article_category'] = 'technology'
        data_dict['article_author'] = article['author'] if article['author'] is not None else 'N\A'
        data_dict['article_publish_date'] = article['publishedAt'] if article['publishedAt'] is not None else 'N\A'

        Helpers.insert(table_name = 'articles', data = data_dict)
        data_dict = {}

    #Helpers.fill_recommendations()
    





    #------------------------------------------------------------------------------------------

    data = ''
    with open('out.json') as json_file:
        data = json.load(json_file)

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    contents = []

    titles_list = [ 'Develop your first Facebook messenger bot in PHP',
                    'IBM Wants to "Evolve the Internet" With Blockchain Technology',
                    'IEEE to Talk Blockchain at Cloud Computing Oxford-Con - CoinDesk',
                    'Banks Need To Collaborate With Bitcoin and Fintech Developers',
                    'What is the Best Cloud? Probably GCP',
                    'What Happens When You Combine Artificial Intelligence and Satellite Imagery',
                    'Your Docker Agenda for April',
                    'PostgreSQL Bloat: origins, monitoring and managing',
                    'Better together: New Microsoft integrations for easier collaboration',
                    'Build Zappos like faceted navigation with ElasticSearch']
    
    desc_list = ['(Credit: Independent.co.uk) Facebook recently announced a Bot platform for it is Messenger which provides businesses and individuals another way to communicate with people. What is a Chat bot? A computer program designed to simulate conversation with human users, especially over the Internet. Chat bot in PHP When I heard of it, my very first thought was to a bot in PHP. I started to find some SDK in this regard released by Facebook but none was present. I headed over to documentation which provided good information for starters. Ok! so without wasting further time, lets build our first Bot Timebot In order to create an Fb bot you will need two things to host your bot: A Facebook Page which will be like Home of Bot, People will visit the page, click on Message option to Interact with your bot. For example, suppose Pizza Hut introduce a bot for order related operations. What could they do that they integrate or host their bot on their official page, a fan can just click on Message button and send messages to order a Pizza, get new deals etc and they will get messages as if some human representatives is responding to them. It all depends how efficient a bot is.',
                'The Aite Group projects the blockchain market could be valued at $400 million by 2019. For that reason, some of the biggest names in banking, industry and technology have entered into the space to evaluate how this technology could change the financial world. IBM and Linux, for instance, have brought together some of the brightest minds in the industry and technology to work on blockchain technology through the Hyperledger Project. The Hyperledger Project is under the umbrella of the Linux Foundation, and seeks to incorporate findings by blockchain projects such as Blockstream, Ripple, Digital Asset Holdings and others in order to make blockchain technology useful for the world\'s biggest corporations. IBM has also contributed its own code to the project. According to John Wolpert, IBM\'s Global Blockchain Offering Director, when IBM and Linux began working together on the blockchain project, Linux made clear it wanted to "disrupt the disruption," in part with their findings, as well as the data gathered by projects such as Ripple, Ethereum and others exploring the blockchain. The Linux foundation announced its Hyperledger project on December 17, 2015. Just one day later, 2,300 companies had requested to join. The second-largest open source foundation in the history of open source had only 450 inquiries. "So, it\'s either going to be a holy mess or it\'s going to change the world," Wolpert said at The Blockchain Conference in San Francisco presented by Lighthouse Partners. As Wolford puts it, a team of IBMers is "on a quest" to understand and "do something important" with blockchain technology. "I don\'t know why we got this rap in the \'70s, way back, that we are not cool, that we\'re kind of stodgy, and that is not the IBM of my experience," Wolpert, who founded the taxi service Flywheel, explained. "We\'re the original crazy people.',
                'One of the largest and oldest organizations for computing professionals will kick off its annual conference on the future of mobile cloud computing tomorrow, where blockchain is scheduled to be one of the attractions. With more than 421,000 members in 260 countries, the Institute of Electrical and Electronics Engineers (IEEE) holding such a high-profile event has the potential to accelerate the rate of blockchain adoption by the engineering community. At the four-day conference, beginning Tuesday, the IEEE will host five blockchain seminars at the 702-year-old Exeter College of Oxford. The conference, IEEE Mobile Cloud 2016, is the organizations fourth annual event dedicated to mobile cloud computing services and engineering. Speaking at the event, hosted at Oxford University, professor Wei-Tek Tsai of the School of Computing, Informatics and Decision Systems engineering at Arizona State University will talk about the future of blockchain technology as an academic topic of research.',
                'It will take time until banks come around to the idea of embracing Bitcoin or Fintech, though. Banks need to innovate at an accelerated pace, yet are unable to do so on their own. Allowing third-party developers to work together with the bank through API access would be a significant step in the right direction, as there is valuable input to be gathered from the Bitcoin and Fintech industries. Banks and other established financial players have not taken a liking to Fintech and digital currency just yet, as they see both industries as major competitors to their offerings. While it is certainly true Bitcoin and Fintech can bring significant improvements to the table, they should be seen as complementary allies who will bring success to the banking industry. Or that is what the Monetary Authority of Singapore seems to be thinking, at least. Also read: Bitcoin Price Technical Analysis For 03/28/2016 - Looking To Buy BTC?',
                'In 2015 we migrated Quizlet from our legacy host to a large cloud provider. AWS is the default choice for most companies, but after comparing the options, we went with Google Cloud Platform (GCP). This is a summary of our analysis. Quizlet is now the ~50th biggest website in the U.S. in terms of traffic. Our technical infrastructure of 200 cloud machines supports 200,000 transactions a minute on an average day with significant shifts in traffic that depend on the school calendar. All those transactions are students learning on Quizlet and we have a responsibility to make sure that their experience is stable and performant. If Quizlet goes down it\'s like ripping a textbook out of students\' hands in the middle of class, so we make our cloud infrastructure and deployment a top priority. Outside of employee compensation, cloud spend is Quizlet\'s biggest expense. Even minor tweaks to our infrastructure can cost us tens of thousands of dollars a month.',
                'Facebook has a vested interest in helping the 4.2 billion people who still lack reliable Internet access find their way online. But when the social media company launched an effort in 2013 to provide connectivity to some of the world\'s most remote and disconnected regions, it immediately ran into a problem. Facebook knew these disconnected billions existed-just not precisely where in the world they were. So the Facebook Connectivity Lab team set out to find them. Using technology similar to what allows Facebook to recognize faces in photos uploaded to its service, the company sifted through more than 14 billion geospatial images captured by satellite imagery provider DigitalGlobe. The resulting maps reveal the locations of more than 2 billion disconnected people spread across 20 countries, many of them developing nations where even basic mapping data is scarce.',
                'Thank you Docker community for your amazing collaborations last month! In March, the community organized over 125 Docker Birthday #3 local trainings and celebrations . This month, you can still catch a few more birthday events and lots of other awesome Docker events! From webinars to workshops, meetups to conference talks, here is our list of Docker events coming up in April. Official Docker Training Courses View the full schedule of instructor led training courses here! Introduction to Docker This is a two-day, on-site or classroom-based training course which introduces you to the Docker platform and takes you through installing, integrating, and running it in your working environment. By the end of the course, you will be familiar with the "why" of Docker.',
                'In Robert M. Wysocki\'s latest Write Stuff article, he looks at the wider aspects of monitoring and managing the bloat in PostgreSQL. PostgreSQL\'s MVCC model provides excellent support for running multiple transactions operating on the same data set. One natural consequence of its design is the existence of so-called "database bloat". Judging by the amount of questions raised in the Internet it is quite a common problem and not many people seem to know, how to properly deal with it. I myself had the same issues and learnt one or two things that might be helpful, so in this article I\'d like to shed some light on this notion - why it\'s there in the first place, how it can affect performance and finally how to monitor and manage it. ',
                'When we partnered with Microsoft in 2014 , we had one goal in mind: to help you be more productive anywhere and on any device. Since then, we\'ve introduced integrations that let you edit Microsoft Office files stored in your Dropbox directly from the web or on your mobile device . And just last week, we released a brand new Dropbox app for Windows 10 . Today we\'re excited to mark the next phase of our partnership with the release of two new integrations with Microsoft products. "This announcement is just the next step in our journey to make Office files more accessible no matter where they\'re stored. We\'re excited that Dropbox customers now have the capabilities to co-edit files in Office Online. They can now also send documents directly from Dropbox within their Outlook.com account, allowing them to better collaborate regardless of their device or location."',
                'I\'ve been looking at different facets implementations while working on REST Search API for my ecommerce store. Some of the solutions I saw were simple to achieve (like plain faceting by terms with single selection), while others required some thinking and some extra work. Today we will talk about Zappos facets, since in my mind they do interesting things with products grouping (seems like they refer to it as sidebar). One of the key things about Zappos facets implementation is multi select within active bracket , which significantly improves and simplifies navigation experience for end customers.'
                ]
    
    img_list = ['https://capacity.com/wp-content/uploads/2019/08/chatbot-4071274_1920.jpg.webp',
                'https://www.gmex-group.com/wp-content/uploads/2019/09/IBM_blockchain.jpg',
                'https://cloudfront-us-east-1.images.arcpublishing.com/coindesk/LJA3TSWCKFGBPFTSGIPCSXHBHQ.jpg',
                'https://d3lkc3n5th01x7.cloudfront.net/wp-content/uploads/2020/09/29020725/hire-stellar-developer-2048x1153.jpg',
                'https://nordcloud.com/wp-content/uploads/2020/10/GCP-logo.png',
                'https://miro.medium.com/max/1400/1*QUUDupitw2Ms-b4g5NFFeQ.jpeg',
                'https://www.docker.com/sites/default/files/d8/styles/large/public/2021-08/Moby-share.png?itok=Kc8zKIm4',
                'https://webapp.io/content/images/size/w2000/2019/11/postgres.png',
                'https://cdn.vox-cdn.com/thumbor/yph6twMZwnafqlcy1LT20wgoYgY=/0x0:2040x1360/920x613/filters:focal(857x517:1183x843):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/70431477/DSCF1179.0.0.jpg',
                'https://miro.medium.com/max/1400/1*BmvPfSSm2G8C-khX1rhCGg.png']
    
    url_list = ['recommendation1.html',
                'recommendation2.html',
                'recommendation3.html',
                'recommendation4.html',
                'recommendation5.html',
                'recommendation6.html',
                'recommendation7.html',
                'recommendation8.html',
                'recommendation9.html',
                'recommendation10.html',
                ]
    i=0
    for curr_data in data:
        if i==10:
            break
        source.append(curr_data[0])
        title.append(titles_list[i])
        desc.append(desc_list[i])
        author.append(curr_data[3])
        img.append(img_list[i])
        p_date.append(curr_data[5])
        url.append(url_list[i])
        i+=1
    contents = zip(source, title, desc, author, img, p_date, url)
    return  contents


def entArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    ent_articles = newsapi.get_top_headlines(category='entertainment')

    all_articles = ent_articles['articles']

    ent_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(all_articles)):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        ent_articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)

    return  contents

def scienceArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    science_articles = newsapi.get_top_headlines(category='science')

    all_articles = science_articles['articles']

    science_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(all_articles)):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        science_articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)

    return  contents

def sportArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    sport_articles = newsapi.get_top_headlines(category='sports')

    all_articles = sport_articles['articles']

    sport_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(all_articles)):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        sport_articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)

    return  contents

def healthArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    health_articles = newsapi.get_top_headlines(category='health')

    all_articles = health_articles['articles']

    health_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(all_articles)):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])
        article_object = Articles(source, title, desc, author, img, p_date, url)

        health_articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)

    return  contents

def get_news_source():
  '''
  Function that gets the json response to our url request
  '''
  get_news_source_url = 'https://newsapi.org/v2/sources?apiKey=' + Config.API_KEY
  with urllib.request.urlopen(get_news_source_url) as url:
    get_news_source_data = url.read()
    
    get_news_source_response = json.loads(get_news_source_data)
    print(get_news_source_response, "...................")
    news_source_results = None

    if get_news_source_response['sources']:
      news_source_results_list = get_news_source_response['sources']
      news_source_results = process_sources(news_source_results_list)

  return news_source_results

def process_sources(source_list):
  '''
  function that process the news articles and transform them to a list of objects
  '''
  news_source_result = []
  for news_source_item in source_list:
    name = news_source_item.get('name')
    description = news_source_item.get('description')
    url = news_source_item.get('url')

    if name:
      news_source_object = Sources(name, description,url)
      news_source_result.append(news_source_object)
  return news_source_result