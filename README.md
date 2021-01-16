# Parallel-Python

## 실습환경
- https://www.packtpub.com/product/parallel-programming-with-python/9781783288397
- Language : Python 3.6
- Tool : Visual-Studio-Code

## 병렬 프로그래밍에서의 통신
- 공유 상태(shared state)
- 메세지 전달: 실행중인 프로세스에서 메세지를 교환하는 메커니즘으로 구성된다.
  '''
  1. 공유 상태와 달리 데이터 접근이 동시에 발생하지 않는다.
  2. 로컬이나 분산 환경에서 메세지를 교환할 수 있다.
  '''

## 병렬 프로그래밍의 문제점
- 교착 상태(deadlock): 무한 대기 상태를 뜻하며 두 개 이상의 작업이 서로 상대방의 작업이 끝나기 만을 기다리고 있기 때문에 다음 단계로 진행하지 못하는 상태
                     한정된 자원을 여러 곳에서 사용하려고 할 때 발생

- 기아 상태(starvation): 특정 프로세스의 우선 순위가 낮아서 원하는 자원을 계속 할당받지 못하는 상태

- 차이점
  '''
  교착상태 : 여러 프로세스가 동일 자원 점유를 요청할 때 발생
  기아상태 : 여러 프로세스가 부족한 자원을 점유하기 위해 경쟁할 때 발생
  '''

- 기아상태의 해결방안
  '''
  1. 프로세스 우선순위 수시 변경을 통해 각 프로세스 높은 우선순위를 가지도록 기회 부여
  2. 오래 기다린 프로세스의 우선순위 높이기
  3. 우선순위가 아닌 요청 순서대로 처리하는 요청큐 사용
  '''

## Python 병렬 프로그래밍 모듈
- threading: 스레드에 기반을 둔 병렬 API 제공
  > 공식 홈페이지: https://docs.python.org/3/library/threading.html

- multiprocessing: 프로세스 기반을 둔 병렬 API 제공
  > 공식 홈페이지: https://docs.python.org/3/library/multiprocessing.html

- Paralle Python: 프로세스 방식을 사용할 수 있는 병렬과 분산 시스템을 위한 API 제공
  > 공식 홈페이지: https://www.parallelpython.com/

- Celery: 분산 시스템을 생성할 떄 사용
  > 동시성 형태로 태스크를 실행하는 세 가지 방식 중 하나를 활용
    1. 다중처리(multiprocessing)
    2. 이벤트 렛(Eventlet)
    3. 게벤트(Gevent)
  > 공식 홈페이지: https://docs.celeryproject.org/en/stable/

## 병렬 알고리즘 설계
- 분할 정복 기법
  > 복잡한 문제의 단위를 발견하고 해결할때까지 영역을 재귀적으로 쪼개서 해결하는 기법
    - 병합정렬(merge sort)와 빠른 정렬(quick sort)같은 정렬 알고리즘을 사용해 해결할 수 있다.

- 데이터 분해 사용
  > 입력 데이터에 대해 분해한 후 여러 작업자가 동시에 실행하여 해결하는 기법
    - ex) 행렬 곱

- 파이프라인으로 태스크 분해
  > 큰 태스크를 병렬 방식으로 실행하는 더 작은 독립적인 태스크로 나누어 해결하는 기법
    - ex) 자동차 공장 조립라인

## 프로세스 간 통신 이해
- IPC(interprocess communication): 프로세스 사이에 정보를 교환
  '''
  1. 동일한 머신에서 실행하는 곳일 경우 여러가지 방법이 있음(공유 메모리, 메세지 큐, 파아프) 
  2. 분산환경일 경우(소켓, 원격프로시저 호출(RPC-Remote Procedure Call))         
  '''

- 네임드 파이프: 파일 디스크립터 사용을 통한 IPC 통신(Python에서 시스템 콜을 통해 구현된다.)
  > ex) 데이터를 쓰고 읽기 위한 선입, 선출 구조를 들 수 있다.

## 분산 시스템 모듈
  - PP(Paralle Python): 로컬 프로세스뿐만 아니라 컴퓨터 네트워크를 통해 물리적으로 분산된 프로세스 간의 IPC를 구축하는 모듈
                      즉, 여러 PC에 분산처리 시키는 작업
    >장점
    1. 부하 분산을 개선하기 위해 프로세서 개수를 자동으로 감지
    2. 할당된 많은 프로세스를 실행 시간에 변경 가능
    3. 실행 시간에 부하 분산
    4. 네트워크를 통해 자원을 자동으로 발견
    > 두가지 방식으로 병렬 코드 실행을 구현할 수 있음.
    1. 동일한 머신안에 다중 프로세서/코어가 있는 SMP 아키텍처 구성
    2. 네트워크에서 머신을 통해 태스크 분산 구성(클러스터 형태)

  - Celery: PP와 동일한 개념

    >장점
    1. 인터넷에서 퍼진 작업자 사이나 로컬 작업자들에게 투명한 방법으로 태스크를 분산
    2. 설정을 통해 작업자의 동시성을 간단한 방법으로 변경(프로세스, 스레드, 게벤트, 이벤트렛)
    3. 동기식, 비동기식, 주기식, 태스트 스케줄링을 지원
    4. 오류가 났을 때 태스크를 다시 실행  

    >구성
    - Task: 모든 호출 가능한 작업(동기식, 비동기식, 주기식, 스케줄링) - @app.task
      - https://docs.celeryproject.org/en/stable/userguide/tasks.html
    - Broker: 브로커를 통해 메세지를 주고 받고 작업자와 통신한다.(태스크 큐) - RabbitMQ, Redis
    - Worker: Broker의 태스크 큐에 있는 작업을 실행하는 역할
      - https://docs.celeryproject.org/en/stable/userguide/workers.html
    - Result Back: 태스크의 상태와 결과를 저장하고, 클라이언트 애플리케이션에 결과를 반환하는 역할
      - https://docs.celeryproject.org/en/stable/userguide/configuration.html#std-setting-result_backend

## 비동기 프로그래밍
  - asyncio 모듈      