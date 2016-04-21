#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2310389120-fIH9Fk24O3RZMf83rFrfWjsoqfaUsF58B8rzu3u"
access_token_secret = "qqPfb0kbLpL2BTLwx8LSRWPPVgHDZoAA86UELFgniYqyu"
consumer_key = "vUEWGUlq6WzHurUY29HacNntP"
consumer_secret = "zylDnntX7QzpPwAEJZxaaGsks1yfI8NKJPTDhz8ExrqhbUjswm"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])


"""Consumer Key (API Key)  vUEWGUlq6WzHurUY29HacNntP
Consumer Secret (API Secret)    zylDnntX7QzpPwAEJZxaaGsks1yfI8NKJPTDhz8ExrqhbUjswm
Access Token    2310389120-fIH9Fk24O3RZMf83rFrfWjsoqfaUsF58B8rzu3u
Access Token Secret qqPfb0kbLpL2BTLwx8LSRWPPVgHDZoAA86UELFgniYqyu"""
