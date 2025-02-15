from src.loading.csv_loader import carregar_dados_youtube
from src.loading.csv_loader import carregar_dados_x

if __name__ == "__main__":

    # --- TRANSFORMAÇÃO E CARGA ---
    carregar_dados_youtube()
    carregar_dados_x()
    
    print("Pipeline ETL concluído com sucesso!")