#!/bin/bash

# OLLAMA

# Inicia o server ollama
ollama serve &

# Baixa e executa os modelos

# Data Scientist ou AI Engineer
ollama run mistral &

# Backend Developer, DevOps Engineer ou Code Reviewer
ollama run codellama &

# UI/UX Designer ou um agente de Suporte ao Cliente
ollama run starling-lm &

# Product Owner ou Scrum Master
ollama run neural-chat &

# QA Tester ou Documenter​
ollama run orca-mini &

# Software Architect ou Security Engineer
ollama run llama2 &

# Developer especialista em python
ollama run wizardcoder &

# Developer especialista em sql
ollama run sqlcoder &


# Litellm - expôe como API os modelos em uma porta

# http://0.0.0.0:8031
litellm --model ollama/mistral --port 8031 & 

# http://0.0.0.0:8032
litellm --model ollama/codellama --port 8032 &

# http://0.0.0.0:8033
litellm --model ollama/starling-lm --port 8033 & 

# http://0.0.0.0:8034
litellm --model ollama/neural-chat --port 8034 & 

# http://0.0.0.0:8035
litellm --model ollama/run orca-mini --port 8035 & 

# http://0.0.0.0:8036
litellm --model ollama/llama2 --port 8036 & 

# http://0.0.0.0:8037
litellm --model ollama/wizardcoder --port 8037 & 

# http://0.0.0.0:8038
litellm --model ollama/sqlcoder --port 8038 & 

