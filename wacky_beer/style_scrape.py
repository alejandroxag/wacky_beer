# Data Focused Python
# Group Project
# Team Wacky
# Beer style information scraping functions
# style_scrape.py

import requests
from bs4 import BeautifulSoup
import json
import re

def beer_styles_urls():
    """ Scrapes all the urls corresponding to a beer style from the website craftbeer.com/styles
        Parameters:
        Returns:
        dict: Dictionary with beer style names as keys and urls as values.
    """
    soups = [soup.find() for soup in BeautifulSoup(requests.get('https://www.craftbeer.com/beer-styles').content, 'html.parser').find(id = 'styles').find_all(class_ = 'style')]
    return [(soup.find(class_ = 'caption-title').get_text().strip().upper(), soup.find(class_ = 'caption').find('a')['href']) for soup in soups]

def bs_soup(url):
    """ Cooks the soup to scrape the beer style template.
        Parameters:
        url (str): URL of a beer style from the website craftbeer.com/styles
        Returns:
        (str, bs4.element.Tag): tuple containing the id and soup corresponding to the url's beer style.
    """
    print('hola')
    try:
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        json_script = str(soup.find(id = 'wpp-json'))
        idx0 = re.search('(<script).*(>)', json_script).span()[1]
        idx1 = re.search('(</script>)$', json_script).span()[0]
        bs_id = json.loads(json_script[idx0:(idx1 - 1)])['ID']
        return bs_id, soup.find(id = f'post-{bs_id}')
    except Exception as e:
        print(e)
        return None

def bs_name(bs_soup):
    """ Scrapes the name of the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        (str): beer style name.
    """
    try: return bs_soup[1].find(class_ = 'entry-title').get_text().strip()
    except: return None

def bs_desc(bs_soup):
    """ Scrapes the description of the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        (str): beer style description.
    """
    try: return ' '.join([p.get_text() for p in bs_soup[1].find(class_ = 'entry-content').find_all('p')])
    except: return None

def bs_cat(bs_soup):
    """ Scrapes the category of the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        (str): beer style category.
    """
    try: return bs_soup[1].find(id = 'knowledge').find(class_ = 'section-title').find(class_ = 'popovers').get_text()
    except: return None

def bs_color(bs_soup):
    """ Scrapes the color level of the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        (str): color-level range of the beer style.
    """
    try: return bs_soup[1].find(id = 'sliders').find_all(class_ = 'slider-container')[0].find(class_ = 'below').get_text().split('(')[0].strip()
    except: return None

def bs_ibu(bs_soup):
    """ Scrapes the ibu level of the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        (str): IBU-level range of the beer style.
    """
    try: return bs_soup[1].find(id = 'sliders').find_all(class_ = 'slider-container')[1].find(class_ = 'below').get_text().split('(')[0].strip()
    except: return None

def bs_pairings(bs_soup):
    """ Scrapes the food pairings for the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        (list): List of (strings) food pairings for the beer style.
    """
    try: return [node.get_text().strip() for node in bs_soup[1].find(id = 'learn').find(id = 'pairings').find_all('li')]
    except: return None

def bs_glassware(bs_soup):
    """ Scrapes the type of glassware recomended for the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        (str, str): Tuple containing the type of glassware recomended and its description (type, description).
    """
    glass = bs_soup[1].find(id = 'learn').find(id = 'glassware').find(class_ = 'glass')
    try: return glass.get_text().strip(), glass.find(class_ = 'popovers')['data-content'].strip()
    except: return None

def bs_temp(bs_soup):
    """ Scrapes serving temperature recomended for the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        str: Recomended serving temperature for the beer style.
    """
    try: return bs_soup[1].find(id = 'learn').find(id = 'glassware').find(class_ = 'temp').get_text().strip()
    except: return None

def bs_features(bs_soup):
    """ Scrapes the color, flavor, aroma, sensations and ingredients features of the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        dict: Dictionary with the type of feature (APPEARANCE, FLAVOR/AROMA, SENSATIONS, INGREDIENTS) as keys
        and dictionaries as values. Each dictionary value has the name of the corresponding feature as key,
        and de description of that particular feature for the beer style as value.
    """
    try:
        ft_soups = [bs_soup[1].find(id = 'attributes').find(id = ft) for ft in ['appearance', 'flavor', 'palette', 'process']]
        h3 = [soup.find('h3').get_text().strip().upper() for soup in ft_soups]
        ft_l = [[[s.get_text().strip().upper() for s in l] for l in [soup.find_all(node) for soup in ft_soups]] for node in ['h4','p']]
        return {h3[i]:dict(zip(ft_l[0][i],ft_l[1][i])) for i in range(4)}
    except: return None

def bs_sugg(bs_soup):
    """ Scrapes suggested beer styles for the beer style.
        Parameters:
        bs_soup (bs4.element.Tag): the second element of the tuple returned by bs_soup.
        Returns:
        list: List of suggested beer styles(strings).
    """
    try: return [sug.get_text().strip() for sug in bs_soup[1].find(id = 'ymal').find(class_ = 'ymal').find_all('li')]
    except: return None

def bs_getinfo(url):
    """ Executes bs_soup for a given url and then all the info-scraping functions and compiles the info in a dictionary.
        Parameters:
        url (str): URL of a beer style from the website craftbeer.com/styles
        Returns:
        dict: Dictionary with different elements from the beer style as keys, and the corresponding information
        scraped with the info-scraping functions as values.
    """
    try: return {ft.upper():eval(f'bs_{ft}')(bs_soup(url)) for ft in ['name', 'desc', 'cat', 'color', 'ibu', 'pairings', 'glassware', 'temp', 'features', 'sugg']}
    except: return None
