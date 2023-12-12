class FeedbackManager:
    def __init__(self):
        self.feedback_records = {}

    def collect_feedback(self, task_id, user_input):
        # Armazena o feedback do usuário para um determinado ID de tarefa
        if task_id not in self.feedback_records:
            self.feedback_records[task_id] = []
        self.feedback_records[task_id].append(user_input)

    def get_feedback(self, task_id):
        # Retorna o feedback para um determinado ID de tarefa, se existir
        return self.feedback_records.get(task_id, None)

    def remove_feedback(self, task_id):
        # Remove o feedback associado a um ID de tarefa específico
        if task_id in self.feedback_records:
            del self.feedback_records[task_id]

    def get_all_feedback(self):
        # Retorna todos os registros de feedback
        return self.feedback_records

    def summarize_feedback(self):
        # Resumo de todos os feedbacks coletados (pode ser expandido para uma análise mais detalhada)
        summary = {}
        for task_id, feedback_list in self.feedback_records.items():
            summary[task_id] = {
                "count": len(feedback_list),
                "feedback": feedback_list
            }
        return summary

    def user_requested_exit(self):
        # Verifica se algum feedback de usuário indica um pedido de encerramento
        for feedback_list in self.feedback_records.values():
            if any("TERMINATE" in feedback for feedback in feedback_list):
                return True
        return False
