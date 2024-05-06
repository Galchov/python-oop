from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        for task_obj in self.tasks:
            if task_obj.name == task.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task_obj in self.tasks:
            if task_obj.name == task_name:
                task_obj.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks_count = 0
        for task_obj in self.tasks:
            if task_obj.completed:
                self.tasks.remove(task_obj)
                completed_tasks_count += 1
        return f"Cleared {completed_tasks_count} tasks."

    def view_section(self):
        print_info = [f"Section {self.name}:"]
        for task_obj in self.tasks:
            print_info.append(task_obj.details())
        return "\n".join(print_info)


# Test code:
task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

