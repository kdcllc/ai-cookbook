import os

from openai import OpenAI


def get_settings():
    if 'OPENAI_API_KEY' in os.environ and 'OPENAI_BASE_URL' in os.environ:
        api_key = os.environ['OPENAI_API_KEY']
        base_url = os.environ['OPENAI_BASE_URL']
        model_name = os.environ.get('OPENAI_MODEL_NAME', 'gpt-4o')    
    else:
        api_key = 'ollama'
        base_url = "http://localhost:11434/v1"
        model_name = 'llama3.1'

    client = OpenAI(api_key=api_key, base_url=base_url)
    return client, model_name
