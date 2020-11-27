import threading
from queue import Queue

from spider import Spider
from domain import *
from general import *

#constants
PROJECT_NAME="WebCrawler"
HOMEPAGE="https://algozenith.com/"
DOMAIN_COM=get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME+'/queue.txt'
CRAWLED_FILE=PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS=8

queue=Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_COM)

