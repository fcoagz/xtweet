from cachetools import TTLCache
from xtweet.request import get_from_cache_or_api

class Tweet(object):
    def __init__(self, url: str, ttl=300, maxsize=1024) -> None:
        """
        Inicializa un objeto Tweet a partir de la URL de un tweet.

        Args:
            url (str): URL del tweet.
        """
        self.cache = TTLCache(maxsize, ttl)
        url = url.split('/')
        self.path = '/' + '/'.join(url[3:])
        self._tuit_info = None

    @property
    def tuit_info(self):
        if self._tuit_info is None:
            self._tuit_info = get_from_cache_or_api(self.cache, f"tuit_{self.path}", "https://api.vxtwitter.com" + self.path)
        return self._tuit_info
    
    @property
    def date(self):
        return self.tuit_info['date']
    
    @property
    def text(self):
        return self.tuit_info['text']

    @property
    def thumbnail_url(self):
        is_thumbnail = 'media_extended' in self.tuit_info and len(self.tuit_info['media_extended']) > 0

        if is_thumbnail:
            return self.tuit_info["media_extended"][0]["thumbnail_url"]
        return None
    
    @property
    def likes(self):
        return self.tuit_info['likes']

    @property
    def replies(self):
        return self.tuit_info['replies']
    
    @property
    def retweets(self):
        return self.tuit_info['retweets']
    
    @property
    def tweet_id(self):
        return self.tuit_info['tweetID']

    @property
    def user_name(self):
        return self.tuit_info['user_name']
    
    @property
    def user_name(self):
        return self.tuit_info['user_screen_name']