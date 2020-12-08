# __init__.py
# wacky-beer package
from .style_scrape import bs_urls, bs_soup, bs_name, bs_desc, bs_cat, bs_color, bs_ibu, bs_pairings, bs_glassware, bs_temp, bs_features, bs_sugg, bs_getinfo, bs_findurl
from .styles_match import bs_relation, bs_search
from .beer_api import fetchBrew, findBrewery
# from .kaggle_dataset import fetchBeerReviews
import json
import re
import requests
import bs4
import pandas as pd


__version__ = '0.1.0'
__author__ = 'Team Wacky'