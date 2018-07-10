#!/usr/bin/env python

import re
import os
import sys
import requests
import lxml.html

NCBI_BASE_URL= 'https://www.ncbi.nlm.nih.gov'
NCBI_SEARCH_PATH = 'pubmed/?term='
NCBI_SEARCH_TERM = 'notch'


if __name__ == '__main__':
    with requests.Session() as s:
        response = s.get("{base}/{path}{term}".format(
            base=NCBI_BASE_URL,
            path=NCBI_SEARCH_PATH,
            term=NCBI_SEARCH_TERM
        ))

        assert response.ok

        # see: https://stackoverflow.com/a/15622069
        html = lxml.html.fromstring(response.content)
        anchors = html.xpath('//p[@class="title"]/a')

        for anchor in anchors:
            print(NCBI_BASE_URL + anchor.attrib['href'])
