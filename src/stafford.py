# Jacob Mannix [08-31-2020]

#Import dependencies
import requests
import bs4
import pandas as pd
import math
from datetime import datetime
import re
import tweepy
import time
import sys
import os
# import dotenv

# Local Modules from parent directory
from webhooks import webhookMessage
from tweepyThread import tweepyThread
from staffordFile import staffordFile

#-----
# FILEPATH OF APP (specified in dockerfile)
src_path = "/app"
#-----

# Function to find mounted secrets files
def get_secret(secret_name):
    with open(src_path + "/secrets/" + secret_name, 'r') as secret_file:
        return secret_file.read()

# Variables from mounted secrets volume (handled by kubernetes)
ckey = get_secret("API_KEY")
csecret = get_secret("API_SECRET")
atoken = get_secret("API_ACCESS_TOKEN")
asecret = get_secret("API_ACCESS_SECRET")
twitterUser = get_secret("TWITTER_ACCOUNT")
webhook_url = get_secret("WEBHOOK_DISCORD")
archiveURL = get_secret("ARCHIVE_WEBSITE")

# Race Results function
def staffordResults(archiveURL):
    # Getting Page of all Race Results
    archivePage = requests.get(archiveURL)
    archiveSoup = bs4.BeautifulSoup(archivePage.text, "html.parser")
    resultsHTML = archiveSoup.find(itemprop="url")

    resultsURL = resultsHTML['href'] # Getting URL of most recent race result
    title = resultsHTML.string # Get title of article of most recent race

    # Use most recent race URL to see results of race
    resultsPage = requests.get(resultsURL)
    resultsSoup = bs4.BeautifulSoup(resultsPage.text, "html.parser")
    resultsData = resultsSoup.find(class_= "row-hover")

    # Appending Race Results to Lists
    A=[]
    B=[]
    C=[]
    for row in resultsData.findAll("tr"):
        cells = row.findAll('td')
        # drivers = row.findAll('th')
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
    
    # Append A,B,C Lists to new list with some formatting
    list_index = []
    list_results = []
    for i in range(0,len(A)):
        list_index.append(A[i] + " (" + B[i] + ") ") # Finish and Start positions formatted in index column
        list_results.append(C[i]) # Driver Name

    # Convert Lists into DataFrame
    df = pd.DataFrame(index = list_index)
    df['Driver']=list_results
    
    # Specific Formatting for Discord
    dfDiscord = repr(df)
    dfDiscord = dfDiscord.replace('Driver', '')
    
    # Creates list for sectioning off drivers to limit 6 drivers per message
    sections = [[0,5]] # only showing top 5 drivers
    num_sections = int(len(df) / 5) + (len(df)  % 5 > 0) # Divides the number of drivers by 5 (5 per tweet) and rounds up
    list_dfString = []
    for i,j in sections[:int(num_sections)]:
        dfString = repr(df[i:j])

        # Formatting string to contain less characters
        dfString = dfString.replace('  ', '')
        dfString = dfString.replace(') ', ')')
        dfString = dfString.replace(')', ') ')
        dfString = dfString.replace('Driver', '')
        
        list_dfString.append(title + "\n" + dfString + "\n" + " "  + "\n" + resultsHTML['href'])
    
    # Filepath of persistent data
    post_filepath = src_path + '/data/postTitle.txt'
    postTitle = staffordFile(post_filepath)

    # Checks if raceDate
    if title != postTitle:
        print(list_dfString)

        # Send race results in tweet
        # tweepyThread(twitterUser, list_dfString, ckey, csecret, atoken, asecret) # creates a tweet, takes a list

        # Send race results to discord -- Optional if you want to send results through webhook
        message_content = title + "\n" + dfDiscord
        webhookMessage(webhook_url, message_content)

    else:
        print('no new race results')
        # webhookMessage(webhook_url, 'no new race results')

    # Save title to file
    with open(post_filepath, "w") as output:
        output.write(str(title.rstrip()))
    
# Calling Function
staffordResults(archiveURL)