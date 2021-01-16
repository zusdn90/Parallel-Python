import sys, time, random, re, requests
import concurrent.futures

from multiprocessing import Queue, cpu_count, current_process, Manager

# 동기화된 큐로부터 URL를 추출해 result_dict 넣는다.
def group_urls_task(urls, result_dict, html_link_regex):
    try:
        url = urls.get(True, 0.05)
        result_dict[url] = None
        print("[%s] putting url [%s] in dictionary..." % (
            current_process().name, url))
    except queue.Empty:
        print('Nothing to be done, queue is empty')
    
# 페이지의 링크 수집   
def crawl_task(url, html_link_regex):
    links = []
    try:
        request_data = requests.get(url)
        print("[%s] crawling url [%s] ..." % (
            current_process().name, url))
        links = html_link_regex.findall(request_data.text)
    except:
        print(sys.exc_info())
        raise
    finally:
        return (url, links) 


if __name__ == '__main__':
    manager = Manager()
    urls = manager.Queue()
    urls.put('http://www.google.com')
    urls.put('http://br.bing.com/')
    urls.put('https://duckduckgo.com/')
    urls.put('https://github.com/')
    urls.put('http://br.search.yahoo.com/')
    result_dict = manager.dict()
    
    html_link_regex = \
        re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')
    
    number_of_cpus = cpu_count()
    
    # ProcessPoolExecutor사용함으로써 GIL 문제를 해결
    # GIL(Global Interpreter lock) - 인터프리터 언어에서 스레드 실행을 동기화하여 한번에 하나의 원시 스레드만 실핼 가능. 
    with concurrent.futures.ProcessPoolExecutor(max_workers=number_of_cpus) as group_link_processes:
        for i in range(urls.qsize()):
            group_link_processes.submit(group_urls_task, urls, result_dict, html_link_regex)
            
    with concurrent.futures.ProcessPoolExecutor(max_workers=number_of_cpus) as crawler_link_processes:
        future_tasks = {crawler_link_processes.submit(crawl_task, url, html_link_regex): url for url in result_dict.keys()}
        for future in concurrent.futures.as_completed(future_tasks):
            result_dict[future.result()[0]] = future.result()[1]        
            
    for url, links in result_dict.items():
        print("[%s] with links : [%s..." % (url, links[0]))        
    
            