# Parallel-Python

## 개발환경
- Language : Python 3.6
- Tool : Visual-Studio-Code


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
      : 병합정렬(merge sort)와 빠른 정렬(quick sort)같은 정렬 알고리즘을 사용해 해결할 수 있다.

  - 데이터 분해 사용
    > 입력 데이터에 대해 분해한 후 여러 작업자가 동시에 실행하여 해결하는 기법
      :ex) 행렬 곱

  - 파이프라인으로 태스크 분해
    > 큰 태스크를 병렬 방식으로 실행하는 더 작은 독립적인 태스크로 나누어 해결하는 기법
      :ex) 자동차 공장 조립라인
          