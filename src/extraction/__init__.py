from src.extraction.x_extraction import extrair_dados_x
from src.extraction.youtube_extraction import extrair_dados_youtube
from src.utils.__init__ import *
from src.utils.config import carregar_variaveis_sensiveis


if __name__ == "__main__":


    config = carregar_variaveis_sensiveis()

    # --- EXTRAÇÃO ---
    # Dados do YouTube
    VIDEO_ID = "Js8yNAOTws8"  # Substitua pelo ID real do vídeo
    video_data, comentarios = extrair_dados_youtube(config["YOUTUBE_API_KEY"], VIDEO_ID)
    
    # Dados do Twitter
    tweets = extrair_dados_x(
        config["BEARER_TOKEN"],
        config["CONSULTA_TWITTER"],
        max_results= 10
    )

    for tweet in tweets:
        print(tweets.text)