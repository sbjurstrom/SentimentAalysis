#from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
from bs4 import BeautifulSoup
import urllib
import requests
from TwitterSearch import *
import csv

alchemyapi = AlchemyAPI()


####Dealership reiews from Cars.com#####

#Urls to be scraped
urls = ["http://www.cars.com/dealers/80802/longo-toyota/reviews/?count=50",
        "http://www.cars.com/dealers/24624/puente-hills-toyota/reviews/?count=100",
        "http://www.cars.com/dealers/24926/toyota-of-redlands/reviews/?count=50",
        "http://www.cars.com/dealers/1129/autonation-toyota-buena-park/reviews/?count=100",
        "http://www.cars.com/dealers/1124/toyota-scion-pasadena/reviews/"]

#Creating array to store sentiment info to be later written to file

count = 1
cEntArray =[]
cKeyArray = []
cSentArray = []
#for each url in list of urls, grab the html and look for the date, rating, and review
for url in urls:
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.text, 'html.parser')

    #finding the reviewers rating of the dealership and the text
    cReviews = [p.text for p in soup.findAll('p', attrs={'itemprop': 'description'})] 
    cRatings = [span.text for span in soup.findAll('span', attrs={'itemprop': 'ratingValue'})]
    cDates = [span1.text for span1 in soup.findAll('span', attrs={'itemprop': 'datePublished'})]

    #for each review discovered, find call AlchemyAPI and find entity score
    for review in range(len(cReviews)):

        cID = 'c' + str(count)
        
##        #Entity Analysis
##        response = alchemyapi.entities('text', cReviews[review], {'sentiment': 1})
##
##        if response['status'] == 'OK':
##            print('## Response Object ##')
##            print (json.dumps(response, indent =4))
##                     
##            for entity in response['entities']:
##                eText = (entity['text'].encode('utf-8'))
##                eType = entity['type']
##                eRelevance = entity['relevance']
##                eSentiment = entity['sentiment']['type']
##                if 'score' in entity['sentiment']:
##                    eSentimentScore = entity['sentiment']['score']
##                else:
##                    eSentimentScore = 'NA'
##
##                cEntRow = [cID, url.encode('utf-8'), cRatings[review+1], cDates[review],
##                    eText, eType, eRelevance, eSentiment, eSentimentScore]
##
##                cEntArray.append(cEntRow)
##
##        else:
##            print response['statusInfo']
        
##        #Keyword Analysis
##        response = alchemyapi.keywords('text', cReviews[review], {'sentiment': 1})
##
##        if response['status'] == 'OK':
##            for keyword in response['keywords']:
##                kText =  (keyword['text'].encode('utf-8'))
##                kRelevance = keyword['relevance']
##                kSentiment = keyword['sentiment']['type']
##                if 'score' in keyword['sentiment']:
##                    kSentimentScore =  keyword['sentiment']['score']
##                else:
##                    kSentimentScore = 0
##
##                cKeyRow = [cID, url.encode('utf-8'), cRatings[review+1], cDates[review],
##                    kText, kRelevance, kSentiment, kSentimentScore]
##
##                cKeyArray.append(cKeyRow)
##
##        else:
##            print('Error in keyword extaction call: ', response['statusInfo'])
##
##
##        #Sentiment Analysis
##        response = alchemyapi.sentiment('text', cReviews[review])
##
##        if response['status'] == 'OK':
##            sSentiment = response['docSentiment']['type']
##            if 'score' in response['docSentiment']:
##                sSentimentScore = response['docSentiment']['score']
##            else: sSentimentScore = 0
##        
##            cSentRow = [cID, url.encode('utf-8'), cRatings[review+1], cDates[review], sSentiment, sSentimentScore]
##
##            cSentArray.append(cSentRow)
##        else:
##            print('Error in sentiment analysis call: ', response['statusInfo'])
        
        
        print cID
        print '\n'        
        count += 1
    
##with open('cEntAnalysis.csv', 'a') as csvfile:
##    cWriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
##    cWriter.writerow(['Id','url','givenrating','date','entityText','entityType','entityRelevance','entitySentiment','entitySentimentScore'])
##    for row in range(len(cEntArray)):
##        cWriter.writerow(cEntArray[row]) 
##
##with open('cKeyAnalysis.csv', 'a') as csvfile:
##    cWriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
##    cWriter.writerow(['Id','url','givenrating','date','keywordText','keywordRelevance','keywordSentiment','keywordSentimentScore'])
##    for row in range(len(cKeyArray)):
##        cWriter.writerow(cKeyArray[row])     
##
##with open('cSentAnalysis.csv', 'a') as csvfile:
##    cWriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
##    cWriter.writerow(['Id','url','givenrating','date','sSentiment','sSentimentScore'])
##    for row in range(len(cSentArray)):
##        cWriter.writerow(cSentArray[row]) 
##
##
##


##
##
#######TWITTER SCRAPE##################
##tso = TwitterSearchOrder()
##tso.setKeywords(['toyota','buy',])
##tso.setLanguage('en')
##tso.setCount(10)
##
##
##ts = TwitterSearch(
##    consumer_key = 'cyhTYoAzQFaRX7uNPTaF92t1I',
##    consumer_secret = 'Sx2eH2e0AnlpSyIDhER2bJqtnzwvu3PFerb7wJ6pCa8QlsYyRX',
##    access_token = '2828888881-kcLAcSXo3CEGfjAtmxeNIec7XdhzmNptGEFmvmo',
##    access_token_secret = '4HVcNCDv03PixHYysOxr5N0RnIXUdpFeb8IqZOezCYH7J'
##    )
##
##count = 0
##for tweet in ts.searchTweetsIterable(tso):
##
##    tText = tweet['text']
##    tDate = tweet['created_at'].encode('utf-8')
###    try:
##    tGeo = tweet['geo']
##    tLoc = tweet['coordinates']
##    print tText
##    print tDate
##    print tweet['coordinates']
##    print tweet['geo']
##



####Yelp Scrape##################
urls = ["http://www.yelp.com/biz/puente-hills-toyota-city-of-industry-2",
        "http://www.yelp.com/biz/puente-hills-toyota-city-of-industry-2?start=40",
        "http://www.yelp.com/biz/puente-hills-toyota-city-of-industry-2?start=80",
        "http://www.yelp.com/biz/puente-hills-toyota-city-of-industry-2?start=120",
        "http://www.yelp.com/biz/longo-toyota-el-monte",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=40",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=80",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=120",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=160",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=200",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=240",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=280",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=320",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=360",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=400",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=440",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=480",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=520",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=560",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=600",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=640",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=680",
        "http://www.yelp.com/biz/longo-toyota-el-monte?start=720",
        "http://www.yelp.com/biz/toyota-of-redlands-redlands",
        "http://www.yelp.com/biz/toyota-of-redlands-redlands?start=40",
        "http://www.yelp.com/biz/autonation-toyota-buena-park-buena-park-2",
        "http://www.yelp.com/biz/autonation-toyota-buena-park-buena-park-2?start=40",
        "http://www.yelp.com/biz/autonation-toyota-buena-park-buena-park-2?start=80",
        "http://www.yelp.com/biz/autonation-toyota-buena-park-buena-park-2?start=120",
        "http://www.yelp.com/biz/toyota-pasadena-pasadena",
        "http://www.yelp.com/biz/toyota-pasadena-pasadena?start=40",
        "http://www.yelp.com/biz/toyota-pasadena-pasadena?start=80",
        "http://www.yelp.com/biz/toyota-pasadena-pasadena?start=120",
        "http://www.yelp.com/biz/toyota-pasadena-pasadena?start=160"]

yEntArray =[]
yKeyArray = []
ySentArray = []


ycount = 1
yID = 0
for url in urls:
    webpage = requests.get(url)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    yReviews = [p.text for p in soup.findAll('p', attrs={'class': 'review_comment ieSucks'})]
    yScores = soup.findAll(attrs= {'itemprop': 'ratingValue'})
    yDates = soup.findAll(attrs= {'itemprop': 'datePublished'})
    for review in range(len(yReviews)):
        yID = 'y' + str(ycount)
    ##    print "date:", date[t]['content'].encode('utf-8')
    ##    print "score: ", scores[t+1]['content'].encode('utf-8'), "/5"
    ##    print "review", reviews[t]
        print yID

        
        #Entity Analysis
        response = alchemyapi.entities('text', yReviews[review], {'sentiment': 1})

        if response['status'] == 'OK':
            print('## Response Object ##')
            print (json.dumps(response, indent =4))
                     
            for entity in response['entities']:
                eText = (entity['text'].encode('utf-8'))
                eType = entity['type']
                eRelevance = entity['relevance']
                eSentiment = entity['sentiment']['type']
                if 'score' in entity['sentiment']:
                    eSentimentScore = entity['sentiment']['score']
                else:
                    eSentimentScore = 'NA'

                yEntRow = [yID, url.encode('utf-8'), yScores[review+1]['content'], yDates[review]['content'],
                    eText, eType, eRelevance, eSentiment, eSentimentScore]

                yEntArray.append(yEntRow)

        else:
            print response['statusInfo']
        
##        #Keyword Analysis
##        response = alchemyapi.keywords('text', yReviews[review], {'sentiment': 1})
##
##        if response['status'] == 'OK':
##            for keyword in response['keywords']:
##                kText =  (keyword['text'].encode('utf-8'))
##                kRelevance = keyword['relevance']
##                kSentiment = keyword['sentiment']['type']
##                if 'score' in keyword['sentiment']:
##                    kSentimentScore =  keyword['sentiment']['score']
##                else:
##                    kSentimentScore = 0
##
##                yKeyRow = [yID, url.encode('utf-8'), yScores[review+1]['content'], yDates[review]['content'],
##                    kText, kRelevance, kSentiment, kSentimentScore]
##
##
##                yKeyArray.append(yKeyRow)
##
##        else:
##            print('Error in keyword extaction call: ', response['statusInfo'])
##
##
##        #Sentiment Analysis
##        response = alchemyapi.sentiment('text', yReviews[review])
##
##        if response['status'] == 'OK':
##            sSentiment = response['docSentiment']['type']
##            if 'score' in response['docSentiment']:
##                sSentimentScore = response['docSentiment']['score']
##            else: sSentimentScore = 0
##        
##            ySentRow = [yID, url.encode('utf-8'), yScores[review+1]['content'], yDates[review]['content'], sSentiment, sSentimentScore]
##
##            ySentArray.append(ySentRow)
##        else:
##            print('Error in sentiment analysis call: ', response['statusInfo'])
##        
##        

        ycount += 1


        
    
with open('cEntAnalysis.csv', 'a') as csvfile:
    cWriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    cWriter.writerow(['Id','url','givenrating','date','entityText','entityType','entityRelevance','entitySentiment','entitySentimentScore'])
    for row in range(len(cEntArray)):
        cWriter.writerow(cEntArray[row]) 

##with open('cKeyAnalysis.csv', 'a') as csvfile:
##    cWriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
##    cWriter.writerow(['Id','url','givenrating','date','keywordText','keywordRelevance','keywordSentiment','keywordSentimentScore'])
##    for row in range(len(cKeyArray)):
##        cWriter.writerow(cKeyArray[row])     
##
##with open('cSentAnalysis.csv', 'a') as csvfile:
##    cWriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
##    cWriter.writerow(['Id','url','givenrating','date','sSentiment','sSentimentScore'])
##    for row in range(len(cSentArray)):
##        cWriter.writerow(cSentArray[row]) 




    

