import twitter
api = twitter.Api(consumer_key = '7Q0PgkxAofe50HgrprWaLkjFE',
                    consumer_secret = 'IwVC9R84wPlp2PtukOUA2xPc2HZsmSmIjRXnCuRFqdz3ADfCpu',
                    access_token_key = 	'911322553-fEKIEXJYVqPVR458fT9uWSWTRn86XxIDhyFDLgqe',
                    access_token_secret = 'htyXX12Z0ON1p3VaBDjB9lSwXye0Pr4ZJcdIMkyEFKnTN')
status = api.PostUpdate('#wherearenatesfish')
print(status.text)
api.PostMedia('Here is my Fish','./f.gif')
