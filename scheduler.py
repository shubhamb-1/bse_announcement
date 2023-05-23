from apscheduler.schedulers.background import BackgroundScheduler
from scrap import fetch_new_data

scheduler = BackgroundScheduler()

def scheduler_function():
    jobs = scheduler.get_jobs()
    if not jobs:
        scheduler.add_job(fetch_new_data, 'interval', seconds=30)
        scheduler.start()
    scheduler.print_jobs()