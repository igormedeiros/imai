import os
from PyPDF2 import PdfReader
from docx import Document

def read_project_specification(file_path):
    file_extension = os.path.splitext(file_path)[1]

    if file_extension in ['.txt', '.md']:
        with open(file_path, 'r') as file:
            project_data = file.read()
    elif file_extension == '.pdf':
        project_data = read_pdf(file_path)
    elif file_extension in ['.doc', '.docx']:
        project_data = read_word_document(file_path)
    else:
        raise ValueError(f"Formato de arquivo não suportado: {file_extension}")

    return project_data

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ''.join([page.extract_text() for page in reader.pages])
    return text

def read_word_document(file_path):
    document = Document(file_path)
    text = '\n'.join([para.text for para in document.paragraphs])
    return text

def parse_project_data(project_data):
    # Exemplo: Extrair título, objetivos e descrição de um projeto
    lines = project_data.split('\n')
    title = lines[0]  # Assumindo que o título está na primeira linha
    objectives = lines[1]  # Assumindo que os objetivos estão na segunda linha
    description = ' '.join(lines[2:])  # Resto do texto como descrição
    return {"title": title, "objectives": objectives, "description": description}
