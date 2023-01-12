# 개요
* fastapi + celery 예제
* celery broker는 filesytem 사용
* 파이썬 3.7이상 필요
* 현재 테스트중

# 실행방법
```bash
pip install -r requirements.txt

# fastapi 실행
uvicorn main:app

# celeroy worker 실행
celery -A tasks worker --concurrency=1 --loglevel=info
celery -A worker:celery worker --concurrency=1 --loglevel=info
```

# 참고자료
* celery filesystem: https://www.distributedpython.com/2018/07/03/simple-celery-setup/
* https://github.com/mossadnik/celery-example-local-filesystem
* https://testdriven.io/blog/fastapi-and-celery/
* https://github.com/bstiel/celery-filesystem-broker/tree/master/app
* chatgpt
