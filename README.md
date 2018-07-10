# PubMed article finder

This script uses [Requests] and [lxml] to parse [PubMed] search results for the
URLs and titles of the top search results matching given search term(s).

## Requirements

* Python 3.something
* [Requests]
* [lxml]

## Installation

Requires you have pip [installed][pipinstall]. _If you are using Linux, your
distro may already provide [a package][pippkg]._

```bash
# if using a virtual environment
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# make sure it works
./pm-article-finder --help
```

## Basic Usage

```bash
# find top articles matching "irf5"
./pm-article-finder irf5 

# find articles with all given search terms
./pm-article-finder notch breast cancer
```

## Authors / Contributors

| Author name          | Email
|----------------------|----------------------------
| David Cheung         | kevin.ernst -at- cchmc.org
| Kevin Ernst          | david.cheung -at- cchmc.org

## Licence

[MIT](./LICENSE.txt)


[portal]: https://dna.cchmc.org/www/main.php
[requests]: http://docs.python-requests.org/en/latest/
[lxml]: http://lxml.de/
[pubmed]: https://www.ncbi.nlm.nih.gov/pubmed
[pipinstall]: https://pip.pypa.io/en/stable/installing/
[pippkg]: https://pkgs.org/download/python-pip
