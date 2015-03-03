# Get old tweets using search
import json
import tweepy

## User credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

## API parameters
max_tw = 2000
myco = 200

## Search parameters
myq = "#TheDress"

## Time periods (Fri 27th Feb, GMT)
id_00 = "571097386749181952"
id_10 = "571248382217359361"
id_11 = "571263482773024768"
id_12 = "571278580640043008"
id_13 = "571293682428727297"
id_19 = "571384277386043392"
id_20 = "571399379321552896"
id_21 = "571414476366467074"
id_22 = "571429579136606208"
id_23 = "571444676500320256"
id_24 = "571459774522494976"

## Locations
#myg = "51.5072,0.1275,200km" #London+200km, UK
myg = "53.4000,3.0000,500km" #Liverpool+500km, UK
#myg = "-90.0000,0.0000,3000km" #Antarctica

## SEARCH ##
#twits = api.search(q=myq, count=myco, since_id=id_st, max_id=id_end, lang="en")
twits = [status for status in tweepy.Cursor(api.search, q=myq, lang='en', geocode=myg, count=myco, since_id=id_19, max_id=id_20).items(max_tw)]

print len(twits)

for index in range(len(twits)):
	print json.dumps(twits[index]._json)
	print