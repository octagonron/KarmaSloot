import praw

# Initialize Reddit instance using configuration file
reddit = praw.Reddit(
    site_name="DEFAULT"
)

def fetch_hot_posts(subreddit_name, limit=5):
    subreddit = reddit.subreddit(subreddit_name)
    return subreddit.hot(limit=limit)

def main():
    subreddit_name = 'python'
    posts = fetch_hot_posts(subreddit_name)
    for post in posts:
        print(f"Title: {post.title}, Score: {post.score}, URL: {post.url}")

if __name__ == "__main__":
    main()
