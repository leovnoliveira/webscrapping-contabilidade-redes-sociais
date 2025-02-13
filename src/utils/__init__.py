from config import carregar_variaveis_sensiveis
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()

    config = carregar_variaveis_sensiveis()
    BEARER_TOKEN = config["BEARER_TOKEN"]
    CONSULTA_TWITTER = config["CONSULTA_TWITTER"]