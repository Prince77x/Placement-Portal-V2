from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "placement_portal",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.beat_schedule = {
    "monthly-placement-report": {
        "task": "tasks.generate_all_placement_reports",
        "schedule": crontab(day_of_month=1, hour=0, minute=0)
    }
}