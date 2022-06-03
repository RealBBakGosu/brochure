import requests
from bs4 import BeautifulSoup as soup
import os

# Define Website to Download pdf
url = 'https://github.com/RealBBakGosu/brochue/blob/13c9c8361e851afbf413d58e3e95378c43a1d945/westmoon_2022.pdf'

# Get Website content
r = requests.get(url)

# Create soup object of requests object
soup = soup(r.text, 'html.parser')

# Loop through all elements of the website with the tag a
for link in soup.find_all('a'):
    # Download pdf if the name pdf is in the hyperlink and
    # is not a None Object
    if link.get('href') is not None and '.pdf' in link.get('href'):
        # Download pdf with wget
        os.system('wget '+ link.get('href'))