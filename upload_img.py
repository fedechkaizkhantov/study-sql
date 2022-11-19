import requests
import csv
from csv import writer
import urllib.parse
from urllib.parse import quote_plus
from selenium import webdriver



with open("2022newsfoto.csv", 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        
        for row in reader:
            print (row[0])
            k = row[0]
            URL1 = urllib.parse.quote_plus(k, safe='/', encoding=None, errors=None)
            URL = urllib.parse.unquote_plus(URL1)
            r = requests.get(URL)
            filename = row[0].split('/')[-1]
            open(filename, 'wb').write(r.content)
            print(filename)
