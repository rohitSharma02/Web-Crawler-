from urllib.request import urlopen
from linkfinder import linkFinder
from general import *

class spider:
    
    base_url=''
    project_name=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue = set()
    crawled=set()
    
    def __init__(self,project_name,base_url,domain_name):
        spider.project_name=project_name
        spider.base_url=base_url
        spider.domain_name=domain_name
        spider.queue_file=spider.project_name+'/queue.txt'
        spider.crawled_file=spider.project_name+'/crawled.txt'
        self.boot()
        self.crawl_page('First spider' , spider.base_url)
    
    @staticmethod    
    def boot():
        create_project_directory(spider.project_name)
        create_data_files(spider.project_name , spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)
    
    @staticmethod    
    def crawl_page(thread_name , page_url):
        if page_url not in spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(spider.queue)) + ' | crawled '+ str(len(spider.crawled)) )
            spider.add_links_to_queue(spider.gather_links(page_url))
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.update_files()
    
    
    @staticmethod
    def gather_links(page_url):
        html_string=''
        possibleOutcomes=set(['text/html; charset=utf-8' , 'text/html' , 'text/html; charset=UTF-8'])
        try:
            response=urlopen(page_url)
            #print(str(response.info()))
            if response.getheader('Content-Type') in possibleOutcomes:
                html_byte = response.read()
                html_string= html_byte.decode('utf-8')
            finder=linkFinder(spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print('Error: can not crawl page')
            print(str(e))
            return set()
        return finder.get_links()
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue
            if spider.domain_name not in url:
                continue
            spider.queue.add(url)
   
    @staticmethod        
    def update_files():
        set_to_file(spider.queue , spider.queue_file)
        set_to_file(spider.crawled , spider.crawled_file)
        