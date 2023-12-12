import autogen
from autogen.llm_config import LLMConfig

# Funções utilitárias para a criação de configurações de LLM
def create_config_list(port):
    return [
        {
            'base_url': f"http://0.0.0.0:{port}",
            'api_key': "NULL"
        }
    ]

def create_llm_config(config_list):
    return {
        "cache_seed": 42, 
        "temperature": 0,
        "config_list": config_list,
    }

# Criando as listas de configuração para os diferentes modelos
config_list_mistral = create_config_list(8031)
config_list_codellama = create_config_list(8032)
config_list_starling_lm = create_config_list(8033)
config_list_neural_chat = create_config_list(8034)
config_list_orca_mini = create_config_list(8035)
config_list_llama2 = create_config_list(8036)
config_list_wizardcoder = create_config_list(8037)
config_list_sqlcoder = create_config_list(8038)

# Criando as configurações LLM
llm_config_mistral = create_llm_config(config_list_mistral)
llm_config_codellama = create_llm_config(config_list_codellama)
llm_config_starling_lm = create_llm_config(config_list_starling_lm)
llm_config_neural_chat = create_llm_config(config_list_neural_chat)
llm_config_orca_mini = create_llm_config(config_list_orca_mini)
llm_config_llama2 = create_llm_config(config_list_llama2)
llm_config_wizardcoder = create_llm_config(config_list_wizardcoder)
llm_config_sqlcoder = create_llm_config(config_list_sqlcoder)