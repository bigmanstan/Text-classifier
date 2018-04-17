"""cli module."""
# Twitter Scraping and Sentiment Analysis
# Copyright 2018 Licensed under MIT License
# A GUI program for scraping twitter data without dealing with the API.
import sys
import argparse

from MinorProject.scraper import scrape
from MinorProject.scraper_and_analysis import scrape_and_analyze
from MinorProject.sentiment_analysis import analyze_sentiment

class clii:
    def cli(argv=None):
        """cli entry point."""
        argv = sys.argv[1:] if argv is None else argv
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(dest="subparser_name")
        func_dict = {
            'scrape': scrape,
            'scrape-and-analyze': scrape_and_analyze,
            'analyze-sentiment': analyze_sentiment,
        }
        for key in func_dict:
            subparsers.add_parser(key, help=func_dict[key].__doc__)
        args = parser.parse_args(argv)
        if args.subparser_name in func_dict:
            func_dict[args.subparser_name]()


    if __name__ == "__main__":
        cli()
