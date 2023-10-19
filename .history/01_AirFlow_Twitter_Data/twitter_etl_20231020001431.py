import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv
load_dotenv()


# consumer = os.getenv("Bearer Token")
client = tweepy.Client(bearer_token='Bearer_Token')
# access_key = os.getenv("API_Key")
# access_secret = os.getenv("API_Key_Secret")
# consumer_key = os.getenv("Access_Token")
# consumer_secret = os.getenv("Access_Token_Secret")

# # Twitter Authentication
# auth = tweepy.OAuthHandler(access_key, access_secret)
# auth.set_access_token(consumer_key, consumer_secret)

# # Create an API object
# api = tweepy.API(auth)

# tweets = api.user_timeline(screen_name="@elonmusk", 
#                            count=20, 
#                            include_rts=False,
#                            tweet_mode="extended")

# print(tweets)   


Skip to content
DEV Community
Search...

Create Post


12
Jump to Comments
33
Save

TwitterDev profile imageSuhem Parack
Suhem Parack for TwitterDev
Posted on Sep 29, 2021 • Updated on Feb 3, 2022


34

5
A comprehensive guide for using the Twitter API v2 with Tweepy in Python
#
twitter
#
api
#
python
Tweepy is a popular package in Python used by students, researchers and developers for interacting with the Twitter API. Recently, the version 4.0 of this package was released that supports the Twitter API v2 and the academic research product track. In this guide, we will learn how to use the various functionality available in the Twitter API v2, using Tweepy.

Note: At the time of writing this guide, the streaming endpoints in the Twitter API v2 (such as filtered stream and sampled stream) are not supported yet in Tweepy, but will be added in the future.

The complete documentation for Tweepy can be found here

Prerequisite
In order to work with the Twitter API, you need to have a developer account and your API keys and tokens to connect to the API. Learn more on how to obtain these keys and tokens here.

In order to work with Tweepy, make sure you have Python installed on your machine. Then, in the terminal run:
pip3 install tweepy
Note: If you already have Tweepy installed, you can upgrade it to the latest version i.e. 4.0 by running:
pip3 install tweepy --upgrade
For all the examples in this section, you will first need to import the tweepy library, then you will need to initialize the client by passing it your bearer token. Once you have the client initialized, you will be ready to start using the various functions in this library.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')
1. Searching for Tweets from the last 7 days
In order to search Tweets from the last 7 days, you can use the search_recent_tweets function available in Tweepy. You will have to pass it a search query to specify the data that you are looking for. In the example below, we are searching for Tweets from the last days from the Twitter handle suhemparack and we are excluding retweets using -is:retweet.

By default, in your response, you will only get the Tweet ID and Tweet text for each Tweet. If you need additional Tweet fields such as context_annotations, created_at (the time the tweet was created) etc., you can specifiy those fields using the tweet_fields parameter, as shown in the example below. Learn more about available fields here. By default, a request returns 10 Tweets. If you want more than 10 Tweets per request, you can specify that using the max_results parameter. The maximum Tweets per request is 100.

Note: Not all Tweets have context_annotations associated with them, which is why, in the sample below, we only print the context_annotations if those are available for a Tweet.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)
2. Searching for Tweets from the full-archive of public Tweets
If you have access to the academic research product track, you can get Tweets older than 7 days i.e. from the full archive of publicly available Tweets. In order to get these Tweets, make sure to use the bearer token from an app connected to your academic project in the Twitter developer portal. You can use the search_all_tweets method and pass it the search query. As shown in the example above, you can also specify additional Tweet fields etc. that you'd like returned for your request to the Twitter API.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)
3. Getting Tweets from the full-archive of public Tweets for a specific time-frame
If you want to get Tweets from the full-archive for a specific time-period, you can specify the time-period using the start_time and end_time parameters, as shown in the example below:
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

# Replace with time period of your choice
start_time = '2020-01-01T00:00:00Z'

# Replace with time period of your choice
end_time = '2020-08-01T00:00:00Z'

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                  start_time=start_time,
                                  end_time=end_time, max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    print(tweet.created_at)
4. Getting more than 100 Tweets at a time using paginator
As seen in the examples above, you can get upto 100 Tweets per request. If you need more than 100 Tweets, you will have to use the paginator and specify the limit i.e. the total number of Tweets that you want.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'covid -is:retweet'

# Replace the limit=1000 with the maximum number of Tweets you want
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
    print(tweet.id)
5. Writing Tweets to a text file
This example shows how you can write the Tweet IDs for each Tweet obtained for a search result, to a text file. Make sure to replace the file_name with the a name of your chosing. If you wish to write other fields to the text file, make sure to adjust the script below accordingly.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'covid -is:retweet'

# Name and path of the file where you want the Tweets written to
file_name = 'tweets.txt'

with open(file_name, 'a+') as filehandle:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                  tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(
            limit=1000):
        filehandle.write('%s\n' % tweet.id)
6. Getting Tweets with user information, for each Tweet
In the examples so far, we have seen how to get Tweet information for the Tweets that we have searched for. However, if you need additional information associated with the Tweet, such as the information of the user Tweeting it, you can use expansions and pass it to the search_recent_tweets function.

In this example, we want user information, which is why the value for expansions that we pass is author_id. Additionally, we will specify the user_fields that we want returned such as profile_image_url etc. Learn more about available fields here.

From the response, we will get the users list from the includes object. Then, we will look up the user information for each Tweet, using the author_id of the Tweet.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'covid -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                     user_fields=['profile_image_url'], expansions='author_id', max_results=100)

# Get users list from the includes object
users = {u["id"]: u for u in tweets.includes['users']}

for tweet in tweets.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(user.profile_image_url)
7. Getting Tweets with media information, for each Tweet
In this example, we want media information, which is why the value for expansions that we pass is attachments.media_keys. Additionally, we will specify the media_fields that we want returned such as preview_image_url etc. Learn more about available fields here.

From the response, we will get the media list from the includes object. Then, we will look up the media information for each Tweet, using the media_keys from the attachements for the Tweet.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'covid -is:retweet has:media'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                     media_fields=['preview_image_url'], expansions='attachments.media_keys',
                                     max_results=100)

# Get list of media from the includes object
media = {m["media_key"]: m for m in tweets.includes['media']}

for tweet in tweets.data:
    attachments = tweet.data['attachments']
    media_keys = attachments['media_keys']
    print(tweet.text)
    if media[media_keys[0]].preview_image_url:
        print(media[media_keys[0]].preview_image_url)
8. Searching for geo-tagged Tweets
Some Tweets have geographic information associated with them. The search endpoints in the Twitter API v2 support operators such as place, place_country, bounding_box, point_radius etc. (these operators are currently only available in the academic research product track) that allow you to get these geo-tagged Tweets.

In the example below, we want all Tweets that are from the country US, which is why we specify it in our search query using the place_country:US operator. Now because by default, only the Tweet ID and Tweet text are returned, we have to specify the fact that we want the geo information in our response as well. We do this by passing the expansions='geo.place_id' to the search_all_tweets function and we also specify the geo fields that we are looking for using place_fields=['place_type','geo'].

In our response, we get the list of places from the includes object, and we match on the place_id to get the relevant geo information associated with the Tweet (the place.full_name in the example below)
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'covid -is:retweet place_country:US'

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'geo'],
                                  place_fields=['place_type', 'geo'], expansions='geo.place_id', max_results=100)

# Get list of places from includes object
places = {p["id"]: p for p in tweets.includes['places']}

for tweet in tweets.data:
    print(tweet.id)
    print(tweet.text)
    if places[tweet.geo['place_id']]:
        place = places[tweet.geo['place_id']]
        print(place.full_name)
9. Getting Tweet counts (volume) for a search query
So far, we have seen examples of how to get Tweets for a search query. However, if you want to get the count of Tweets (volume) for a search term, you can use the get_recent_tweets_count function. You can pass it the search query and specify the granularity for the data aggregation e.g. if you want the daily count, hourly count or 15-minute count for a search term.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'covid -is:retweet'

counts = client.get_recent_tweets_count(query=query, granularity='day')

for count in counts.data:
    print(count)
The response will look something like this:
{'end': '2021-09-23T00:00:00.000Z', 'start': '2021-09-22T03:01:44.000Z', 'tweet_count': 142282}
10. Getting a user's timeline
In order to get the most recent 3200 Tweets from a user's timeline, we can use the get_users_tweets method and pass it the user id. We can also specify additional fields that we want using the tweet_fields and expansions (as shown in the examples above).
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace user ID
id = '2244994945'

tweets = client.get_users_tweets(id=id, tweet_fields=['context_annotations','created_at','geo'])

for tweet in tweets.data:
    print(tweet)

11. Getting a user's mentions
In order to get the most recent 3200 mentions for a user, we can use the get_users_mentions method and pass it the user id. We can also specify additional fields that we want using the tweet_fields and expansions (as shown in the examples above).
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace user ID
id = '2244994945'

tweets = client.get_users_mentions(id=id, tweet_fields=['context_annotations','created_at','geo'])

for tweet in tweets.data:
    print(tweet)
12. Getting a user's followers
In order to get the followers of a user, we can use the get_users_followers function and pass it the user ID. If we want additional fields for the User object such as profile_image_url, we can specify those using the user_fields parameter.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace user ID
id = '2244994945'

users = client.get_users_followers(id=id, user_fields=['profile_image_url'])

for user in users.data:
    print(user.id)
13. Getting users that a user follows
In order to get the list of users that a user follows, we can use the get_users_following function and pass it the user ID. If we want additional fields for the User object such as profile_image_url, we can specify those using the user_fields parameter.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace user ID
id = '2244994945'

users = client.get_users_following(id=id, user_fields=['profile_image_url'])

for user in users.data:
    print(user.id)
14. Getting users that like a Tweet
In order to get the list of users that like a Tweet, we can use the get_liking_users function and pass it the Tweet ID. If we want additional fields for the User object such as profile_image_url, we can specify those using the user_fields parameter.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace Tweet ID
id = '1441054496931541004'

users = client.get_liking_users(id=id, user_fields=['profile_image_url'])

for user in users.data:
    print(user)

15. Getting users that retweeted a Tweet
In order to get the list of users that retweeted a Tweet, we can use the get_retweeters function and pass it the Tweet ID. If we want additional fields for the User object such as profile_image_url, we can specify those using the user_fields parameter.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace Tweet ID
id = '1441054496931541004'

users = client.get_retweeters(id=id, user_fields=['profile_image_url'])

for user in users.data:
    print(user)
16. Getting Tweets that a user liked
In order to get the list of Tweets that a user liked, we can use the get_liked_tweets function and pass it the User ID. If we want additional fields for the Tweet object such as context_annotations, created_at etc. we can specify those using the tweet_fields parameter.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace User ID
id = '2244994945'

tweets = client.get_liked_tweets(id=id, tweet_fields=['context_annotations','created_at','geo'])

for tweet in tweets.data:
    print(tweet)
17. Lookup Tweets using Tweet IDs
In some cases, if we have a list of Tweet IDs and want to build the Tweet dataset for these Tweet IDs, we can use the get_tweets function and pass it the list of Tweet IDs. By default, only the Tweet ID and Tweet text are returned. If we want additional Tweet fields, we can specify those using tweet_fields parameter.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace Tweet IDs
ids = ['1409935014725177344', '1409931481552543749', '1441054496931541004']

tweets = client.get_tweets(ids=ids, tweet_fields=['context_annotations','created_at','geo'])

for tweet in tweets.data:
    print(tweet)
18. Lookup Users using User IDs
In some cases, if we have a list of User IDs and want to build the User dataset for these User IDs, we can use the get_users function and pass it the list of User IDs. If we want additional User fields, we can specify those using user_fields parameter.
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace User IDs
ids = ['2244994945']

users = client.get_users(ids=ids, user_fields=['profile_image_url'])

for user in users.data:
    print(user.profile_image_url)
19. Create a Tweet
If you want to create a Tweet with Tweepy using the Twitter API v2, you will need to make sure that you have your consumer key and consumer secret, along with your access token and access token secret, that are created with Read and Write permissions. You will use these keys and token when initializing the client as shown below.
import tweepy

client = tweepy.Client(consumer_key='REPLACE_ME',
                       consumer_secret='REPLACE_ME',
                       access_token='REPLACE_ME',
                       access_token_secret='REPLACE_ME')

# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text='hello world')

print(response)
20. Retweet a Tweet
If you want to retweet a Tweet with Tweepy using the Twitter API v2, you will need to make sure that you have your consumer key and consumer secret, along with your access token and access token secret, that are created with Read and Write permissions (similar to the previous example). You will use these keys and token when initializing the client as shown below.
import tweepy

client = tweepy.Client(consumer_key='REPLACE_ME',
                       consumer_secret='REPLACE_ME',
                       access_token='REPLACE_ME',
                       access_token_secret='REPLACE_ME')

# Replace the Tweet ID that you want to retweet
response = client.retweet(1409931481552543749)

print(response)
21. Replying to a Tweet
If you want to reply to a Tweet with Tweepy using the Twitter API v2, in the create_tweet method, you can simply pass the in_reply_to_tweet_id with the ID of the Tweet that you want to reply to, as shown below:
import tweepy

client = tweepy.Client(consumer_key='REPLACE_ME',
                       consumer_secret='REPLACE_ME',
                       access_token='REPLACE_ME',
                       access_token_secret='REPLACE_ME')

# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text='hello world reply', in_reply_to_tweet_id=12345678)

print(response)
These are some common examples of working with the Twitter API v2 using Tweepy. As Tweepy adds support for additional endpoints, we will update this post to include examples of using those endpoints.

If you have any questions or feedback about this guide, please feel free to reach out to me on Twitter!

Also, special shoutout to Harmon and the contributors of the Tweepy package for supporting the Twitter API v2 and the academic product track.

Top comments (12)

Subscribe
pic
Add to the discussion
 
 
y3khan profile image
Yasser Khan
•
Dec 27 '21

great tutorial. I am glad you used tweepy to show the functionalities! Thank You

Few notes:

I was not able to execute some statements because I do not have access to the academic research account
I was not able to complete # 9. Getting Tweet counts (volume) for a search query because It says , "unexpected parameter: granularity".

1
 like
Like
Reply
 
 
jwang14247372 profile image
J Wang
•
Jan 7 '22

Great tutorial.


2
 likes
Like
Reply
 
 
mble profile image
Maciej Błędkowski
•
Nov 5 '22

I get this error and I have no idea why, in other project that uses Twitter API v1 every works fine:
tweepy.errors.Unauthorized: 401 Unauthorized


1
 like
Like
Reply
 
 
mikkel_thomhav_6b720a53a7 profile image
Mikkel Thomhav
•
Feb 10

Hey man. Thank you so much for this article.
I was stuck with a problem for 7 days, but it's solved now.
I still have one small problem though, and i think you can help me out.
Is there any ways to contact you? Would you mind adding me on telegram?
Username: everydaypsychologies

or write me an email at: mikkelthomav@gmail.com

Best regards
Mikkel


1
 like
Like
Reply
 
 
bserjeantson profile image
Brett Serjeantson
•
Jun 13 '22

So I have streaming working for V2. However, it seems that the only data I can get for the author of the incoming tweets is the author_id.

Does this mean I have to do a separate user lookup to get username, description, etc... using the following?

users = client.get_users(ids=idarray, user_fields=fieldarray)

Also, I see there is an allowance of 900 calls per 15 minutes. However, when I run the following function, 'data = api.rate_limit_status()', I can't see any of my calls being decremented.

Thoughts?


1
 like
Like
Reply
 
 
zeguil profile image
José Guilherme
•
Nov 25 '21

two questions:
1 - How can I reply to tweets?
2 - How can I tweet an image?


1
 like
Like
Reply
 
 
taotetom profile image
TaoTeTom
•
Dec 13 '21

Question:

If I want to search for a given topic or for tweets that have above x likes how would I do that?

Thanks this guide has been uber helpful


1
 like
Like
Reply
 
 
goldytech profile image
Muhammad Afzal Qureshi
•
Mar 17 '22

Thanks for the great post. How can I retrieve all the replies for a given tweet ?


1
 like
Like
Reply
 
 
srisai1796 profile image
Sri_Sai
•
Mar 20 '22

Hey, This is really helpful. Is there any update on Filtered Stream in Python in a similar way ? @TwitterDev


Like
Reply
 
 
szyle profile image
szyle
•
Jul 29 '22

i needed this. thank you.


1
 like
Like
Reply
 
 
thalibarrifqi profile image
gray november, hey december
•
Nov 30 '21

How to add language filter when using pagination?


Like
Reply
 
 
kiprono profile image
Kiprono
•
Mar 6 '22

Hey @suhemparack How can I tweet an image?


Like
Reply
Code of Conduct • Report abuse
DEV Community

🚀 Update Your DEV Experience Level:
Settings

Go to your customization settings to nudge your home feed to show content more relevant to your developer experience level. 🛠

Read next
k_ndrick profile image
Data Science for Beginners: 2023 - 2024 Complete Roadmap
Kendrick Onyango - Sep 30

bshadmehr profile image
Unveiling the Factory Method Design Pattern in Python
Bahman Shadmehr - Aug 28

jdenzel profile image
How to get started with SQLAlchemy
Denzel - Aug 28

lannuttia profile image
Announcing Starlette Session Middleware
Anthony Lannutti - Aug 27


TwitterDev
Follow
Build What's Next
Questions about how to use our APIs, or want to learn more?

Come join the discussion with other developers using the Twitter platform, and share your own knowledge!

Visit our community
More from TwitterDev
Handling Refresh Tokens in the OAuth 2.0 Authorization Code Flow with PKCE with Flask
#python #twitter #oauth2 #showdev
A guide to working with the Twitter API v2 in Java using twitter-api-java-sdk
#java #beginners #twitter #api
Tweet to Super Followers with Postman, OAuth 2.0 and Manage Tweets
#twitter #showdev #beginners #postman
DEV Community

Hacktoberfest is happening now!

Hacktoberfest 2023 is happening now!
Throughout this month, developers from all around the world will come together to contribute to open-source projects, learn, and grow as a community.

Find more information about participating on DEV

import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)
DEV Community — A constructive and inclusive social network for software developers. With you every step of your journey.

Home
Podcasts
Videos
Tags
FAQ
Advertise on DEV
About
Contact
Guides
Software comparisons
Code of Conduct
Privacy Policy
Terms of use
Built on Forem — the open source software that powers DEV and other inclusive communities.

Made with love and Ruby on Rails. DEV Community © 2016 - 2023.