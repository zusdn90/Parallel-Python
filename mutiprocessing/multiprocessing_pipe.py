import os, random
from multiprocessing import Process, Pipe

def producer_task(conn):
    value = random.randint(1, 10)
    conn.send(value)
    print('Value [%d] sent by PID [%d]' % (value, os.getpid()))

def consumer_task(conn):   
    print('Value [%d] received by PID [%d]' % (conn.recv(), os.getpid()))
    
    
if __name__ == '__main__':
    producer_conn, consumer_conn = Pipe()
    consumer = Process(target=consumer_task, args=(consumer_conn,))
    producer = Process(target=producer_task, args=(producer_conn,))
    
    # 프로세스 실행 초기화
    consumer.start()
    producer.start()
    
    # 메인 프로세스가 생성된 프로세스(consumer, producer) 실행을 기다리는 역할
    consumer.join()
    producer.join()
    