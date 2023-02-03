import tweepy

# Consumer keys and access tokens, used for OAuth
access_tokens = "1220826728790142976-zmxiSLYqeWfYxiRioWazr1qx3c40Vj"
access_tokens_secret = "gsVtkOSjwpcpn4kskzLY5acgAT3F7pCz39eyCSndwKniy"
bearer = "AAAAAAAAAAAAAAAAAAAAANN5lgEAAAAAXvm5%2BgOCRb3UKd7VUE%2Bew6SOhI4%3D6Ch06uzOZyRsY4w9hOHNJHjYFTFmiYOO8h0r2YXRFJp1xmWjp3"

# access tokens, used for OAuth
auth = tweepy.OAuth2BearerHandler(bearer)
api = tweepy.API(auth)

topic = "SNCF"

# fetch tweets about topic SNCF in french using cursor and search_tweets
tweets = tweepy.Cursor(api.search_tweets, q=topic, lang="fr").items(1000)



if __name__ == "__main__":
    print("Number of tweets about SNCF: {}".format(len(tweets)))

