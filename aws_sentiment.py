import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

text = "It is raining today in Seattle"

print('Calling DetectSentiment')
response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
print(json.dumps(response, sort_keys=True, indent=4))
sentiment = response['Sentiment']
sentiment_mixed = response['SentimentScore']['Mixed']
sentiment_negative = response['SentimentScore']['Negative']
sentiment_neutral = response['SentimentScore']['Neutral']
sentiment_positive = response['SentimentScore']['Positive']
print(sentiment, sentiment_mixed, sentiment_negative, sentiment_neutral, sentiment_positive)
print('End of DetectSentiment\n')

"""
{
    "ResponseMetadata": {
        "HTTPHeaders": {
            "connection": "keep-alive",
            "content-length": "164",
            "content-type": "application/x-amz-json-1.1",
            "date": "Sun, 15 Apr 2018 21:08:31 GMT",
            "x-amzn-requestid": "269fc140-40f1-11e8-8df2-9de8e1b73d46"
        },
        "HTTPStatusCode": 200,
        "RequestId": "269fc140-40f1-11e8-8df2-9de8e1b73d46",
        "RetryAttempts": 0
    },
    "Sentiment": "NEUTRAL",
    "SentimentScore": {
        "Mixed": 0.002063251566141844,
        "Negative": 0.013271247036755085,
        "Neutral": 0.9274052977561951,
        "Positive": 0.057260122150182724
    }
}

"""