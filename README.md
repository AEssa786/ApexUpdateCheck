# 🎮 Apex Legends Update Tracker
# 📖 Description
This app was created to notify me when there's an update available for the game Apex Legends, including a brief description of what the update includes.

It works by using the X (Twitter) API v2 along with Tweepy, a Python library that simplifies working with the API. The app fetches tweets from the official X account of the game's development company and scans them for keywords like "update" or "fix". Relevant tweets are then forwarded to a Discord server via webhook.

The program is scheduled to run automatically four times a week using a GitHub Actions workflow.

# 🛠 Tech Stack
-Python 3.12

-Tweepy 4.16.0

-X API v2

-GitHub Actions

# 🚀 How to Use
This program is open for anyone to use and easy to configure:

-Clone or download the project files.

-Open the code file and replace:

-YOUR_BEARER_TOKEN with your own X API bearer token

-YOUR_DISCORD_WEBHOOK_URL with your Discord webhook URL

-Push to a GitHub repository (if you want GitHub Actions to run it automatically).

-You’re good to go! The app will post relevant update tweets to your Discord server.

# 📌 Notes
Make sure your bearer token has appropriate access under the X API Free or Basic tier.

Avoid exceeding rate limits: the app runs infrequently to stay within the Free tier limits, which only allows 1 request every 15 minutes and up to 100 tweets pulled per month.
