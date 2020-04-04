from html.parser import HTMLParser

class TableParser(HTMLParser):
    def __init__(self):
        super(TableParser, self).__init__(convert_charrefs=True)

        self.init_parser_state()
        
    def init_parser_state(self):
        self.tables = []
        self.intable = False
        self.inrow = False
        self.tindex = []
        self.rindex = -1
        self.data = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.handle_table_starttag(tag, attrs)

        if self.intable and tag == 'tr':
            self.handle_table_tr_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag == 'table':
            self.handle_table_endtag(tag)
        
        if tag == 'tr':
            self.handle_table_tr_endtag(tag)
        
        if tag == 'td' or tag == 'th':
            self.handle_table_tdth_endtag(tag)

    def handle_data(self, data):
        tag = self.get_starttag_text()
        
        if not self.inrow:
            return

        if tag == '<th>' or tag == '<td>':
            self.data += data

    def handle_table_starttag(self, tag, attrs):
        self.intable = True
        self.rindex = -1
        self.tindex = -1
        self.tables.append([])
    
    def handle_table_endtag(self, tag):
        self.intable = False
        self.tindex -= 1

    def handle_table_tr_starttag(self, tag, attrs):
        self.inrow = True
        self.rindex += 1
        self.tables[self.tindex].append([])
    
    def handle_table_tr_endtag(self, tag):
        self.inrow = False

    def handle_table_tdth_endtag(self, tag):
        self.tables[self.tindex][self.rindex].append(self.data.strip())
        self.data = ''
