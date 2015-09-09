import praw
 
def main():
     r = praw.Reddit(user_agent='news_reader')
     submissions = r.get_subreddit('news').get_hot(limit=30)
     submission_form = "{}) {} : {} <{}>"
     count = 1
     print("Top 30 Posts from /r/news")
     print('-' * 25)
     for sub in submissions:
         print(submission_form.format(count, sub.ups, sub.title, sub.url))
         count += 1
main()