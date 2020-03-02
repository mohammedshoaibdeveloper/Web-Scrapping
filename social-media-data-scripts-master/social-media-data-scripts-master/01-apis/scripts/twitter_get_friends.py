#!/usr/bin/env python
# encoding: utf-8
# import dependencies
import tweepy #https://github.com/tweepy/tweepy
import csv
import time

from utils import open_csv_w
# import authentication credentials
from secrets import TWITTER_C_KEY, TWITTER_C_SECRET, TWITTER_A_KEY, TWITTER_A_SECRET

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(TWITTER_C_KEY, TWITTER_C_SECRET)
auth.set_access_token(TWITTER_A_KEY, TWITTER_A_SECRET)
api = tweepy.API(auth)



# array of user names, replace them with your own choices
usernames = [
"marshallproj",
"buzzfeednews"
]



def get_friends(name):

	# open spreadsheet and add column heads
	with open_csv_w('../output/%s_friendlist.csv' % name) as f:
			writer = csv.writer(f)
			writer.writerow(["id",
							"screen_name",
							"display_name",
							"bio",
							"followers_count",
							"following_count",
							"acct_created",
							"location"

			])


	# friends_ids returns an array of the ids of all the people the user follows
	friend_ids = api.friends_ids(screen_name = name)

	# cycle through every id in the array of people that the user follows and gather information for each one
	for friend_id in friend_ids:
		user = None
		while user is None:
			try:
				user = api.get_user(friend_id)
			except tweepy.error.RateLimitError:
				print("sleeping for a minute")
				time.sleep(60)

		# write the csv
		with open_csv_w('../output/%s_friendlist.csv' % name) as f:
			writer = csv.writer(f)
			writer.writerow([friend_id,
							user.screen_name,
							user.name,
							user.description,
							user.followers_count,
							user.friends_count,
							user.created_at,
							user.location
			])
			print(user.screen_name)




# for each username run the function
for name in usernames:
	get_friends(name)
