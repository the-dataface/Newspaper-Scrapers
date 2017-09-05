import sys
from pymongo import MongoClient
from NewspaperScraper import *

client = MongoClient()
db = client.News_database


def run_scraper (scraper):
    scraper.get_pages()
    data = scraper.newspaper_parser()
    scraper.write_to_mongo(data, db.articles_about_fake_news_rerun)


def initialize_scraper (args):
    if args[1] == 'Chicago Tribune':
        run_scraper(ChicagoTribuneScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'Los Angeles Times':
        run_scraper(LaTimesScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'Washington Post':
        run_scraper(WashPostScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'Slate':
        run_scraper(SlateScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'Politico':
        run_scraper(PoliticoScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'Fox News':
        run_scraper(FoxNewsScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'The Weekly Standard':
        run_scraper(WeeklyStandardScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'Bloomberg':
        run_scraper(BloombergScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'TIME':
        run_scraper(TimeScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'Wall Street Journal':
        run_scraper(WSJScraper(args[1], args[2], args[3], args[4], args[5], args[6]))
    elif args[1] == 'New York Times':
        run_scraper(NYTScraper(args[1], args[2], args[3], args[4], args[5], args[6]))
    elif args[1] == 'CNN':
        run_scraper(CNNScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'USA Today':
        run_scraper(USATodayScraper(args[1], args[2], args[3], args[4]))
    elif args[1] == 'CNBC':
        run_scraper(CNBCScraper(args[1], args[2], args[3], args[4]))


if __name__ == "__main__":
    initialize_scraper(sys.argv)
