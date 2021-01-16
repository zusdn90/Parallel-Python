import os, pp

input_list = [4, 3, 8, 6, 10]
result_dict = {}

"""
Python 2.x 버전 환경에서 실행가능
"""

"""
callback function
fibo_task함수가 실행 결과를 반환하자마자 콜백 함수를 호출한다.
"""
def aggregate_results(result):
    print "Computing results with PID [%d]" % os.getpid() 
    result_dict[result[0]] = result[1]

def fibo_task(value):
    a, b = 0, 1
    for item in range(value):
        a,b = b, a + b
        message = "the fibonacci calculated by pid %d was %d" \
        % (os.getpid(), a)
        
        return (value, message)

# Server() - task를 dispatch하는 역할    
job_server = pp.Server()
for item in input_list:
    # submit호출을 통해 fibo_task 함수를 디스패치 한다.
    job_server.submit(fibo_task, (item,), modules=('os',), callback=aggregate_results)

# 디스패치한 모든 태스크를 기다리는 역할
job_server.wait()

print "Main process PID [%d]" % os.getpid() 
for key, value in result_dict.items():
    print "For input %d, %s" % (key, value)    