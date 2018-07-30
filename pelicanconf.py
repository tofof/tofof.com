#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS=['pelican-plugins']
PLUGINS=['summary', 'sitemap']

AUTHOR = u'Tofof'
SITENAME = u'Negative One'
# SITEURL = "http://localhost:8000"
SITEURL = "http://tofof.com"

PATH = 'content'
STATIC_PATHS = ['images', 'files']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 5
TYPOGRIFY = True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 25

THEME = "themes/lannisport"
################################
### 
### lannisport Config Begins
###
##GOOGLE_ANALYTICS_CODE: your Google Analytics stats
SITELOGO = '/images/eipi_trans_white.png'
SITETAGLINE = "by Tofof"
SITEDESCR = "Tirades, trials, tasks and trivialities of a 21<sup>st</sup>-century polymath"

DISQUS_SITENAME = "tofof"

EMAIL_URL = 'web@tofof.com'
#TWITTER_URL = 'http://twitter.com/tofof'
#GOOGLE_URL = 'https://plus.google.com/105275131994304318274/'
#GITHUB_URL: URL to your GitHub page, for the social icons
#LINKEDIN_URL: URL to your LinkedIn page, for the social icons
#FACEBOOK_URL: URL to your Facebook page, for the social icons
#FLICKR_URL: URL to your Flickrpage, for the social icons
#LICENSE_NAME: the license for your content (e.g. CC BY-SA)
#LICENSE_URL: the link to where the full text of your license is
#ARCHIVES_URL: the link to your archives
#CONTACT_URL: the link to your contact page
### 
### lannisport Config Ends
###
################################

# Blogroll
LINKS = (
	('wdtz / Will Dietz', 'http://wdtz.org'),
	('nohelix / Noelle James', 'http://nohelix.com'),
)

# Social widget
SOCIAL = (
#	('Email', 'mailto:wdietz2@uiuc.edu', 'fa-envelope'),
#	('Twitter', 'http://twitter.com/wdtz', 'fa-twitter'),
#	('Github', 'http://github.com/dtzWill', 'fa-github'),
#	('Facebook', 'http://facebook.com/dtzWill', 'fa-facebook-square'),
#	('Google-Plus', 'http://wdtz.org/+', 'fa-google-plus'),
#	('##uiuc on Freenode', 'http://webchat.freenode.net/?channels=%23%23uiuc', 'fa-comment'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.75,
        'indexes': 0.25,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

