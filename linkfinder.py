from urllib import parse
from html.parser import HTMLParser

class linkFinder(HTMLParser):
    
    def __init__(self , base_url ,page_url):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.links=set()
        
        
    def handle_starttag(self,tag,attr):
        if tag == 'a':
            for (attribute , value) in attr:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url , value)
                    self.links.add(url)
                    
    def get_links(self):
        return self.links
        
        
    def error(self , message):
        pass