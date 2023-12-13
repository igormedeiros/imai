from autogen.core import AutoGen

class FeedbackManager:
    def __init__(self):
        self.feedbacks = {}
        self.autogen = AutoGen()  # Inicializa o AutoGen

    def add_feedback(self, task_id, feedback):
        if task_id not in self.feedbacks:
            self.feedbacks[task_id] = []
        self.feedbacks[task_id].append(feedback)

    def process_feedback(self):
        for task_id, feedbacks in self.feedbacks.items():
            for feedback in feedbacks:
                # Aqui você pode implementar lógica específica para analisar o feedback
                # e criar ou ajustar tarefas no AutoGen conforme necessário
                if "ajuste" in feedback:
                    self.adjust_task(task_id, feedback)
                elif "nova tarefa" in feedback:
                    self.create_new_task(feedback)

    def adjust_task(self, task_id, feedback):
        # Implement the logic to adjust an existing task based on feedback
        # For example, modify the parameters of the task in AutoGen
        new_params = self.analyze_feedback(feedback)  # Analyze feedback to get new parameters
        self.autogen.modify_task(task_id, new_params)

    def create_new_task(self, feedback):
        # Implement the logic to create a new task based on feedback
        # For example, create a new task in AutoGen based on the information from the feedback
        task_description = self.extract_task_from_feedback(feedback)  # Extract task description from feedback
        new_task_id = self.autogen.create_task(task_description)
        return new_task_id


    def get_feedback_for_task(self, task_id):
        return self.feedbacks.get(task_id, [])
