import ollama

# Certifique-se que o Ollama está rodando e o modelo foi baixado
# (ex: ollama pull llama3)
MODEL_NAME = 'llama3' # Ou 'deepseek-coder:6.7b' se você baixou esse

try:
    print(f"Tentando se comunicar com o modelo '{MODEL_NAME}' via Ollama...")
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                'role': 'user',
                'content': 'Why is the sky blue?',
            },
        ]
    )
    print("\nResposta do modelo:")
    print(response['message']['content'])
    print("\nComunicação com Ollama bem-sucedida!")

except Exception as e:
    print(f"Erro ao se comunicar com o Ollama ou o modelo '{MODEL_NAME}': {e}")
    print("Verifique se o Ollama está em execução e se o modelo foi baixado corretamente (ollama list).")
    print("Se o Ollama estiver rodando, talvez o modelo especificado não esteja disponível ou haja um problema de rede local.")

