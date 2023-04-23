from apscheduler.schedulers.background import BackgroundScheduler
from scrap import fetch_new_data

scheduler = BackgroundScheduler()

def scheduler_function():
    scheduler.add_job(fetch_new_data, 'interval', seconds=30)
    scheduler.start()
    scheduler.print_jobs()