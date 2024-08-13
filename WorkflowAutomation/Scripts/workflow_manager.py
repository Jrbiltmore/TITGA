
# workflow_manager.py

import logging

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/WorkflowAutomation/Logs/workflow.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def manage_workflow(task_list):
    """
    Manages and executes a list of tasks in sequence.
    Args:
        task_list (list): A list of functions representing tasks to be executed.
    Returns:
        bool: True if all tasks are executed successfully, False otherwise.
    """
    try:
        for task in task_list:
            task_name = task.__name__
            logging.info(f"Starting task: {task_name}")
            print(f"Starting task: {task_name}")
            task()
            logging.info(f"Completed task: {task_name}")
            print(f"Completed task: {task_name}")

        logging.info("All tasks completed successfully.")
        print("All tasks completed successfully.")
        return True

    except Exception as e:
        logging.error(f"Error in managing workflow: {e}")
        print(f"Error: {e}")
        return False

# Example tasks
def example_task_1():
    print("Executing Task 1")

def example_task_2():
    print("Executing Task 2")

# Example usage
if __name__ == "__main__":
    tasks = [example_task_1, example_task_2]
    manage_workflow(tasks)
