import threading
import multiprocessing

def manage_parallel_tasks(task_list, use_multiprocessing=False):
    """
    Manages parallel tasks for performance optimization.

    Args:
        task_list (list): List of tasks to be executed in parallel.
        use_multiprocessing (bool): Flag to use multiprocessing instead of threading.

    Returns:
        None
    """
    if use_multiprocessing:
        processes = []
        for task in task_list:
            process = multiprocessing.Process(target=task)
            processes.append(process)
            process.start()
        
        for process in processes:
            process.join()
    else:
        threads = []
        for task in task_list:
            thread = threading.Thread(target=task)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
