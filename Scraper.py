import praw
from praw.models import MoreComments

import re

import json
import os
import time

class Scraper():

    def __init__(self):
        pass

    """
    read in the login credentials
    """
    def get_credentials(self):
        client_secret = client_id = user_agent = None
        
        with open('credentials.json', 'r') as cred_file:
            json_data = json.load(cred_file)
            
            client_id = json_data['client_id'].encode('utf-8')
            client_secret = json_data['client_secret'].encode('utf-8')
            user_agent = json_data['user_agent'].encode('utf-8')

            return client_id, client_secret, user_agent

    """
    get all top level comments for a given post id
    """
    def get_comments(self, post_id):
        client_id, client_secret, user_agent = self.get_credentials()

        reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent)
        reddit.read_only = True

        post = reddit.submission(id=post_id)
        post.comments.replace_more(limit=10)
        top_level_comments = list(post.comments)

        comment_list = []
        for comment in top_level_comments:
            if isinstance(comment, MoreComments):
                continue
            comment_list.append(comment.body)

        return comment_list

    """
    pre-processing comments
    """
    def format_comments(self, comment_list):
        processed = []

        for comment in comment_list:
            # remove [deleted] or [removed]
            if len(comment) < 10:
                continue

            # keep alpha numeric only
            comment_proc = re.sub(r"[^A-Za-z0-9\s]", "", comment.strip())
        
            processed.append(comment_proc)
        
        return processed

    """
    dump to file
    """
    def save_comments(self, filename, comment_map):
        if not os.path.isfile(filename):
            with open(filename, 'w') as spoiler_file:
                json.dump([], spoiler_file)

        curr_data = []
        with open(filename, 'r') as spoiler_file:
            curr_data = json.load(spoiler_file)

        for curr_comment in comment_map:
            curr_data.append(curr_comment)

        with open(filename, 'w') as spoiler_file:
            json.dump(curr_data, spoiler_file)

    """
    collect spoilers
    """
    def get_spoilers(self):
        post_ids = ['32e2vv', '336lyi', '33z8s5', '34rvno', '35jpn9', '36bh62', '375e8z', '380v9t', '38yyly', '39v18c']

        for curr_id in post_ids:
            processed_comments = self.format_comments(self.get_comments(curr_id))

            comment_map = []
            for comment in processed_comments:
                temp = {'data': comment, 'tag': 1}
                comment_map.append(temp)

            print 'Adding: ', str(len(comment_map)), 'spoilers'
            self.save_comments('spoilers.json', comment_map)
            time.sleep(5)

    """
    collect not spoiler data
    """
    def get_not_spoiler_data(self):
        post_ids = ['7cd22v', '7bfg76', '7c3q6z', '6ep9fd', '7c3q9y', '7bd71a', '776mx6']

        for curr_id in post_ids:
            processed_comments = self.format_comments(self.get_comments(curr_id))

            comment_map = []
            for comment in processed_comments:
                temp = {'data': comment, 'tag': 0}
                comment_map.append(temp)

            print 'Adding: ', str(len(comment_map)), 'not spoilers'
            self.save_comments('not_spoilers.json', comment_map)
            time.sleep(5)

    def scrape(self):
        self.get_spoilers()
        self.get_not_spoiler_data()


        

sc = Scraper()
sc.scrape()