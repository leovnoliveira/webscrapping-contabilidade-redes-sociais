import tweepy
import time


def extrair_dados_x(bearer_token, consulta, max_results=10):

    """
    Extraí dados do X (tweets, retweets e replies) utilizando a API do X    
    """

    # Autenticação com API do Twitter

    client = tweepy.Client(bearer_token=bearer_token)

    if isinstance(consulta, list):
        query = " OR ".join(consulta)
    else:
        query = consulta

    print("Consulta realizada foi:", query)

    try:
        response = client.search_recent_tweets(query = query, max_results = max_results)
        tweets = response.data if response.data else []
        return tweets
    
    except tweepy.errors.TooManyRequests as e:
        # Extraindo o tempo de espera a partir dos cabeçalhos
        reset_time = None
        if e.response and 'x-rate-limit-reset' in e.response.headers:
            reset_time = int(e.response.headers['x-rate-limit-reset'])
            wait_time = max(0, reset_time - int(time.time()))

        else:
            # Valor padrão: 15 minutos 900 segundos
            wait_time = 900

            print(f"Limite de requisições excedido. Aguardando {wait_time} segundos...")
            time.sleep(wait_time)
            # Após o período de espera, tenta novamente

            return extrair_dados_x(bearer_token, consulta, max_results)