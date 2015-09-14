#!/usr/bin/env python3

from bs4 import BeautifulSoup
import subprocess
import requests
import time

def search_url(terms):
    term_text = '+'.join(terms.split())
    base = "https://www.youtube.com/results?search_query="
    return base + term_text
# https://www.youtube.com/results?search_query=gzip+compression

def good_link(tag):
    if not '/watch?v=' in tag.get('href'):
        return False
    elif not tag.has_attr('title'):
        return False
    else:
        return True

def get_number(in_str):
    numbers = '0123456789'
    num = input(in_str)
    num = ''.join([a for a in num if a in numbers])
    
    if num:
        return int(num)
    else:
        print("You didn't enter a number")
        return get_number(in_str) 
    
while True:
    terms = input("Search terms: ")
    if terms:
        url = search_url(terms)
        html = requests.get(url).text
        soup = BeautifulSoup(html, "lxml")
        videos = [v for v in soup.find_all('a') if good_link(v)]
        for i,v in enumerate(videos):
            print('[',i + 1, ']', v.get('title') )
        
        video_num = get_number('Video #:') 
        link = videos[video_num - 1].get('href')
        base = 'https://www.youtube.com'
        
        video_url = base + link
        subprocess.call(['youtube-dl',video_url])


