import praw
from pprint import pprint
from urllib import urlretrieve
import pickle


#Creates the Reddit object
r = praw.Reddit(user_agent='/r/museum scraper by /u/UnclePolycarp')

already_grabbed = pickle.load(open("save.p", "rb"))

#Code for pulling all recent submissions
subreddit = r.get_subreddit('museum')
for submission in subreddit.get_hot(limit=10):
	if submission.id in already_grabbed:
		break
	else:
		#Pulls url of /r/museum image
		url = submission.url
		title = submission.title
		response = urlretrieve(url, title + '.jpg')
		already_grabbed.append(submission.id)

pickle.dump(already_grabbed, open("save.p", "wb"))


		