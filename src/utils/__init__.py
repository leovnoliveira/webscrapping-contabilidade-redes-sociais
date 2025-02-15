import os
from src.utils.config import carregar_variaveis_sensiveis
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise ValueError("YOUTUBE_API_KEY não está definida! Verifique seu arquivo .env.")

    print("YOUTUBE_API_KEY =", api_key)

    config = carregar_variaveis_sensiveis()
    BEARER_TOKEN = config["BEARER_TOKEN"]
    CONSULTA_X = config["CONSULTA_X"]
    YOUTUBE_API_KEY = config['YOUTUBE_API_KEY']
    