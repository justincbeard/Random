#!/usr/bin/python

######################################
# Praw Testing                       #
# v.1                                #
# Install with: pip install praw     #
######################################

import praw
import pprint

#Setting user agent.  
#Format of Platform : Description : Version : User Name

user_agent="Win32:praw_testing:v0.1:/u/sothereisthat"

r = praw.Reddit(user_agent)

# submissions = r.get_subreddit('linux').get_hot(limit=5)

# print [str(x) for x in submissions]

user_name = "sidious7"
user = r.get_redditor(user_name)

thing_limit = 10
gen = user.get_submitted(limit=thing_limit)

# print 'Last posts: '
# for posts in gen:
# 	print posts

karma_by_subreddit = {}

for thing in gen:
	subreddit = thing.subreddit.display_name
	print 'Subreddit name: ', subreddit
	print 'Post score: ', thing.score
	print 'Total score so far: ', karma_by_subreddit.get(subreddit,0)
	karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit,0) + thing.score)

pprint.pprint(karma_by_subreddit)

