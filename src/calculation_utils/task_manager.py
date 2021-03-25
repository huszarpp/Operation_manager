

class TaskManager(object):

    filename_to_log = None

    @staticmethod
    def set_filename_to_log(filename):
        TaskManager.filename_to_log = filename

    @staticmethod
    def execute_all_task(task_calculationlist_dict):
        for task, calculation_list in task_calculationlist_dict.items():
            current_task = task_calculationlist_dict[task]
            for calculation in current_task:
                calculation.calculate()
                print(calculation.result)
