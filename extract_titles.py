############
#
# Extract Titles from RSS feed
#
# Implement get_headlines() function. It should take a url of an RSS feed
# and return a list of strings representing article titles.
#
############

from bs4 import BeautifulSoup
import requests

google_news_url="https://news.google.com/news/rss"
def get_headlines(rss_url: str) -> list[str]:
    
    """
        @returns a list of titles from the rss feed located at `rss_url`
    """
    response = requests.get(rss_url)
    
    # Parse the RSS feed content with BeautifulSoup
    soup = BeautifulSoup(response.text, features="xml")
    
    # Extract all titles from the RSS feed
    titles = [item.title.text for item in soup.find_all("item")]
    
    return titles
    
print(get_headlines(google_news_url))