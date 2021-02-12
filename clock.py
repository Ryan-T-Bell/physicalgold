from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from worker import conn

# my module
from gold_physical import get_all

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

sched = BlockingScheduler()

q = Queue(connection=conn)

def gather_gold_prices():
    q.enqueue(get_all)

sched.add_job(gather_gold_prices) #enqueue right away once
sched.add_job(gather_gold_prices, 'interval', minutes=10)
sched.start()
