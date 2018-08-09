#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS=['pelican-plugins']
PLUGINS=['summary', 'sitemap', "tag_cloud"]

AUTHOR = u'Brian James'
SITENAME = u'Negative One'
SITEURL = "http://tofof.com"

PATH = 'content'
STATIC_PATHS = ['images', 'files']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TIMEZONE = u'America/Chicago'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 5
TYPOGRIFY = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 25

THEME = "themes/euler-theme"
################################
### 
### euler-theme Config Begins
###
ARCHIVES_URL = 'archives.html'
SITELOGO = '/images/eipi_trans_white.png'
SITETAGLINE = u"by Tofof"
SITEDESCR = u"Tirades, trials, tasks and trivialities of a 21<sup>st</sup>-century polymath"
#DISQUS_SITENAME = "tofof"
LICENSE_IMAGE = '<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" />'
LICENSE_NAME = u'CC BY-SA 4.0'
LICENSE_URL  = 'http://creativecommons.org/licenses/by-sa/4.0/'
EMAIL_URL = 'web@tofof.com'
TWITTER_URL = 'https://twitter.com/tofof'
#GOOGLE_URL = 'https://plus.google.com/105275131994304318274/'
GITHUB_URL = 'https://github.com/tofof'
#LINKEDIN_URL = URL to your LinkedIn page, for the social icons
#FACEBOOK_URL = URL to your Facebook page, for the social icons

# Social widget
SOCIAL = (('Email web@tofof.com',   'fas fa-envelope',      'mailto:web@tofof.com'),
          ('GitHub',                'fab fa-github',        'http://github.com/tofof'),
          # ('Twitter',               'fab fa-twitter',       'http://twitter.com/tofof'),
          ('BoardGameGeek',         'fas fa-dice',          'http://boardgamegeek.com/user/tofof'),
          ('Slashdot',              'icon-slashdot',        'http://slashdot.org/~Tofof'),
          # ('Google+',               'fab fa-google-plus',   'http://plus.google.com/105275131994304318274/'),
          ('Youtube',               'fab fa-youtube',       'http://youtube.com/channel/UCZF7fWxrCQZRo3Yvpf7u4rQ')
          )

#CONTACT_URL = the link to your contact page
##GOOGLE_ANALYTICS_CODE= your Google Analytics stats
### 
### euler-theme Config Ends
###
################################

# Blogroll
LINKS = (
	('wdtz / Will Dietz', 'http://wdtz.org'),
	('nohelix / Noelle James', 'http://nohelix.com'),
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

