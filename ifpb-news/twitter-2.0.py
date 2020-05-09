import twitter


class GetTwitterIFCZ():

    @staticmethod
    def get_tweets():
        api = twitter.Api(consumer_key="PAhGdOl71p5zAmbZWetTXGno9",
                          consumer_secret="h9cOdbSEUnsekNNLK47ilex9o1yTdaas2nOjvUtKKrRARDS7yZ",
                          access_token_key="1123341102273187840-wU0vHHTdsMn6jvMvzMjgrETNwMykSu",
                          access_token_secret="yQ5c3fx65agy8lE78Ct7qgbTCAQU3ZhR2fcOkK1CZmGVY",
                          tweet_mode="extended")

        statuses = api.GetUserTimeline(147705433)
        return statuses


if __name__ == '__main__':
    tt_IFPB = GetTwitterIFCZ()
    for x in tt_IFPB.get_tweets():
        print('-' * 10)
        print(x.full_text)
