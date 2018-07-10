#!/usr/bin/env python

import sys
import urllib
import argparse
import requests
import lxml.html

NCBI_BASE_URL= 'https://www.ncbi.nlm.nih.gov'
NCBI_SEARCH_PATH = 'pubmed/?term='
NCBI_SEARCH_TERM = 'notch'


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Search PubMed for given term(s) and return URLs and '
                    'titles from first page of search results')
    parser.add_argument('terms', nargs='*', default=['notch'],
                        help='The search term(s) [default: "notch"]')

    args = parser.parse_args()
    terms = urllib.parse.quote(' '.join(args.terms))  # percent-encoded
    query_url = NCBI_BASE_URL + '/' + NCBI_SEARCH_PATH + terms

    with requests.Session() as s:
        response = s.get(query_url)
        assert response.ok

        # see: https://stackoverflow.com/a/15622069
        html = lxml.html.fromstring(response.content)
        anchors = html.xpath('//p[@class="title"]/a')

        # suppress this in the output by redirecting stderr to /dev/null,
        # e.g., './notchfinder.py notch 2>/dev/null'
        print('# ' + query_url, file=sys.stderr)

        for anchor in anchors:
            print(NCBI_BASE_URL + anchor.attrib['href'], end='')  # no EOL
            # text_content() method strips all inner tags (like <b></b>)
            print("\t", anchor.text_content())
