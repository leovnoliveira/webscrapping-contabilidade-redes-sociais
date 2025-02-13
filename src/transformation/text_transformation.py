import re


###########################################
# ETAPA 2: TRANSFORMAÇÃO
###########################################

def transformar_texto(texto):
    """
    Realiza a limpeza do texto, removendo URLs, menções, hashtags e espaços extras.
    """
    # Remove URLs
    texto = re.sub(r'http\S+', '', texto)
    # Remove menções (@usuario) e hashtags (#termo)
    texto = re.sub(r'[@#]\S+', '', texto)
    # Remove espaços extras e quebras de linha
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto