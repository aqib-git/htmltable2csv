import sys
import os
import csv
from urllib.request import urlopen
from urllib.parse import urlparse
from pathlib import Path

from parser import TableParser

class Table2CSV:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

        self.table2csv()

    def table2csv(self):
        html = self.get_html(self.source)

        if type(html) != str:
            return
        
        parser = TableParser()

        parser.feed(html)
        
        if (len(parser.tables) == 0):    
            return

        for index, table in enumerate(parser.tables):
            self.tocsv(table, index)

        self.destination = Path(self.destination)

        self.log('Done! Number of Tables found => {}'.format(len(parser.tables)))
        self.log('Check CSV files in => {}'.format(self.destination.resolve()))

    def tocsv(self, table, index): 
        filename = Path(self.destination + '/table_' + str(index + 1) + '.csv')
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            
            for tr in table:
                csvwriter.writerow(tr)

    def get_html(self, source):
        try:
            scheme = urlparse(source).scheme

            if not scheme.startswith('http'):
                 return self.get_html_from_file(source)

            return self.get_html_from_url(source)
        except:
            return self.get_html_from_file(source)

    def get_html_from_url(self, url):
        with urlopen(url) as response:
            return response.read().decode('utf-8')

    def get_html_from_file(self, file):
        filepath = Path(file).resolve()
        
        if not filepath.exists():
            self.log('{} doesn\'t exist'.format(filepath))
            
            return

        if not filepath.is_file():
            return

        if filepath.suffix != '.html':
            self.log('Source file must have .html extension.')

            return

        with open(filepath, 'r', newline='') as f:
            return f.read()

    def log(self, message):
        if __name__ != '__main__':
            return
        
        print(message)

if __name__ == '__main__':
    argc = len(sys.argv)

    if argc <= 2:
        print('Usage: python3 table2csv.py [SOURCE] [DESTINATION]\n')
        print('[SOURCE] URL of a WebPage or Path to HTML file.\n')
        print('[DESTINATION] Path where CSV files will be stored.')
        
        sys.exit()

    Table2CSV(*sys.argv[1:])
