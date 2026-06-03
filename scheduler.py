import schedule
import time

from scripts.main import main

# schedule.every().day.at("08:00").do(main)
schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(60)