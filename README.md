## HTMLTable2CSV

HTMLTable2CSV is a package for transforming HTML tables in a WebPage to CSV files.

### Install

```
pip install htmltable2csv
```

### Usage

#### 1. Using as a package inside a project.

a) Fetch HTML content from a Web Page URL.

```
from htmltable2csv.htmltable2csv import Table2CSV

Table2CSV('http://example.com/page.html', '/path/to/destination')
```

It will parse all the HTML tables in http://example.com/page.html and store theme in specified destination folder.


b) Read HTML content from a html file in the specified path.

```
from htmltable2csv.htmltable2csv import Table2CSV

Table2CSV('/home/aqib/source.html', '/path/to/destination')
```

It will parse all the HTML tables in */home/aqib/source.html* file and store theme in specified destination folder.


#### 2. Using as a utility from command line.

a) Fetch HTML content from a Web Page URL.

```
python3 -m  htmltable2csv.htmltable2csv 'http://example.com/page.html' '/path/to/destination'

```

b) Read HTML content from a html file in the specified path.

```
python3 -m  htmltable2csv.htmltable2csv '/path/to/source.html' '/path/to/destination'

```
