from src.loading.csv_loader import carregar_dados_x, carregar_dados_youtube

def main():

    # Dados simulados para tete de carga de dados do youtube

    video_data = {
        "video_id": "1234567890",
        "titulo": "Exemplo de vídeo",
        "descricao": "Esta é uma descrição de vídeo do youtube",
        "data_publicacao": "2023-02-22T12:00:00Z"

    }

    comentarios = [
        "Primeiro comentário de teste!",
        "Segundo comentário de teste!",
        "Outro comentário para teste."
    ]

    # Dados simulados para teste da carga de dados do Twitter
    tweets = [
        {
            "id_str": "tweet1",
            "created_at": "2023-02-22T12:00:00Z",
            "user": {"screen_name": "usuario1"},
            "text": "Texto do tweet 1 de exemplo.",
            "retweet_count": 10,
            "favorite_count": 5
        },
        {
            "id_str": "tweet2",
            "created_at": "2023-02-22T12:05:00Z",
            "user": {"screen_name": "usuario2"},
            "text": "Texto do tweet 2 de exemplo.",
            "retweet_count": 3,
            "favorite_count": 8
        }
    ]

    # Carregar dados do YouTube em arquivos CSV
    print("Carregando dados do YouTube...")
    carregar_dados_youtube(video_data, comentarios,
                           arquivo_video="dados_video_youtube.csv",
                           arquivo_comentarios="comentarios_youtube.csv")
    
    # Carregar dados do Twitter em arquivo CSV
    print("Carregando dados do X...")
    carregar_dados_x(tweets, arquivo="dados_twitter.csv")
    
    print("Pipeline ETL de loading concluído com sucesso!")

if __name__ == "__main__":
    main()