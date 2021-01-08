#coding: utf-8

import logging, threading

from queue import Queue

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fibo_dict = {}

# 피보나치 수열을 계산하는 스레드 사이에 공유된 데이터를 담는 컨테이너
# 각 스레드는 Queue 객체에 요소를 삽입한다.
shared_queue = Queue()
input_list = [3, 10, 5, 7] #simulates user input

# Condition - 특정 조건에 따라 자원 접근 시 동기화 하는 것이 목적
queue_condition = threading.Condition()

def fibonacci_task(condition):
    with condition:
        while shared_queue.empty():
            logger.info("[%s] - waiting for elements in queue..." % threading.current_thread().name)
            condition.wait()
        else:
            value = shared_queue.get()
            a, b = 0, 1
            
            for item in range(value):
                a, b = b, a + b
                fibo_dict[value] = a
            shared_queue.task_done()
            logger.debug("[%s] fibonacci of key [%d] with result [%d]" %
                (threading.current_thread().name, value, fibo_dict[value]))

# 스레드가 실행하는 함수이며, 처리된 요소를 shared_queue에 채우는 역할
def queue_task(condition):
    logging.debug('Starting queue_task...')
    
    with condition:
        for item in input_list:
            shared_queue.put(item)
        logging.debug("Notifying fibonacci_task threads that the queue is ready to consume..")
        
        # shared_queue에 모든 요소 삽입 후 피보나치 수열 계산 스레드에게 큐를 사용할 준비가 됐다고 통지
        condition.notifyAll()    

# 4개의 스레드집합 생성
threads = [threading.Thread(
            daemon=True, target=fibonacci_task, args=(queue_condition,)) for i in range(4)]                

# 스레드 시작
[thread.start() for thread in threads]

# shared_queue를 채우는 스레드 생성 후 시작
prod = threading.Thread(name='queue_task_thread', daemon=True, target=queue_task, args=(queue_condition,))
prod.start()

# join() main스레드가 다른 스레드 작업이 끝나기를 기다린다.
[thread.join() for thread in threads]
logger.info("[%s] - Result: %s" % (threading.current_thread().name, fibo_dict))