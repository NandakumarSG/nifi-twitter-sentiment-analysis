from nltk.sentiment.vader import SentimentIntensityAnalyzer
import mysql.connector
import sys
import os

cnx = mysql.connector.connect(user='root', password='family',host='127.0.0.1',database='sonoo')
cursor = cnx.cursor()


analyser = SentimentIntensityAnalyzer()
x=sys.argv[1]
snt = analyser.polarity_scores(x)

add_tweet= ("INSERT INTO analysis " "(tweet, negative, neutral, positive, compound) " "VALUES(%s, %s, %s, %s, %s);")

data_sentiment = (str(x), str(snt['neg']), str(snt['neu']), str(snt['pos']), str(snt['compound']))
cursor.execute(add_tweet, data_sentiment)
cnx.commit()
cursor.close()
cnx.close()
