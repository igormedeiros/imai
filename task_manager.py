from autogen.core import AutoGen

class TaskManager:
    def __init__(self):
        self.autogen = AutoGen()
        self.tasks = {}
        self.completed_tasks = set()

    def delegate_task(self, agent_name, task_description):
        # Cria uma tarefa para o AutoGen
        task_id = self.autogen.create_task(agent_name, task_description)
        self.tasks[task_id] = {
            "agent": agent_name,
            "description": task_description,
            "status": "pending"
        }

    def update_task_progress(self):
        # Atualiza o progresso das tarefas através do AutoGen
        for task_id in list(self.tasks):
            status = self.autogen.get_task_status(task_id)
            self.tasks[task_id]["status"] = status
            if status == "completed":
                self.complete_task(task_id)

    def complete_task(self, task_id):
        # Processa uma tarefa completada
        result = self.autogen.get_task_result(task_id)
        self.save_task_result(task_id, result)
        self.completed_tasks.add(task_id)
        del self.tasks[task_id]

    def save_task_result(self, task_id, result):
        # Salva o resultado da tarefa em um arquivo
        filename = f"task_result_{task_id}.txt"
        with open(filename, 'w') as file:
            file.write(result)
        print(f"Resultado da tarefa {task_id} salvo em {filename}")

    def all_tasks_completed(self):
        # Verifica se todas as tarefas foram concluídas
        return not self.tasks
