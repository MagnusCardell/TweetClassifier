#!/usr/bin/env python

import time
from getpass import getpass
from textwrap import TextWrapper

import tweepy


class StreamWatcherListener(tweepy.StreamListener):

    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print(self.status_wrapper.fill(status.text))
            print('\n %s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source))
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, status_code):
        print('An error has occured! Status code = %s' % status_code)
        return True  # keep stream alive

    def on_timeout(self):
        print('Snoozing Zzzzzz')


def main():
    # Prompt for login credentials and setup stream object
    # consumer_key = input('Consumer Key: ')
    # consumer_secret = getpass('Consumer Secret: ')
    # access_token = input('Access Token: ')
    # access_token_secret = getpass('Access Token Secret: ')

    consumer_key = "t1S4U7WiHxiRwje99pGrInIpG"
    consumer_secret = "ItGMAIpAFftFlgdnVa7nPC23Xt3KDnbJfWloeOWKvZp2ad0DKL"
    access_token = "819047201854857216-gVCJEqmUGQMyBsYQ0iolLgCjqKZdyEo"
    access_token_secret = "rvvBR5bQ9OJ9VLUKaVRlcAax7OotjXwbZhm6Jag4HqSMB"

    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = tweepy.Stream(auth, StreamWatcherListener(), timeout=None)
    api = tweepy.API(auth)
    # Prompt for mode of streaming

    mode = input('Start the Fetch? (type yes) ')

    if mode == 'yes':
        follow_list = input('Users to follow (comma separated): ').strip()
        track_list = input('Keywords to track (comma seperated): ').strip()
        if follow_list:
            follow_list = [u for u in follow_list.split(',')]
            userid_list = []
            username_list = []
            
            for user in follow_list:
                if user.isdigit():
                    userid_list.append(user)
                else:
                    username_list.append(user)
            
            for username in username_list:
                user = api.get_user(username)
                userid_list.append(user.id)
            
            follow_list = userid_list
            #print(userid_list)
        else:
            follow_list = None
        if track_list:
            track_list = [k for k in track_list.split(',')]
        else:
            track_list = None
        print(follow_list)
        stream.filter(follow_list, track_list)

    else:
        print(mode, ' Not fetching...')
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ('\nGoodbye!')