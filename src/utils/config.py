import os
from dotenv import load_dotenv

def carregar_variaveis_sensiveis():

    load_dotenv()

    """
    Carrega as variáveis sensíveis do arquivo .env e retorna um dicionário com as chaves necessárias
    
    """

    variaveis = {
        "BEARER_TOKEN": os.getenv("BEARER_TOKEN"),
        "YOUTUBE_API_KEY": os.getenv("YOUTUBE_API_KEY"),
        "CONSULTA_TWITTER": ["contabilidade online", "imposto infoprodutor", "imposto representante comercial",
                             "contabilidade digital", "imposto revendedor de veículos", "imposto", "impostos"]  # Exemplo de palavra-chave
    }
    
    return variaveis