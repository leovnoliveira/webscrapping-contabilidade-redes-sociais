from src.extraction.x_extraction import extrair_dados_x
from src.extraction.youtube_extraction import extrair_dados_youtube
from src.utils import *

if __name__ == "__main__":

    config = carregar_variaveis_sensiveis()
    print("Rodando extração de dados...")

    # Exemplo de execução
    VIDEO_ID = "Js8yNAOTws8"
    video_data, comentarios = extrair_dados_youtube(config["YOUTUBE_API_KEY"], VIDEO_ID)

    tweets = extrair_dados_x(
        config["BEARER_TOKEN"],
        config["CONSULTA_X"],
        max_results= 10
    )

    print(f"Total de tweets extraídos: {len(tweets)}")
