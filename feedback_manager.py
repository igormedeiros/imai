class FeedbackManager:
    def __init__(self):
        # Dicionário para armazenar feedbacks, chave é o ID da tarefa e o valor é uma lista de feedbacks
        self.feedbacks = {}
        # Dicionário para rastrear se o feedback foi lido ou não
        self.feedback_read_status = {}

    def add_feedback(self, task_id, feedback):
        # Adiciona um novo feedback para uma tarefa específica
        if task_id not in self.feedbacks:
            self.feedbacks[task_id] = []
        self.feedbacks[task_id].append(feedback)
        # Marca o feedback mais recente como não lido
        self.feedback_read_status[task_id] = False

    def mark_feedback_as_read(self, task_id):
        # Marca todos os feedbacks para uma tarefa como lidos
        if task_id in self.feedback_read_status:
            self.feedback_read_status[task_id] = True

    def has_new_feedback(self, task_id):
        # Verifica se há feedbacks não lidos para uma tarefa específica
        return self.feedback_read_status.get(task_id, False)
    
    def get_all_feedback(self):
        # Retorna todos os IDs de tarefas para os quais há feedback
        return list(self.feedbacks.keys())