from src.transformation.text_transformation import transformar_texto
import pandas as pd

###########################################
# ETAPA 3: CARGA
###########################################

def carregar_dados_youtube(video_data, comentarios,
                             arquivo_video="dados_video_youtube.csv",
                             arquivo_comentarios="comentarios_youtube.csv"):
    """
    Processa e salva os dados do YouTube em arquivos CSV.
    """
    # Processa a descrição do vídeo
    video_data["descricao"] = transformar_texto(video_data.get("descricao", ""))
    df_video = pd.DataFrame([video_data])
    df_video.to_csv(arquivo_video, index=False, encoding="utf-8")
    
    # Processa os comentários
    comentarios_transformados = [transformar_texto(c) for c in comentarios]
    df_comentarios = pd.DataFrame(comentarios_transformados, columns=["comentario"])
    df_comentarios.to_csv(arquivo_comentarios, index=False, encoding="utf-8")

def carregar_dados_x(tweets, arquivo="dados_twitter.csv"):
    """
    Processa e salva os dados do Twitter em arquivo CSV.
    """
    registros = []
    for tweet in tweets:
        # Se o tweet for retweet, o texto completo pode estar em 'full_text'
        texto = tweet.get("full_text") if "full_text" in tweet else tweet.get("text", "")
        registros.append({
            "id": tweet.get("id_str"),
            "data_criacao": tweet.get("created_at"),
            "usuario": tweet.get("user", {}).get("screen_name"),
            "texto": transformar_texto(texto),
            "retweet_count": tweet.get("retweet_count", 0),
            "favorite_count": tweet.get("favorite_count", 0)
        })
    
    df_x = pd.DataFrame(registros)
    df_x.to_csv(arquivo, index=False, encoding="utf-8")