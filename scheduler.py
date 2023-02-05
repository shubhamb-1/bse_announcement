from apscheduler.schedulers.background import BackgroundScheduler
from scrap import fetch_new_data
from logic import move_from_cache

scheduler = BackgroundScheduler()

def scheduler_function():
    scheduler.add_job(fetch_new_data, 'interval', seconds=60)
    scheduler.add_job(move_from_cache, 'interval', hours = 1)
    scheduler.start()
    scheduler.print_jobs()