class Project:
    def __init__(self, name, pathway, objectives, technologies):
        self.name = name
        self.objectives = objectives
        self.technologies = technologies
        self.pathway = pathway

    def add_task(self, task):
        self.pathway.append(task)

    def get_tasks(self):
        return self.pathway

    def __str__(self):
        project_info = f'Project Name: {self.name}\nObjectives: {self.objectives}\nTechnologies: {self.technologies}\nPathway:\n'
        for task in self.pathway:
            project_info += str(task) + '\n'
        return project_info

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True
    def mark_incomplete(self):
        self.completed = False

    def add_description(self, description):
        self.description = description
    

    def __str__(self):
        status = 'Completed' if self.completed else 'Not Completed'
        return f'Task: {self.description}, Status: {status}'
    
class ProjectManager:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_projects(self):
        return self.projects

    def __str__(self):
        project_info = ''
        for project in self.projects:
            project_info += str(project) + '\n'
        return project_info
    
class Objective:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True
    def mark_incomplete(self):
        self.completed = False

    def add_description(self, description):
        self.description = description

    def __str__(self):
        status = 'Completed' if self.completed else 'Not Completed'
        return f'Objective: {self.description}, Status: {status}'
    
class Objectives:
    def __init__(self):
        self.objectives = []

    def add_objective(self, objective):
        self.objectives.append(objective)
    
    def remove_objective(self, objective):
        self.objectives.remove(objective)

    def get_objectives(self):
        return self.objectives

    def __str__(self):
        objective_info = ''
        for objective in self.objectives:
            objective_info += str(objective) + '\n'
        return objective_info
    
class Technology:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def add_description(self, description):
        self.description = description
    
    def __str__(self):
        return f'Technology: {self.name}, Description: {self.description}'
    
## Classes end here
    

## Functions start here
    
def add_task_to_project(project_manager):
    project_name = input("\nEnter the name of the project to add a task: ")
    project = next((p for p in project_manager.get_projects() if p.name == project_name), None)

    if project is None:
        print(f"No project found with the name '{project_name}'")
        return

    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    new_task = Task(task_title, task_description)
    project.add_task(new_task)
    print(f"Task added to project '{project_name}'.\n")

def update_status(project_manager, item_type="task"):
    project_name = input(f"\nEnter the name of the project to update a {item_type}: ")
    project = next((p for p in project_manager.get_projects() if p.name == project_name), None)

    if project is None:
        print(f"No project found with the name '{project_name}'")
        return

    item_title = input(f"Enter the {item_type}'s title to update: ")
    for item in getattr(project, item_type + 's'):
        if item.title == item_title:
            item.mark_completed() if item_type == "task" else item.mark_incomplete()
            print(f"{item_type.capitalize()} '{item_title}' status updated.\n")
            return

    print(f"{item_type.capitalize()} with title '{item_title}' not found in project '{project_name}'.")

def list_tasks_in_project(project_manager):
    project_name = input("\nEnter the name of the project to list tasks: ")
    project = next((p for p in project_manager.get_projects() if p.name == project_name), None)

    if project is None:
        print(f"No project found with the name '{project_name}'")
        return

    if not project.get_tasks():
        print("No tasks found in this project.")
        return

    print("\nTasks in Project:")
    for task in project.get_tasks():
        print(task)

def update_technology_description(project_manager):
    project_name = input("\nEnter the name of the project to update technology: ")
    project = next((p for p in project_manager.get_projects() if p.name == project_name), None)

    if project is None:
        print(f"No project found with the name '{project_name}'")
        return

    tech_name = input("Enter the name of the technology to update: ")
    for tech in project.technologies:
        if tech.name == tech_name:
            new_description = input("Enter new description for the technology: ")
            tech.add_description(new_description)
            print(f"Technology '{tech_name}' description updated in project '{project_name}'.\n")
            return

    print(f"Technology '{tech_name}' not found in project '{project_name}'.")



def view_projects(project_manager):
    print("\n-- Existing Projects --")
    if not project_manager.get_projects():
        print("No projects found.")
        return

    for project in project_manager.get_projects():
        print(project)


def create_project(project_manager):
    print("\n-- Create a New Project --")
    name = input("Enter project name: ")
    objectives = input("Enter project objectives (comma-separated): ").split(',')
    technologies_input = input("Enter technologies used (comma-separated): ").split(',')

    objectives_list = [Objective(name.strip(), "") for name in objectives]
    tech_list = [Technology(name.strip(), "") for name in technologies_input]

    new_project = Project(name, [], objectives_list, tech_list)
    project_manager.add_project(new_project)
    print(f"Project '{name}' created successfully!\n")




#main function

def main():
    project_manager = ProjectManager()

    while True:
        print('\nWelcome to the Project Manager')
        print('1. Create a new project')
        print('2. View existing projects')
        print('3. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            create_project(project_manager)
        elif choice == '2':
            view_projects(project_manager)
        elif choice == '3':
            print("Exiting Project Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


