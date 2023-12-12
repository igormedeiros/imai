from agents import get_agents
from feedback_manager import FeedbackManager
from task_manager import TaskManager
from project_specification import read_project_specification, parse_project_data

def main():
    # Inicializa as classes de gerenciamento
    task_manager = TaskManager()
    feedback_manager = FeedbackManager()

    # Obtém os agentes
    agents = get_agents()

    # Define a tarefa inicial (ajuste este trecho conforme a lógica do seu projeto)
    initial_task = "count 1 to 100"  # Substitua com a descrição da tarefa inicial apropriada


    # Delega a tarefa inicial ao agente apropriado
    task_manager.delegate_task('Product Owner', initial_task)

    # Inicializa uma variável para rastrear se pelo menos uma rodada de processamento ocorreu
    first_round_completed = False

    # Loop for interaction and task management
    while True:
        # Verifica o status de todas as tarefas e simula o progresso
        for agent_name in agents:
            status = task_manager.check_task_status(agent_name)
            print(f"Task status of agent {agent_name}: {status}")

        task_manager.simulate_task_progress()  # Simula o progresso da tarefa

        # Marca que a primeira rodada de processamento ocorreu
        first_round_completed = True

        # Coleta feedback do usuário após a primeira rodada de processamento
        if first_round_completed:
            user_feedback = input("Enter your feedback: ")  # Coleta feedback do usuário
            if user_feedback:
                task_id = task_manager.get_current_task_id(agent_name)  # Obtém o ID da tarefa atual
                feedback_manager.add_feedback(task_id, user_feedback)

            # Analisa o feedback e gera novas tarefas, se necessário
            for task_id in feedback_manager.get_all_feedback():
                if feedback_manager.has_new_feedback(task_id):
                    new_tasks = feedback_manager.analyze_feedback_and_generate_tasks(task_id)
                    for agent_name, new_task in new_tasks.items():
                        task_manager.delegate_task(agent_name, new_task)
                    feedback_manager.mark_feedback_as_read(task_id)

        # Condição de saída (pode ser modificada conforme necessário)
        if task_manager.all_tasks_completed() or feedback_manager.user_requested_exit():
            print("All tasks have been completed or user requested termination.")
            break

        # Imprime relatório de tarefas
        print(task_manager.get_task_report())

# Executa a função principal se o script for o ponto de entrada
if __name__ == "__main__":
    main()
