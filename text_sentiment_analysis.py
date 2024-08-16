from textblob import TextBlob
text = "you are a bad person"
analysis = TextBlob(text)
sentiment = analysis.sentiment.polarity
if sentiment>0:
    print("positive sentiment")
elif sentiment<0:
    print("negative sentiment")
else:
    print("neutral sentiment")

