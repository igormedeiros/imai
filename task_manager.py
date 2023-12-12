import random
import datetime

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.completed_tasks = {}
        self.task_progress = {}
        self.task_results = {}
        self.task_priority = {}
        self.task_changes_log = {}

    def define_initial_task(self, project_specification):
        initial_task = f"Análise Inicial: {project_specification}"
        return initial_task

    def delegate_task(self, agent_name, task, priority=5):
        self.tasks[agent_name] = task
        self.task_progress[agent_name] = 0
        self.task_priority[agent_name] = priority
        self.log_task_change(agent_name, "Tarefa delegada")
        return "Tarefa delegada"

    def cancel_task(self, agent_name):
        if agent_name in self.tasks:
            del self.tasks[agent_name]
            self.log_task_change(agent_name, "Tarefa cancelada")
            print(f"Tarefa do agente '{agent_name}' cancelada.")

    def log_task_change(self, agent_name, change):
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if agent_name not in self.task_changes_log:
            self.task_changes_log[agent_name] = []
        self.task_changes_log[agent_name].append((time_stamp, change))

    def simulate_task_progress(self):
        for agent in self.tasks:
            if self.task_progress[agent] < 100:
                self.task_progress[agent] += random.randint(5, 20)
                self.task_progress[agent] = min(self.task_progress[agent], 100)
                if self.task_progress[agent] == 100:
                    self.complete_task(agent)

    def complete_task(self, agent_name):
        self.completed_tasks[agent_name] = True
        result = f"Resultado da tarefa do agente '{agent_name}'"
        self.task_results[agent_name] = result
        self.log_task_change(agent_name, "Tarefa concluída")
        print(f"Tarefa do agente '{agent_name}' concluída com resultado: {result}")

    def get_overdue_tasks(self):
        # Implementar lógica para identificar tarefas atrasadas
        pass

    def update_task_details(self, agent_name, new_details):
        if agent_name in self.tasks:
            self.tasks[agent_name] = new_details
            self.log_task_change(agent_name, "Detalhes da tarefa atualizados")
            return "Detalhes da tarefa atualizados com sucesso"
        else:
            return "Agente não possui uma tarefa atribuída"

    def get_task_report(self):
        report = "Relatório de Tarefas:\n"
        for agent, task in self.tasks.items():
            status = self.check_task_status(agent)
            priority = self.task_priority.get(agent, "N/A")
            report += f"Agente: {agent}, Tarefa: {task}, Status: {status}, Prioridade: {priority}\n"
        return report
        
    def check_task_status(self, agent_name):
        if agent_name in self.completed_tasks:
            return "Concluída"
        elif agent_name in self.tasks:
            progress = self.task_progress[agent_name]
            if progress < 100:
                return f"Em progresso ({progress}% completo)"
            else:
                return "Aguardando confirmação de conclusão"
        else:
            return "Nenhuma tarefa atribuída"

    def get_current_task_id(self, agent_name):
        # Implement your logic here to get the current task ID
        pass

