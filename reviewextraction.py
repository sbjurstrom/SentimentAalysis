
import json
from bs4 import BeautifulSoup
import urllib
import requests
from TwitterSearch import *
import csv

####Dealership reiews from Cars.com#####

#Urls to be scraped
urls = ["http://www.cars.com/dealers/80802/longo-toyota/reviews/?count=50",
        "http://www.cars.com/dealers/24624/puente-hills-toyota/reviews/?count=100",
        "http://www.cars.com/dealers/24926/toyota-of-redlands/reviews/?count=50",
        "http://www.cars.com/dealers/1129/autonation-toyota-buena-park/reviews/?count=100",
        "http://www.cars.com/dealers/1124/toyota-scion-pasadena/reviews/"]

#Creating array to store sentiment info to be later written to file

count = 1
cArray =[]
tArray = []
yArray = []
cGeo = 0
cLoc = 0

###for each url in list of urls, grab the html and look for the date, rating, and review
##
##for url in urls:
##    webpage = requests.get(url)
##    soup = BeautifulSoup(webpage.text, 'html.parser')
##
##    #finding the reviewers rating of the dealership and the text
##    cReviews = [p.text for p in soup.findAll('p', attrs={'itemprop': 'description'})] 
##    cRatings = [span.text for span in soup.findAll('span', attrs={'itemprop': 'ratingValue'})]
##    cDates = [span1.text for span1 in soup.findAll('span', attrs={'itemprop': 'datePublished'})]
##
##    #for each review discovered, find call AlchemyAPI and find entity score
##    for review in range(len(cReviews)):
##
##        cID = 'c' + str(count)
##        
##
##        cRow = [cID, url.encode('utf-8'), cRatings[review+1], cDates[review],cReviews[review].encode('utf-8'), cGeo, cLoc]
##        print cID
##        cArray.append(cRow)
##        
##        count += 1
##    
##with open('spssanalysis.csv', 'a') as csvfile:
##    cWriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
##    cWriter.writerow(['Id','url','givenrating','date','review', 'geo', 'loc'])
##    for row in range(len(cArray)):
##        cWriter.writerow(cArray[row]) 
##
##
##
##
##
######Yelp Scrape##################
##urls = ["http://www.yelp.com/biz/puente-hills-toyota-city-of-industry-2",
##        "http://www.yelp.com/biz/puente-hills-toyota-city-of-industry-2?start=40",
##        "http://www.yelp.com/biz/puente-hills-toyota-city-of-industry-2?start=80",
##        "http://www.yelp.com/biz/puente-hills-toyota-city-of-industry-2?start=120",
##        "http://www.yelp.com/biz/longo-toyota-el-monte",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=40",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=80",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=120",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=160",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=200",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=240",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=280",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=320",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=360",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=400",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=440",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=480",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=520",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=560",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=600",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=640",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=680",
##        "http://www.yelp.com/biz/longo-toyota-el-monte?start=720",
##        "http://www.yelp.com/biz/toyota-of-redlands-redlands",
##        "http://www.yelp.com/biz/toyota-of-redlands-redlands?start=40",
##        "http://www.yelp.com/biz/autonation-toyota-buena-park-buena-park-2",
##        "http://www.yelp.com/biz/autonation-toyota-buena-park-buena-park-2?start=40",
##        "http://www.yelp.com/biz/autonation-toyota-buena-park-buena-park-2?start=80",
##        "http://www.yelp.com/biz/autonation-toyota-buena-park-buena-park-2?start=120",
##        "http://www.yelp.com/biz/toyota-pasadena-pasadena",
##        "http://www.yelp.com/biz/toyota-pasadena-pasadena?start=40",
##        "http://www.yelp.com/biz/toyota-pasadena-pasadena?start=80",
##        "http://www.yelp.com/biz/toyota-pasadena-pasadena?start=120",
##        "http://www.yelp.com/biz/toyota-pasadena-pasadena?start=160"]
##
##ycount = 1
##yID = 0
##for url in urls:
##    webpage = requests.get(url)
##
##    soup = BeautifulSoup(webpage.text, 'html.parser')
##
##    yReviews = [p.text for p in soup.findAll('p', attrs={'class': 'review_comment ieSucks'})]
##    yScores = soup.findAll(attrs= {'itemprop': 'ratingValue'})
##    yDates = soup.findAll(attrs= {'itemprop': 'datePublished'})
##    for review in range(len(yReviews)):
##        yID = 'y' + str(ycount)
##    ##    print "date:", date[t]['content'].encode('utf-8')
##    ##    print "score: ", scores[t+1]['content'].encode('utf-8'), "/5"
##    ##    print "review", reviews[t]
##        print yID
##        yRow = [yID, url.encode('utf-8'), yScores[review+1]['content'].encode('utf-8'), yDates[review]['content'].encode('utf-8'), yReviews[review].encode('utf-8'), cGeo, cLoc]
##        yArray.append(yRow)
##        ycount += 1
##
##
##
##
##
##with open('spssanalysis.csv', 'a') as csvfile:
##    cWriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
##    for row in range(len(yArray)):
##        cWriter.writerow(yArray[row]) 
##
##
##



###TWITTER SCRAPE##################
tso = TwitterSearchOrder()
tso.setKeywords(['toyota','buy',])
tso.setLanguage('en')
tcount = 1
tRating = 0
tURL = 'tweet'
ts = TwitterSearch(
    consumer_key = 'cyhTYoAzQFaRX7uNPTaF92t1I',
    consumer_secret = 'Sx2eH2e0AnlpSyIDhER2bJqtnzwvu3PFerb7wJ6pCa8QlsYyRX',
    access_token = '2828888881-kcLAcSXo3CEGfjAtmxeNIec7XdhzmNptGEFmvmo',
    access_token_secret = '4HVcNCDv03PixHYysOxr5N0RnIXUdpFeb8IqZOezCYH7J'
    )

tcount = 1
for tweet in ts.searchTweetsIterable(tso):

    tID = 't' + str(tcount)
    tText = tweet['text'].encode('utf-8')
    tDate = tweet['created_at'].encode('utf-8')
    print tID
    tRow = tID, tURL, tRating,tDate, tText, cGeo, cLoc
    tArray.append(tRow)
    tcount += 1

with open('spssanalysis.csv', 'a') as csvfile:
    cWriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    for row in range(len(tArray)):
        cWriter.writerow(tArray[row]) 

    

