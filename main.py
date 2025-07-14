import tweepy
import requests
import os
import datetime

bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

respawnId = "207936757"


def authenticate_twitter_app(bearer_token):
    return tweepy.Client(bearer_token=bearer_token)

def sendMessage(message):
    DiscordWebHook = os.getenv("DISCORD_WEBHOOK_URL")
    if not DiscordWebHook:
        print("Error: Discord Webhook URL not found. Please set the DISCORD_WEBHOOK_URL environment variable.")
        return

    content_message = message
    try:
        response = requests.post(DiscordWebHook, json={"content": content_message})
        response.raise_for_status()
        print("Message sent successfully to Discord!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Discord: {e}")
        print(f"Response content: {response.text if 'response' in locals() else 'No response'}")

client = authenticate_twitter_app(bearer_token)


if datetime.datetime.now().weekday() == 5:
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)

else:
    yesterday = datetime.datetime.now() - datetime.timedelta(days=2)

tweets = client.get_users_tweets(respawnId, max_results=5, start_time=yesterday)

news = []

keywords = {"update", "patch", "release", "fix", "bug", "changes", "features"}

if tweets.data:
    for tweet in tweets.data:
        if any(keyword in tweet.text.lower() for keyword in keywords):
            news.append(tweet.text)
        

if news:
    sendMessage("\n\n--------------------------------------------\n\n".join(news))

