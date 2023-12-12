import os

def read_project_specification(file_path):
    file_extension = os.path.splitext(file_path)[1]

    if file_extension == '.txt':
        with open(file_path, 'r') as file:
            project_data = file.read()
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")

    return project_data

def parse_project_data(project_data):
    # Example: Extract title, objectives, and description of a project
    lines = project_data.split('\n')
    title = lines[0]  # Assuming the title is on the first line
    objectives = lines[1]  # Assuming the objectives are on the second line
    description = ' '.join(lines[2:])  # Rest of the text as description
    return {"title": title, "objectives": objectives, "description": description}
