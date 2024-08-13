
# task_scheduler.py

import logging
import time
import schedule

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/WorkflowAutomation/Logs/workflow.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def task():
    """
    The task to be scheduled and executed.
    """
    logging.info("Scheduled task executed.")
    print("Scheduled task executed.")

def schedule_task(interval, unit):
    """
    Schedules a task to be executed at a specified interval.
    Args:
        interval (int): The interval at which to execute the task.
        unit (str): The time unit ('seconds', 'minutes', 'hours', 'days').
    """
    try:
        if unit == 'seconds':
            schedule.every(interval).seconds.do(task)
        elif unit == 'minutes':
            schedule.every(interval).minutes.do(task)
        elif unit == 'hours':
            schedule.every(interval).hours.do(task)
        elif unit == 'days':
            schedule.every(interval).days.do(task)
        else:
            logging.error("Invalid time unit for scheduling.")
            print("Invalid time unit for scheduling.")
            return False

        logging.info(f"Task scheduled to run every {interval} {unit}.")
        print(f"Task scheduled to run every {interval} {unit}.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    except Exception as e:
        logging.error(f"Error in scheduling task: {e}")
        print(f"Error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    schedule_task(5, 'seconds')
