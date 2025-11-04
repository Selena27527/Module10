from todo import Todo
class SchoolTasks(Todo):
    def __init__(self):
        super().__init__()
    def addTask(self, task_date, task):
        self._task_list.append((task_date, task))
    def _str__(self):
        string = ""
        for index, task_item in enumerate(self.task_list, start=1):
            if isinstance(task_item, tuple):
                string += f"task{index}. {task_item[0]}: {task_item[1]}\n"
            else:
                string += f"task{index} Task: {task_item}" 
        return string