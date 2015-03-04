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
id_05 = "571172886045712384"
id_10 = "571248382217359361"
id_11 = "571263482773024768"
id_12 = "571278580640043008"
id_13 = "571293682428727297"
id_14 = "571308779775660032"
id_15 = "571323881576898560"
id_16 = "571338978680553472"
id_17 = "571354080192421889"
id_18 = "571369180945113090"
id_19 = "571384277386043392"
id_20 = "571399379321552896"
id_21 = "571414476366467074"
id_22 = "571429579136606208"
id_23 = "571444676500320256"
id_24 = "571459774522494976"
#(Sat 28th Feb, GMT)
id_s00 = "571459774522494976"
id_s01 = "571474875879186433"
id_s02 = "571489974027202560"
id_s03 = "571505073991385088"
id_s04 = "571520173359955968"
id_s05 = "571535275060531200"

## Locations
#myg = "51.5072,-0.1275,200km" #London+200km, UK
#myg = "53.4000,-3.0000,500km" #Liverpool+500km, UK
myg = "40.4397,-79.9764,800km" #Pittsburgh+800km, US East Coast (NYC/Chic)
#myg = "-90.0000,0.0000,3000km" #Antarctica

## SEARCH ##
#twits = api.search(q=myq, count=myco, since_id=id_st, max_id=id_end, lang="en")
twits = [status for status in tweepy.Cursor(api.search, q=myq, lang='en', geocode=myg, count=myco, since_id=id_19, max_id=id_20).items(max_tw)]

print len(twits)

for index in range(len(twits)):
	print json.dumps(twits[index]._json)
	print