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

    # Lê e analisa a especificação do projeto
    project_data = read_project_specification('specification/software_reqs.txt')
    parsed_data = parse_project_data(project_data)

    # Define a tarefa inicial com base na especificação do projeto
    initial_task = task_manager.define_initial_task(parsed_data)

    # Delega a tarefa inicial ao agente apropriado
    task_manager.delegate_task('Product Owner', initial_task)

    # Loop para interação e gerenciamento de tarefas
    while True:
        # Verifica o status de todas as tarefas e simula progresso
        for agent_name in agents:
            status = task_manager.check_task_status(agent_name)
            print(f"Status da tarefa do agente {agent_name}: {status}")

        task_manager.simulate_task_progress()  # Simula progresso das tarefas

        # Coleta feedback do usuário (implementação depende do mecanismo de entrada)
        user_feedback = feedback_manager.collect_feedback_from_user()
        if user_feedback:
            feedback_manager.collect_feedback('TaskID', user_feedback)

        # Analisa o feedback e gera novas tarefas, se necessário
        if feedback_manager.has_new_feedback('TaskID'):
            new_tasks = feedback_manager.analyze_feedback_and_generate_tasks('TaskID')
            for agent_name, new_task in new_tasks.items():
                task_manager.delegate_task(agent_name, new_task)

        # Condição de saída (pode ser modificada conforme necessário)
        if task_manager.all_tasks_completed() or feedback_manager.user_requested_exit():
            print("Todas as tarefas foram concluídas ou usuário solicitou encerramento.")
            break

        # Imprimir relatório de tarefas
        print(task_manager.get_task_report())

# Executa a função principal se o script for o ponto de entrada
if __name__ == "__main__":
    main()
