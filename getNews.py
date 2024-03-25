# pip install GoogleNews
# https://pypi.org/project/GoogleNews/

from GoogleNews import GoogleNews


googlenews = GoogleNews(lang='en', region='US')
googlenews.get_news('APPLE')
googlenews.results()

