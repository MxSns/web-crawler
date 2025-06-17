# Script : web_crawler.py
# Author : mxn

import argparse, requests, sys, re
from urllib.parse import urljoin

parser = argparse.ArgumentParser(description='Web crawler script to recursively visit pages within a specified domain, logging crawled URLs and external references.\nRun with: python3 web_crawler.py --domain <URL>')
parser.add_argument('-d', '--domain', required=True, help='the domain to crawl in')
args = parser.parse_args()

domain = args.domain
to_crawl = [domain]
crawled = []
external = []

# This function will request a webpage and return the html text
def fetch_page(url):
    try:
        response = requests.get(url)

    except requests.exceptions.RequestException as e:
        sys.exit(e)
    # Remove the url if it is in the to_crawl list
    if url in to_crawl:
        to_crawl.remove(url)
    # Add the url to the crawled list
    crawled.append(url)

    return response.text

# This function will parse the HTML for links decide which needs to be visited
def get_linked_pages(html):

    pattern = r'<a\s+href=\"?([^\">\s]+).*?([a-z0-9: ]+)</a>'

    links = re.findall(pattern, html, re.I)
    for link in links:
        # Access the URL in match group 0.
        this_url = link[0]
        page = urljoin(domain, this_url)

        # Check if the domain is in the current URL
        inDomain = re.search(domain, page, re.I)
        if inDomain:
            if page not in crawled and page not in to_crawl:
                to_crawl.append(page)
        # Otherwise not in domain, it's an external link
        elif page not in external:
             external.append(page)

# This will continue until the to_crawl list is empty (equals false)
while to_crawl:
    for url in to_crawl:
        for url in to_crawl:
            html = fetch_page(url)
            get_linked_pages(html)

print("\nCrawled URLs...."+str(crawled))
print("\nExternal URLs...."+str(external))
