#!/usr/bin/env python

import re
import os
import sys
import requests
import lxml.html

NCBI_BASE_URL= 'https://www.ncbi.nlm.nih.gov'
NCBI_SEARCH_URL = 'pubmed/?term='
NCBI_SEARCH_TERM = 'notch'


if __name__ == '__main__':
    with requests.Session() as s:
        response = s.get(NCBI_BASE_URL + '/' + NCBI_SEARCH_URL
                         + NCBI_SEARCH_TERM)

        assert response.ok

        # see: https://stackoverflow.com/a/15622069
        html = lxml.html.fromstring(response.content)
        html.xpath('//p[@class="title"]/a')

        for anchor in html.xpath('//p[@class="title"]/a'):
            print(NCBI_BASE_URL + anchor.attrib['href'])
