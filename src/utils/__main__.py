import os
from dotenv import load_dotenv
from src.utils.config import carregar_variaveis_sensiveis

def main():
    # Carrega as variáveis definidas no arquivo .env
    load_dotenv()
    
    # Carrega as variáveis sensíveis usando a função definida em config.py
    config = carregar_variaveis_sensiveis()
    BEARER_TOKEN = config.get("BEARER_TOKEN")
    CONSULTA_X = config.get("CONSULTA_X")
    YOUTUBE_API_KEY = config.get('YOUTUBE_API_KEY')
    
    # Exibe as variáveis carregadas para verificação
    print("BEARER_TOKEN =", BEARER_TOKEN)
    print("CONSULTA_X =", CONSULTA_X)
    print("YOUTUBE_API_KEY", YOUTUBE_API_KEY)

if __name__ == "__main__":
    main()
