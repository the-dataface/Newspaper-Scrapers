# Newspaper Scrapers

## A quick precursor: 
We used these scripts to collect data for two projects on The DataFace's website: [34 Percent of Articles about Trump Now Mention His Twitter Activity](http://thedataface.com/trumps-twitter-activity/) and [Trump and the Media: A Text Analysis](http://thedataface.com/trump-media-analysis/).

NewspaperScraper.py provides support for scraping the websites of 14 major media outlets. They are listed below:
* New York Times
* Washington Post
* Wall Street Journal
* USA Today
* CNN
* Fox News
* Politico
* Slate
* CNBC
* Bloomberg
* TIME
* The Weekly Standard
* LA Times
* Chicago Tribune

You can extend the library to support other websites by creating new classes in NewspaperScraper.py. Just make sure your class inherits from NewspaperScraper, then write your own version of get_pages() specific to each new site!

## Dependencies:
This project is indebted to the great work of Lucas Ou-Yang and his [Newspaper library](http://newspaper.readthedocs.io/en/latest/).

Here are the rest of the project's dependencies. Be sure to install these before proceeding:
* [requests](http://docs.python-requests.org/en/master/)
* [selenium](http://selenium-python.readthedocs.io/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* MongoDB + [pyMongo](https://api.mongodb.com/python/current/)
* [pytz](http://pythonhosted.org/pytz/)

## Here's how to use this thing...
A NewspaperScraper object expects four inputs (at a minimum). The scraper's name, a search term, a start date, and an end date. After initializing a scraper, the intended workflow is as follows:
* First, run get_pages() to find the URLs of all articles matching the search term within the relevant time period.
* Then, run newspaper_parser() to grab metadata about each article returned by get_pages()
* Finally, store the data using either write_to_mongo() or write_to_csv()

If you have mongoDB installed, you can get started quickly by referencing RunScrapers.py. You'll simply write the four inputs on the command line.

Note 1: NYT and WSJ require the credentials of a subscribed user to work. Those can be input as command line arguments as well (see RunScrapers.py).

Note 2: Some scrapers work better than others. We had some glitches gathering data from NYT and CNN in particular (oops), so feel free to fork + improve!

## What you'll end up with:
A database (or file) that contains the following pieces of metadata about each article:
* title
* date_published
* news_outlet
* authors
* feature_img
* article_link
* keywords
* movies
* summary
* text
* html
