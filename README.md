## HTMLTable2CSV

HTMLTable2CSV is a package for transforming HTML tables in a WebPage to CSV files.

### Install

```
pip install htmltable2csv
```

### Usage

##### 1. Using as a package inside a project.

```
from htmltable2csv.htmltable2csv import Table2CSV

Table2CSV('http://example.com/page.html', 'csvfiles')
```

It will parse all the HTML tables in http://example.com/page.html and store theme in csvfiles folder.


##### 2. Using as a utility from command line.

```
python3 -m  htmltable2csv.htmltable2csv 'http://example.com/page.html' 'csvfiles'

```
It will parse all the HTML tables in http://example.com/page.html and store theme in csvfiles folder of current directory.
