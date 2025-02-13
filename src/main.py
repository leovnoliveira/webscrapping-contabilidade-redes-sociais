from src.utils.config import carregar_variaveis_sensiveis
from src.extraction.youtube_extraction import extrair_dados_youtube
from src.extraction.x_extraction import extrair_dados_x
from src.loading.csv_loader import carregar_dados_youtube, carregar_dados_x

def main():
    # Carrega as variáveis sensíveis
    config = carregar_variaveis_sensiveis()

    # Extração dos dados
    VIDEO_ID = "ydWXdLIBWDY"  # Substitua pelo ID correto do vídeo
    video_data, comentarios = extrair_dados_youtube(config["YOUTUBE_API_KEY"], VIDEO_ID)
    
    tweets = extrair_dados_x(
        config["TWITTER_BEARER_TOKEN"],  # ou outro token conforme sua implementação
        config["CONSULTA_X"],
        max_results=10
    )

    # Transformação (se as funções de transformação estiverem integradas nas funções de carregamento ou separadas)
    # Pode ser chamada dentro dos métodos de carregamento, se necessário.

    # Carregamento dos dados
    carregar_dados_youtube(video_data, comentarios)
    carregar_dados_x(tweets)

    print("Pipeline ETL concluído com sucesso!")

if __name__ == "__main__":
    main()
