import os
from dotenv import load_dotenv
from src.utils.config import carregar_variaveis_sensiveis
from src.extraction.youtube_extraction import extrair_dados_youtube
from src.extraction.x_extraction import extrair_dados_x
from src.transformation import *
from src.loading.csv_loader import carregar_dados_youtube, carregar_dados_x

def main():


    dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    print("Procurando .env em:", dotenv_path )
    load_dotenv(dotenv_path=dotenv_path)

    # Carrega as variáveis sensíveis
    config = carregar_variaveis_sensiveis()
    print("Rodando extração de dados...")

    # Extração dos dados
    VIDEO_ID = "ydWXdLIBWDY"  # Substitua pelo ID correto do vídeo
    video_data, comentarios = extrair_dados_youtube(config["YOUTUBE_API_KEY"], VIDEO_ID)
    
    tweets = extrair_dados_x(
        config["BEARER_TOKEN"],  # ou outro token conforme sua implementação
        config["CONSULTA_X"],
        max_results=10
    )
    # Transformação (se as funções de transformação estiverem integradas nas funções de carregamento ou separadas)
    # Pode ser chamada dentro dos métodos de carregamento, se necessário.

    tweets_tratados = []
    for tweet in tweets:
        tweet_dict = {
            "id": tweet.id,
            "text": transformar_texto(tweet.text),
            "created_at": tweet.created_at,
            "author_id": getattr(tweet, "author_id", None)
        }
        tweets_tratados.append(tweet_dict)
        
    print(f"Total de tweets após tratamento: {len(tweets_tratados)}")
    print(f"Os tweets tratados são: {tweets_tratados}")

    comentarios_tratados = [transformar_texto(comentario) for comentario in comentarios]

    print(f"Total de comentários após tratamento: {len(comentarios_tratados)}")
    print(f"Os comentários tratados são: {comentarios}")

    

    # Carregamento dos dados
    carregar_dados_youtube(video_data, comentarios_tratados)
    carregar_dados_x(tweets_tratados)

    print("Pipeline ETL concluído com sucesso!")

if __name__ == "__main__":
    main()
