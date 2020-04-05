import urllib.request
import sys
import os
import csv
from pathlib import Path

from .parser import TableParser

class Table2CSV:
    def __init__(self, url, dest='data'):
        self.url = url
        self.dest = dest

        self.table2csv()

    def table2csv(self):
        html = self.get_html(self.url)
        parser = TableParser()

        parser.feed(html)
    
        print('Number of tables found: {}'.format(len(parser.tables)))
        
        if (len(parser.tables) == 0):    
            return

        for index, table in enumerate(parser.tables):
            self.tocsv(table, index)

        print('Done! Check CSV files in {}'.format(self.dest))

    def tocsv(self, table, index): 
        filename = Path(self.dest + '/table_' + str(index + 1) + '.csv')
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            
            for tr in table:
                csvwriter.writerow(tr)

    def get_html(self, url):
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')

if __name__ == '__main__':
    argc = len(sys.argv)

    if argc <= 1:
        print('Usage: python3 table2csv.py URL [DESTINATION_PATH]')
        
        sys.exit()

    Table2CSV(*sys.argv[1:])
