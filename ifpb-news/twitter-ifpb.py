import oauth2, json, pprint

class GetTwitterIFCZ():

    #@staticmethod
    def get_tweets(self):
        ConsumerKey = "PAhGdOl71p5zAmbZWetTXGno9"
        ConsumerSecret = "h9cOdbSEUnsekNNLK47ilex9o1yTdaas2nOjvUtKKrRARDS7yZ"
        AccessToken = "1123341102273187840-wU0vHHTdsMn6jvMvzMjgrETNwMykSu"
        AccessTokenSecret = "yQ5c3fx65agy8lE78Ct7qgbTCAQU3ZhR2fcOkK1CZmGVY"

        consumer = oauth2.Consumer(ConsumerKey, ConsumerSecret)
        toker = oauth2.Token(AccessToken, AccessTokenSecret)
        cliente = oauth2.Client(consumer, toker)


        r = cliente.request('https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=147705433')
        dec = r[1].decode()
        obj = json.loads(dec)

        for x in range(20):
            tweets = obj[x]['text']
            pprint.pprint(tweets)

if __name__=='__main__':
    tt_IFPB = GetTwitterIFCZ()
    tt_IFPB.get_tweets()
