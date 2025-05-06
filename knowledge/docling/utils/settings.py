import os

from openai import AzureOpenAI, OpenAI


def get_settings():
    if 'OPENAI_API_KEY' in os.environ and 'OPENAI_BASE_URL' in os.environ:
        api_key = os.environ['OPENAI_API_KEY']
        base_url = os.environ['OPENAI_BASE_URL']
        model_name = os.environ.get('OPENAI_MODEL_NAME', 'gpt-4o')    
        api_version = os.environ.get('OPENAI_VERSION','2023-05-15')
        client = AzureOpenAI(api_key=api_key, azure_endpoint=base_url, azure_deployment=model_name, api_version=api_version)
    else:
        api_key = 'ollama'
        base_url = "http://127.0.0.1/11434/v1"
        model_name = 'mistral'
        client = OpenAI(api_key=api_key, base_url=base_url)
    print(f"Using {client.__class__.__name__} with model {model_name}")
    return client, model_name
