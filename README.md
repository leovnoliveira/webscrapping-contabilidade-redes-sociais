# Projeto de Webscrapping e Análise de Sentimento para Dados Contábeis

Este repositório contém a implementação de um projeto para a coleta, tratamento e análise de sentimento de dados relacionados a temas de contabilidade e tributação. O foco do projeto é identificar dúvidas e tendências dos usuários por meio de dados coletados de diferentes fontes, como YouTube e Twitter.

## Sumário

- [Objetivos](#objetivos)
- [Planejamento Estratégico](#planejamento-estratégico)
- [Pipeline ETL](#pipeline-etl)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Contribuir](#como-contribuir)
- [Licença](#licença)

## Objetivos

- **Coletar Dados:** Implementar webscrapping para extrair informações de fontes como YouTube (descrição e comentários) e Twitter (tweets, retweets e replies).
- **Normalizar Dados:** Padronizar termos de busca, substituindo ocorrências de “imposto” pelo formato “como declarar imposto de [profissão]”.
- **Analisar Sentimentos:** Aplicar técnicas de processamento de linguagem natural para identificar sentimentos e dúvidas dos usuários.
- **Gerar Insights:** Desenvolver dashboards e relatórios para auxiliar na compreensão dos principais questionamentos e dores dos usuários.

## Planejamento Estratégico

O planejamento estratégico completo está documentado no arquivo [planejamento.md](./planejamento.md). Ele detalha:

- Os objetivos do projeto.
- As etapas, desde a definição do escopo até a validação e monitoramento.
- Uma tabela comparativa dos canais de busca para webscrapping.
- Considerações finais e recomendações de ferramentas e metodologias.

## Pipeline ETL

O pipeline ETL desenvolvido no projeto realiza as seguintes etapas:

1. **Extração:**  
   - Coleta dados do YouTube (descrição de vídeos e comentários).
   - Coleta dados do Twitter (tweets, retweets e replies) usando a API do Twitter via Tweepy.

2. **Transformação:**  
   - Limpeza e normalização dos textos (remoção de URLs, menções, hashtags, etc.).
   - Padronização dos termos que contenham “imposto”.

3. **Carga:**  
   - Armazenamento dos dados transformados em arquivos CSV para análises futuras.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:**  
  - Webscrapping: Scrapy, BeautifulSoup, Selenium  
  - APIs: Google API (YouTube), Tweepy (Twitter)  
  - Análise e Visualização: Pandas, Matplotlib, Seaborn, Plotly, Power BI  
  - Processamento de Linguagem Natural: NLTK, spaCy, VADER, TextBlobPT, BERTimbau

## Como Contribuir

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature ou correção (`git checkout -b minha-feature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

*Para converter este README em PDF, você pode utilizar ferramentas como o [Pandoc](https://pandoc.org/) ou editores de Markdown que possuam opção de exportação para PDF.*
