# Table2CSV

Table2CSV is a package for transforming HTML tables in a WebPage to CSV files.


### Using as a package inside a project.

```
from table2csv.table2csv import Table2CSV

Table2CSV('http://example.com/page.html', 'csvfiles')
```

It will parse all the HTML tables in *http://example.com/page.html* and store theme in csvfiles directory.


### Using as a utility from command line.

```
python3 -m table2csv.table2csv 'http://example.com/page.html' 'csvfiles'
```
