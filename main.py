from agents import get_agents
from feedback_manager import FeedbackManager
from task_manager import TaskManager

def main():
    task_manager = TaskManager()
    feedback_manager = FeedbackManager()
    agents = get_agents()

    # Delega uma tarefa inicial ao AutoGen através do Product Owner
    initial_task_description = "Create a Python file to count from 1 to 100"
    task_manager.delegate_task('Product Owner', initial_task_description)

    while True:
        # Atualiza o progresso das tarefas no AutoGen
        task_manager.update_task_progress()

        # Verifica o status de todas as tarefas atribuídas no AutoGen
        for agent_name in agents:
            task_id = task_manager.get_current_task_id(agent_name)
            if task_id:
                status = task_manager.get_task_status(task_id)
                print(f"Task status of agent {agent_name}: {status}")
            else:
                print(f"Task status of agent {agent_name}: Nenhuma tarefa atribuída")

        # Coleta e processa feedback do usuário
        if not task_manager.all_tasks_completed():
            user_feedback = input("Enter your feedback: ")
            if user_feedback:
                # Supondo que o feedback esteja relacionado à tarefa do Scrum Master
                task_id = task_manager.get_current_task_id('Scrum Master')
                if task_id:
                    feedback_manager.process_feedback(task_id, user_feedback)

        # Verifica se todas as tarefas no AutoGen foram concluídas
        if task_manager.all_tasks_completed():
            print("All tasks have been completed.")
            break

        # Imprime o relatório das tarefas geridas pelo AutoGen
        print(task_manager.get_task_report())

if __name__ == "__main__":
    main()
