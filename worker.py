from celery import Celery

celery = Celery(__name__)
celery.conf.update({
  "broker_url": "filesystem://",
  "broker_transport_options": {
    "data_folder_in": "./broker/in",
    "data_folder_out": "./broker/out",
    "data_folder_processed": "./broker/processed"
  },
  "imports": ("tasks",),
  "result_persistent": False,
  "task_serializer": "json",
  "result_serializer": "json",
  "accept_content": ["json"]
})

