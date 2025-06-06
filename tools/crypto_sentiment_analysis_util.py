
import os
from dotenv import load_dotenv
from transformers import pipeline
import os
import pandas as pd
from GoogleNews import GoogleNews
from langchain_openai import ChatOpenAI
import pandas as pd
import praw
from datetime import datetime

load_dotenv()

def fetch_news(stockticker):
    
    """ Fetches news articles for a given stock symbol within a specified date range.

    Args:
    - stockticker (str): Symbol of a particular stock
    
    Returns:
    - list: A list of dictionaries containing stock news. """
    
    load_dotenv()
    days_to_fetch_news = os.environ["DAYS_TO_FETCH_NEWS"]

    googlenews = GoogleNews()
    googlenews.set_period(days_to_fetch_news)
    googlenews.get_news(stockticker)
    news_json=googlenews.get_texts()
    urls=googlenews.get_links()
    
    no_of_news_articles_to_fetch = os.environ["NO_OF_NEWS_ARTICLES_TO_FETCH"]
    news_article_list = []
    counter = 0
    for article in news_json:
        
        if(counter >= int(no_of_news_articles_to_fetch)):
            break

        relevant_info = {
            'News_Article': article,
            'URL': urls[counter]
        }
        news_article_list.append(relevant_info)
        counter+=1
    return news_article_list

def fetch_reddit_news(cryptocurrencyticker):
    load_dotenv()
    REDDIT_USER_AGENT= os.environ["REDDIT_USER_AGENT"]
    REDDIT_CLIENT_ID= os.environ["REDDIT_CLIENT_ID"]
    REDDIT_CLIENT_SECRET= os.environ["REDDIT_CLIENT_SECRET"]
    #https://medium.com/geekculture/a-complete-guide-to-web-scraping-reddit-with-python-16e292317a52
    user_agent = REDDIT_USER_AGENT
    reddit = praw.Reddit (
    client_id= REDDIT_CLIENT_ID,
    client_secret= REDDIT_CLIENT_SECRET,
    user_agent=user_agent
    )

    headlines = set ( )
    for submission in reddit.subreddit('CryptoCurrencyTrading').search(cryptocurrencyticker,time_filter='week'):
        headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    
    if len(headlines)<10:
        for submission in reddit.subreddit('CryptoCurrencyTrading').search(cryptocurrencyticker,time_filter='year'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    if len(headlines)<10:
        for submission in reddit.subreddit('CryptoCurrencyTrading').search(cryptocurrencyticker): #,time_filter='week'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)

# coinbase
    for submission in reddit.subreddit('CoinBase').search(cryptocurrencyticker,time_filter='week'):
        headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    
    if len(headlines)<10:
        for submission in reddit.subreddit('CoinBase').search(cryptocurrencyticker,time_filter='year'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    if len(headlines)<10:
        for submission in reddit.subreddit('CoinBase').search(cryptocurrencyticker): #,time_filter='week'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)

# coingecko
    for submission in reddit.subreddit('coingecko').search(cryptocurrencyticker,time_filter='week'):
        headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    
    if len(headlines)<10:
        for submission in reddit.subreddit('coingecko').search(cryptocurrencyticker,time_filter='year'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    if len(headlines)<10:
        for submission in reddit.subreddit('coingecko').search(cryptocurrencyticker): #,time_filter='week'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)

# crypto
    for submission in reddit.subreddit('CryptoCurrency').search(cryptocurrencyticker,time_filter='week'):
        headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    
    if len(headlines)<10:
        for submission in reddit.subreddit('CryptoCurrency').search(cryptocurrencyticker,time_filter='year'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    if len(headlines)<10:
        for submission in reddit.subreddit('CryptoCurrency').search(cryptocurrencyticker): #,time_filter='week'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)

# shitcoin
    for submission in reddit.subreddit('ShitcoinCentral').search(cryptocurrencyticker,time_filter='week'):
        headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    
    if len(headlines)<10:
        for submission in reddit.subreddit('ShitcoinCentral').search(cryptocurrencyticker,time_filter='year'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    if len(headlines)<10:
        for submission in reddit.subreddit('ShitcoinCentral').search(cryptocurrencyticker): #,time_filter='week'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)

# shitcoin
    for submission in reddit.subreddit('shitcoinmoonshots').search(cryptocurrencyticker,time_filter='week'):
        headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    
    if len(headlines)<10:
        for submission in reddit.subreddit('shitcoinmoonshots').search(cryptocurrencyticker,time_filter='year'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    if len(headlines)<10:
        for submission in reddit.subreddit('shitcoinmoonshots').search(cryptocurrencyticker): #,time_filter='week'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)

# solana
    for submission in reddit.subreddit('solana').search(cryptocurrencyticker,time_filter='week'):
        headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    
    if len(headlines)<10:
        for submission in reddit.subreddit('solana').search(cryptocurrencyticker,time_filter='year'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)
    if len(headlines)<10:
        for submission in reddit.subreddit('solana').search(cryptocurrencyticker): #,time_filter='week'):
            headlines.add(submission.title + ', Date: ' +datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S') + ', URL:' +submission.url)

    return headlines

def analyze_sentiment(article):
    """
    Analyzes the sentiment of a given news article.

    Args:
    - news_article (dict): Dictionary containing 'summary', 'headline', and 'created_at' keys.

    Returns:
    - dict: A dictionary containing sentiment analysis results.
    """

    #Analyze sentiment using default model
    #classifier = pipeline('sentiment-analysis')

    #Analyze sentiment using specific model
    classifier = pipeline(model='mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis')
    sentiment_result = classifier(str(article))

    analysis_result = {
        'News_Article': article,
        'Sentiment': sentiment_result
    }

    return analysis_result


def generate_summary_of_sentiment(sentiment_analysis_results):
    
    
    news_article_sentiment = str(sentiment_analysis_results)
    print("News article sentiment : " + news_article_sentiment)
    

    os.environ["OPENAI_API_KEY"] = os.environ["OPENAI_API_KEY"]
    model = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
        # base_url="...",
        # organization="...",
        # other params...
    )

    messages=[
            {"role": "system", "content": "You are a helpful assistant that looks at all news articles with their sentiment, hyperlink and date in front of the article text, the articles MUST be ordered by date!, and generate a summary rationalizing dominant sentiment. At the end of the summary, add URL links with dates for all the articles in the markdown format for streamlit. Make sure the articles as well as the links are ordered descending by Date!!!!!!! Example of adding the URLs: The Check out the links: [link](%s) % url, 2024-03-01. "},
            {"role": "user", "content": f"News articles and their sentiments: {news_article_sentiment}"}
    ]
    response = model.invoke(messages)
    

    summary = response.content
    print ("+++++++++++++++++++++++++++++++++++++++++++++++")
    print(summary)
    print ("+++++++++++++++++++++++++++++++++++++++++++++++")
    return summary


def plot_sentiment_graph(sentiment_analysis_results):
    """
    Plots a sentiment analysis graph 

    Args:
    - sentiment_analysis_result): (dict): Dictionary containing 'Review Title : Summary', 'Rating', and 'Sentiment' keys.

    Returns:
    - dict: A dictionary containing sentiment analysis results.
    """
    df = pd.DataFrame(sentiment_analysis_results)
    print(df)

    #Group by Rating, sentiment value count
    grouped = df['Sentiment'].value_counts()

    sentiment_counts = df['Sentiment'].value_counts()

    # Plotting pie chart
    # fig = plt.figure(figsize=(5, 3))
    # plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    # plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    #Open below when u running this program locally and c
    #plt.show()

    return sentiment_counts


def get_dominant_sentiment (sentiment_analysis_results):
    """
    Returns overall sentiment, negative or positive or neutral depending on the count of negative sentiment vs positive sentiment 

    Args:
    - sentiment_analysis_result): (dict): Dictionary containing 'summary', 'headline', and 'created_at' keys.

    Returns:
    - dict: A dictionary containing sentiment analysis results.
    """
    df = pd.DataFrame(sentiment_analysis_results)

    # Group by the 'sentiment' column and count the occurrences of each sentiment value
    sentiment_counts = df['Sentiment'].value_counts().reset_index()
    sentiment_counts.columns = ['sentiment', 'count']
    print(sentiment_counts)

    # Find the sentiment with the highest count
    dominant_sentiment = sentiment_counts.loc[sentiment_counts['count'].idxmax()]

    return dominant_sentiment['sentiment']

#starting point of the program
if __name__ == '__main__':
    
    #fetch stock news
    news_articles = fetch_news('AAPL')

    analysis_results = []
    
    #Perform sentiment analysis for each product review
    for article in news_articles:
        sentiment_analysis_result = analyze_sentiment(article['News_Article'])

        # Display sentiment analysis results
        print(f'News Article: {sentiment_analysis_result["News_Article"]} : Sentiment: {sentiment_analysis_result["Sentiment"]}', '\n')

        result = {
                    'News_Article': sentiment_analysis_result["News_Article"],
                    'Sentiment': sentiment_analysis_result["Sentiment"][0]['label']
                }
        
        analysis_results.append(result)

    
    #Graph dominant sentiment based on sentiment analysis data of reviews
    dominant_sentiment = get_dominant_sentiment(analysis_results)
    print(dominant_sentiment)
    
    #Plot graph
    plot_sentiment_graph(analysis_results)

