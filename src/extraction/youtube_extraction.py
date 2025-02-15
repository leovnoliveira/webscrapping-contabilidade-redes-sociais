from googleapiclient.discovery import build
from src.utils.config import *


def extrair_dados_youtube(api_key, video_id):

    """
    Extrai dados do YouTube, incluindo informações do vído e comentários.
    
    """

    youtube = build('youtube', 'v3', developerKey=api_key, credentials = None)

    # Extração dos dados do vídeo (descrição, título, data de publicação etc)

    resposta_video = youtube.videos().list(
        part = 'snippet',
        id = video_id
    ).execute()

    video_data = {}
    if resposta_video.get('items'):
        snippet = resposta_video['items'][0]['snippet']
        video_data = {
            "video_id": video_id,
            "titulo": snippet.get("title"),
            "descricao": snippet.get("description"),
            "data_publicacao": snippet.get("publishedAt")
        }

    # Extração dos comentários do vídeo
    comentarios = []
    try:
        resposta_comentarios = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=100  # Limita a 100 comentários (exemplo)
        ).execute()
        
        for item in resposta_comentarios.get("items", []):
            texto_comentario = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comentarios.append(texto_comentario)
    except Exception as e:
        print("Erro ao extrair comentários:", e)
    
    
    return video_data, comentarios