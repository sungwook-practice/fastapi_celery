from worker import celery
import random
import time
from celery import shared_task


@shared_task
def long_running_task():
  print("===== celery worker triggerd =====")

  time.sleep(10)
  n = 100000
  total = 0
  for i in range(0, n):
      total += random.randint(1, 1000)

  print("===== celery worker triggerd =====")

  return total / n

