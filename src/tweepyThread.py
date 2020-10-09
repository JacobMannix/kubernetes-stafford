# # Jacob Mannix [08-31-2020]

# TweepyThread function to tweet multiple tweets in a thread

# Import Dependencies
import tweepy

# -----
# Only needed if defining api keys here
# import os

# # Changing path to parent path
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir) # getting parent directory for envpath
# sys.path.append(parentdir) # changing path for local modules

# # Load Environment Variables - from env.env file
# envpath = parentdir + "/env.env" # Set directory of env.env file
# from dotenv import load_dotenv
# load_dotenv(dotenv_path = envpath)
# -----

# Function
def tweepyThread(user, list):
    # Define Authentication keys through environmental variables
    # ckey = os.getenv("API_KEY_TC")
    # csecret = os.getenv("API_SECRET_TC")
    # atoken = os.getenv("API_ACCESS_TOKEN_TC")
    # asecret = os.getenv("API_ACCESS_SECRET_TC")

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # Create API object
    api = tweepy.API(auth)
    
    # Loops through list to reply to the previous tweet to create a thread
    count = 0
    for i in list:
        statuses = api.user_timeline(user, count = 1) 
        count += 1
        if count > 1:
            for status in statuses:
                tweetid = status.id
            api.update_status(status = i, in_reply_to_status_id = tweetid , auto_populate_reply_metadata=True)
            # time.sleep(2) # optional sleep between each tweet
        else:
            api.update_status(status = i)
            # time.sleep(2) # optional sleep between each tweet
