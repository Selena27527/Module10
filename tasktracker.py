from schooltasks import SchoolTasks
class TaskTracker(SchoolTasks):
  def __init__(self, task_type):
    super().__init__(self)
    self.task_type = task_type
    def clearTaskList(self):
        self._task_list.clear()
        def removeTask(self, task):
            for i, task_item in enumerate(self._task_list):
                if isinstance(task_item, tuple) and len(task_item) == 3:
                    date, task_desc, complete_date = task_item
                    if task == task_desc:
                        del self._task_list[i]
                        return
                    print(f"Task '{task}' not found.")
        def _str__(self):
         string = self.task_type + "\n"
        for index, task_item in enumerate(self.task_list, start=1):
            if isinstance(task_item, tuple):
                string += f"task{index}. {task_item[0]}: {task_item[1]}\n"
            else:
                string += f"task{index} Task: {task_item}" 
        return string