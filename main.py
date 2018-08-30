import threading
from queue import Queue
from spider import spider
from general import *
from domain import *

PROJECT_NAME=str(input('Enter Project name:'))
HOMEPAGE=str(input('Enter HOMEPAGE:'))
DOMAIN_NAME=get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME + '/queue.txt'
CRAWLED_FILE=PROJECT_NAME+'/crawled.txt'
queue = Queue()
spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
NUMBER_OF_THREADS=12

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon=True
        t.start()
        
def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.currentThread().name, url)
        queue.task_done()
        

def create_jobs():
    links=file_to_set(QUEUE_FILE)
    for url in links:
        queue.put(url)
    queue.join()
    crawl()
    
def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' items in queue')
        create_jobs()
        
create_workers()
crawl()
