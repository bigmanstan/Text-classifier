"""main module."""
# Ishmeet Singh
# Twitter Scraping and Sentiment Analysis
# Copyright 2018 Licensed under MIT License
# A GUI program for scraping twitter data without dealing with the API.
import sys

from MinorProject.cli import clii
if __name__ == "__main__":
    clii(sys.argv[1:])
