def main():
    #The Todo Class
    from todo import Todo
    todo = Todo()
    todo.addTask("Make the bed")
    todo.addTask("Do homework")
    todo.addTask("Check emails")
    print(repr(todo))
    #The schoolTasks Class
    from Module10.schooltasks import SchoolTasks
    school = SchoolTasks()
    school.addTasks("11/04/2025", "Drink water")
    school.addTasks("11/04/2025,respond to emails")
    school.addtasks("11/04/2025""Study for exams")
    print(repr(school))
    print(school)

    #The TaskTracker Class
    from tasktracker import TaskTracker
    task_tracker = TaskTracker("Workout")
    task_tracker.addTask("11/01/2025,Deadlift")
    task_tracker.addTask("Ran 3 miles", "11/01/2025")
    task_tracker.addTask("11/01/2025", "Swim 50 laps")
    task_tracker.addTask("11/01/2025", "Hill Training")
    print(repr(task_tracker))
    task_tracker.remove_task("Deadlift")
    print(repr(task_tracker))
    print(str(task_tracker))

    #call generate_list
    generate_list(todo)
    generate_list(school)
    generate_list(task_tracker)

def generate_list(t, Todo):
    from todo import Todo
    if not isinstance(t, Todo):
        print("not Todo List")
        return NotImplemented
    print("Generate List Function")
    print(t)

                         



    main()