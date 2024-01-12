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
    








def main():
    print('Welcome to the Project Manager')
    print('What would you like to do?')
    print('1. Create a new project')
    print('2. View existing projects')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        create_project()
    elif choice == '2':
        view_projects()
    elif choice == '3':
        return None
    
    
