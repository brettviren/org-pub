#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

org_pub_dir = os.path.expanduser('~/org-pub')
pel_dir = os.path.join(org_pub_dir, 'pelican')
orgonpy_dir = os.path.join(pel_dir, 'orgonpy')
theme_dir = os.path.join(pel_dir, 'themes')

AUTHOR = u'Brett Viren'
SITENAME = u'They Call Me Brett'
SITEURL = 'http://localhost:800'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('BNL', 'http://www.phy.bnl.gov/~bviren/'),
    ('GitHub', 'https://github.com/brettviren/'),
)

# my hacked version of 'elegant'
THEME = os.path.join(theme_dir, 'elegant')

# Social widget - modified for my copy of 'elegant' theme
SOCIAL = (
    ("GitHub","github","https://github.com/brettviren"),
    ("Personal Email","envelope","mailto:brett.viren@gmail.com"),
    ("Work Email","envelope","mailto:bv@bnl.gov"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = [os.path.join(orgonpy_dir,'python'),
                os.path.join(orgonpy_dir,'pelican-plugin')]
#                os.path.expanduser('~/org-pub/pelican/pelican-plugins')]
PLUGINS = ['orgonpy','extract_toc']

# this copies all source material
STATIC_PATHS = [ '.' ]

# these are specific to elegant 

LANDING_PAGE_ABOUT =dict(
    title = 'They Call Me Brett',
    details =
''' 

<p> I am a human residing mostly on the Island of Long, off the
Eastern coast of the North American Continent, Earth, Milky Way
Galaxy.  </p>

<p> Other centers of my online identity include: </p>

<ul>

<li> Personal: 
<a href="mailto:brett.viren@gmail.com">email</a>
<a href="https://github.com/brettviren">github</a>
</li>

<li>BNL: 
<a href="http://www.phy.bnl.gov/~bviren/">web</a>
<a href="mailto:bv@bnl.gov">email</a>
<a href="http://www.phy.bnl.gov/edg/w">EGD</a>
<a href="http://www.bnl.gov/Physics/">Physics</a>
</li>

<li> DUNE: 
<a href="http://www.dunescience.org/">web</a>
<a href="https://dune.bnl.gov/">@BNL</a>
<a href="https://github.com/DUNE">github</a>
</li>

<li> Daya Bay: 
<a href="http://dayabay.bnl.gov/">@BNL</a>
</li>

</ul>

<p> This web sites hold links to and notes on software, Physics and
various other pursuits that my life takes.  </p>

<p> To the right are some active, major projects I'm involved in and
see below for most recent notes.  I tend to update old notes from time
to time so check the last update stamp.  This site is always under
construction to don't mind the dust.  </p> ''')


PROJECTS = [
    dict(
        name =  'DUNE',
        url ='https://dune.bnl.gov/',
        description = 'The next generation long-baseline neutrino experiment may discover CP violation in the neutrino sector and will measure the neutrino mass hierarchy and other neutrino oscillation parameters.',
    ),
    dict (
        name =  'Daya Bay',
        url ='https://dayabay.bnl.gov/',
        description = 'Reactor anti-neutrino precision theta13 measurement experiment.',
        ),
    dict(
        name='Wire Cell',
        url='https://github.com/BNLIF/wire-cell',
        description='A novel liquid-argon reconstruction technique developed by our group at BNL.'
        ),
    dict(
        name = 'OrgOnPy',
        url = 'https://github.com/brettviren/orgonpy',
        description = 'Org markup exported to JSON and processed with Python.  It partly powers this web site.'),
    dict(
        name='Worch',
        url='https://github.com/brettviren/worch',
        description = 'Orchestrate building of large software suites with Waf.',
    ),
    dict(
        name='GeGeDe',
        url='https://github.com/brettviren/gegede',
        description='General Geometry Description for authoring detector and beam geometries.',
        ),
    dict(
        name='nuosc++',
        url='https://github.com/brettviren/nuosc',
        description='C++ library and command line tool for calculating neutrino oscillation probabilities.',
        ),
    dict(name="etc",
         url="https://github.com/brettviren/",
         description='and others.',
         ),
    ]
