import os
from src.utils import *
from src.extraction.x_extraction import extrair_dados_x
from src.extraction.youtube_extraction import extrair_dados_youtube

def main():

    dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    print("Procurando .env em:", dotenv_path )
    load_dotenv(dotenv_path=dotenv_path)

    config = carregar_variaveis_sensiveis()
    print("Rodando extração de dados...")

    VIDEO_ID = "Js8yNAOTws8"
    video_data, comentarios = extrair_dados_youtube(api_key=config.get("YOUTUBE_API_KEY"), video_id= VIDEO_ID)

    tweets = extrair_dados_x(
        config["BEARER_TOKEN"],
        config["CONSULTA_X"],
        max_results= 10
    )

    print(f"Total de tweets extraídos: {len(tweets)}")
    print(f"Conteúdo dos tweets extraíos: {tweets}")
    print(f"Total de videos coletados: {len(video_data)}")
    print(f"Total de comentários coletados: {len(comentarios)}")


if __name__ == "__main__":
    main()