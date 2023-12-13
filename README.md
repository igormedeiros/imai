# im.ai
Software Agency based on Multiple GenAI Models

Welcome to the im.ai project on GitHub! This software agency is focused on harnessing the power of Multiple GenAI Models to tackle various tasks. Below, you'll find detailed instructions on how to install and use our models.

## Installation Instructions

### Step 1 - Install OLLAMA
To get started, you'll need to install OLLAMA, our framework for managing and running GenAI Models. Follow these steps:

1. Download the LLM (Llama Language Models) from our repository.
```
curl https://ollama.ai/install.sh | sh
```

2. Start the OLLAMA server:

```
ollama serve &
```


### Step 2. Download and execute the specific models based on your role:

- For Data Scientists or AI Engineers Agents:
  ```
  ollama run mistral &
  ```

- For Backend Developers, DevOps Engineers, or Code Reviewers Agents:
  ```
  ollama run codellama &
  ```

- For UI/UX Designers or Customer Support Agents:
  ```
  ollama run starling-lm &
  ```

- For Product Owners or Scrum Masters Agents:
  ```
  ollama run neural-chat &
  ```

- For QA Testers or Documenters Agents:
  ```
  ollama run orca-mini &
  ```

- For Software Architects or Security Engineers Agents:
  ```
  ollama run llama2 &
  ```

- For Python Specialists Agents:
  ```
  ollama run wizardcoder &
  ```

- For SQL Specialists Agents:
  ```
  ollama run sqlcoder &
  ```

### Step 3 - Expose Models as API with Litellm 
To access the models via API, you can use Litellm. Here are the instructions:

1. Create and activate conda env
```
# create env
conda create -n autogen python=3.11
```
```
# activate env
conda activate autogen
```
#### 2. Install Litellm
```
pip install litellm
```

#### 3. Start Litellm for each model with the respective ports:

- Mistral Model:
  ```
  litellm --model ollama/mistral --port 8031 &
  ```

- Codellama Model:
  ```
  litellm --model ollama/codellama --port 8032 &
  ```

- Starling-lm Model:
  ```
  litellm --model ollama/starling-lm --port 8033 &
  ```

- Neural-Chat Model:
  ```
  litellm --model ollama/neural-chat --port 8034 &
  ```

- Orca-mini Model:
  ```
  litellm --model ollama/orca-mini --port 8035 &
  ```

- Llama2 Model:
  ```
  litellm --model ollama/llama2 --port 8036 &
  ```

- Wizardcoder Model:
  ```
  litellm --model ollama/wizardcoder --port 8037 &
  ```

- SQLcoder Model:
  ```
  litellm --model ollama/sqlcoder --port 8038 &
  ```

### Step 4 - Run the Application
To run the application, follow these instructions:

#### 1. Activate your Conda environment with Python 3.11:
```
conda activate myenv
```


#### 2. Run the main application:
```
python main.py
```


That's it! You've successfully installed and configured the im.ai project with Multiple GenAI Models. Feel free to explore and utilize these models for various tasks in your projects. If you have any questions or need assistance, don't hesitate to reach out to our support team.

Happy coding! 🚀
