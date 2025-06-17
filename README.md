# Web Crawler
A Python script to crawl websites and track internal/external links

## Description
This script uses 'requests' to fetch wab pages and 're' for links extraction. It supports a command line argument to specify the domain to crawl.

## Installation
1. Clone the repository

git clone https://github.com/MxSns/web-crawler.git

2. Install dependencies
pip install requests

## Usage
Run the script with a domain argument

python3 web_crawler.py -d <url>

## Output
Crawled URLs:
List of visited internal links
External URLs:
List on links pointing outside the domain
